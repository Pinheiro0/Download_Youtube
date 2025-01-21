from flask import Flask, request, jsonify, render_template
import yt_dlp

app = Flask(__name__)

@app.route('/')
def index():
    # Rendeiriza a página inicial do aplicativo
    return render_template('index.html')

@app.route('/get_video_details', methods=['POST'])
def get_video_details():
    try:
        # Obter os dados da requisição JSON
        data = request.get_json()
        url = data.get('url')
        if not url:
            raise ValueError("A URL não foi fornecida.")

        # Configurações para o yt-dlp para extrair informações do vídeo
        ydl_opts = {
            'quiet': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=False)
            title = result.get('title', 'Título não encontrado')
            thumbnail_url = result.get('thumbnail', '')

        # Retorna os detalhes do vídeo como uma resposta JSON
        return jsonify({
            'success': True,
            'title': title,
            'thumbnail_url': thumbnail_url
        })
    except Exception as e:
        # Log do erro para depuração
        print(f"Erro ao processar a URL: {e}")
        return jsonify({'success': False, 'error': str(e)})

@app.route('/download_video', methods=['POST'])
def download_video():
    try:
        # Obter os dados da requisição JSON
        data = request.get_json()
        url = data.get('url')
        if not url:
            raise ValueError("A URL não foi fornecida.")

        # Configurações para o yt-dlp para realizar o download do vídeo
        ydl_opts = {
            'quiet': False,  # Mostrar logs de progresso no console
            'format': 'best',
            'outtmpl': './downloads/%(title)s.%(ext)s',  # Caminho e formato do arquivo de saída
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        # Resposta JSON indicando sucesso
        return jsonify({'success': True, 'message': 'Download concluído!'})
    except Exception as e:
        # Log do erro para depuração
        print(f"Erro ao baixar o vídeo: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    # Executa o aplicativo Flask em modo de depuração
    app.run(debug=True)
