from flask import Flask, render_template, request
import os
import subprocess
import json

app = Flask(__name__)

def get_video_info(video_url):
    try:
        command = [
            "yt-dlp",
            "--dump-json",  # Retorna as informações do vídeo em formato JSON
            video_url
        ]
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        video_info = json.loads(result.stdout)
        return video_info.get("title"), video_info.get("thumbnail")
    except Exception as e:
        print(f"Erro ao obter informações com yt-dlp: {e}")
        return "Título não disponível (erro ao acessar informações)", "https://via.placeholder.com/300"

def download_video(video_url, download_path):
    try:
        command = [
            "yt-dlp",
            "-o",
            os.path.join(download_path, "%(title)s.%(ext)s"),
            video_url
        ]
        subprocess.run(command, check=True)
        return "Download completo!"
    except Exception as e:
        return f"Erro ao baixar o vídeo: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    video_url = None
    title = None
    thumbnail_url = None
    message = None
    if request.method == 'POST':
        video_url = request.form.get('video_url')
        download_type = request.form.get('download_type')

        if video_url:
            title, thumbnail_url = get_video_info(video_url)

            # Apenas inicia o download após mostrar as informações do vídeo
            if request.form.get('start_download') == 'yes':
                download_path = os.path.expanduser('~/Downloads')  # Pasta padrão de downloads
                message = download_video(video_url, download_path)

    return render_template('index.html', video_url=video_url, title=title, thumbnail_url=thumbnail_url, message=message)

if __name__ == '__main__':
    app.run(debug=True)
