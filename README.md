# YouTube Video Downloader com Flask e yt-dlp

Este projeto é um aplicativo web simples para baixar vídeos do YouTube, desenvolvido usando Flask e yt-dlp.

## Funcionalidades

1. **Busca de informações sobre o vídeo**: Insira a URL de um vídeo do YouTube para obter detalhes como título e thumbnail.
2. **Download do vídeo**: Baixe o vídeo no formato e na qualidade especificados.

## Requisitos

- Python 3.7+
- yt-dlp
- Flask

## Como usar

1. Clone este repositório:

   ```bash
   git clone <URL_DO_REPOSITORIO>
   cd <NOME_DO_REPOSITORIO>
   ```

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

3. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

4. Abra seu navegador e acesse:

   ```
   http://127.0.0.1:5000
   ```

5. Insira a URL do vídeo do YouTube e siga as instruções para obter informações e fazer o download.

## Estrutura do Projeto

```
.
├── app.py                 # Código principal do aplicativo Flask
├── templates
│   └── index.html         # Interface do usuário
├── downloads              # Pasta onde os vídeos baixados serão salvos
├── requirements.txt       # Lista de dependências do projeto
└── README.md              # Documentação do projeto
```

## Requisitos.txt

Certifique-se de incluir as dependências no arquivo `requirements.txt`:

```
flask
yt-dlp
```

## Observações

1. Certifique-se de que a pasta `downloads` existe ou será criada automaticamente no mesmo diretório onde o script é executado.
2. Este projeto é apenas para uso educacional. Use-o com responsabilidade e de acordo com as políticas do YouTube.

## Autor

Desenvolvido por Gustavo Pinheiro.

## Licença

Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais informações.


