#YouTube Video Downloader com Flask e yt-dlp

Este projeto é um aplicativo web simples para baixar vídeos do YouTube, desenvolvido usando Flask e yt-dlp.

Funcionalidades

Busca de informações sobre o vídeo: Insira a URL de um vídeo do YouTube para obter detalhes como título e thumbnail.

Download do vídeo: Baixe o vídeo no formato e na qualidade especificados.

Requisitos

Python 3.7+

yt-dlp

Flask

Como usar

Clone este repositório:

git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_REPOSITORIO>

Instale as dependências necessárias:

pip install -r requirements.txt

Inicie o servidor Flask:

python app.py

Abra seu navegador e acesse:

http://127.0.0.1:5000

Insira a URL do vídeo do YouTube e siga as instruções para obter informações e fazer o download.

Estrutura do Projeto

.
├── app.py                 # Código principal do aplicativo Flask
├── templates
│   └── index.html         # Interface do usuário
├── downloads              # Pasta onde os vídeos baixados serão salvos
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto

Requisitos.txt

Certifique-se de incluir as dependências no arquivo requirements.txt:

flask
yt-dlp

Observações

Certifique-se de que a pasta downloads existe ou será criada automaticamente no mesmo diretório onde o script é executado.

Este projeto é apenas para uso educacional. Use-o com responsabilidade e de acordo com as políticas do YouTube.

Autor

Desenvolvido por Gustavo Pinheiro.

Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.
