# Transcrição de Áudio do YouTube

Um script Python que permite baixar áudio de vídeos do YouTube, transcrever o conteúdo e salvar tanto o áudio quanto a transcrição em arquivos separados.

## 🚀 Funcionalidades

- Download de áudio de vídeos do YouTube
- Transcrição automática do áudio para texto
- Suporte para vídeos em inglês e português
- Organização automática em pastas:
  - `audio/`: armazena os arquivos de áudio (.wav)
  - `transcription/`: armazena as transcrições (.txt)

## 📋 Pré-requisitos

- Python 3.x
- FFmpeg instalado (Configurar path em variáveis de ambiente)
- Bibliotecas Python:
  - yt-dlp
  - SpeechRecognition
  - pydub

## 🔧 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/tradutor-python.git
cd tradutor-python
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Instale o FFmpeg:
   - Baixe o FFmpeg de https://ffmpeg.org/download.html
   - Extraia para `C:\ffmpeg`
   - Certifique-se que o executável está em `C:\ffmpeg\bin\ffmpeg.exe`

## 🎯 Como Usar

1. Execute o script:

```bash
python transcript.py
```

2. Cole a URL do vídeo do YouTube quando solicitado

3. O script irá:
   - Baixar o áudio do vídeo
   - Transcrever o conteúdo
   - Salvar o áudio na pasta `audio/`
   - Salvar a transcrição na pasta `transcription/`

## 📁 Estrutura do Projeto

```
tradutor-python/
├── audio/              # Arquivos de áudio baixados
├── transcription/      # Arquivos de transcrição
├── transcript.py       # Script principal
├── requirements.txt    # Dependências do projeto
├── README.md          # Este arquivo
└── LICENSE            # Licença MIT
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - Para download de vídeos do YouTube
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) - Para transcrição de áudio
- [FFmpeg](https://ffmpeg.org/) - Para processamento de áudio
