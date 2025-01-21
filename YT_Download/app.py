from flask import Flask, request, jsonify, render_template
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_video_details', methods=['POST'])
def get_video_details():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            raise ValueError("A URL não foi fornecida.")

        # Usar yt-dlp para obter os detalhes do vídeo
        ydl_opts = {
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            title = result.get('title', 'Título não encontrado')
            thumbnail_url = result.get('thumbnail', '')

        return jsonify({
            'success': True,
            'title': title,
            'thumbnail_url': thumbnail_url
        })
    except Exception as e:
        print(f"Erro ao processar a URL: {e}")  # Log do erro
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download_video', methods=['POST'])
def download_video():
    try:
        data = request.get_json()
        url = data.get('url')
        if not url:
            raise ValueError("A URL não foi fornecida.")

        # Usar yt-dlp para baixar o vídeo
        ydl_opts = {
            'quiet': False,  # Ativar logs de progresso
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s',  # Caminho do arquivo de saída
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return jsonify({'success': True, 'message': 'Download concluído!'})
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")  # Log do erro
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
