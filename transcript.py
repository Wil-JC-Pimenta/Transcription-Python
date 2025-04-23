import os
import time
import yt_dlp
import speech_recognition as sr
import sys
import subprocess
from datetime import datetime
import re

# Cria as pastas se não existirem
for pasta in ['audio', 'transcription']:
    if not os.path.exists(pasta):
        os.makedirs(pasta)

def limpar_nome_arquivo(nome):
    """Remove caracteres inválidos do nome do arquivo"""
    # Remove caracteres especiais e substitui espaços por underscores
    nome_limpo = re.sub(r'[<>:"/\\|?*]', '', nome)
    nome_limpo = nome_limpo.replace(' ', '_')
    return nome_limpo

def verificar_ffmpeg():
    """Verifica se o FFmpeg está instalado e acessível"""
    caminho_ffmpeg = r"C:\ffmpeg\bin\ffmpeg.exe"
    try:
        subprocess.run([caminho_ffmpeg, '-version'], capture_output=True, check=True)
        return caminho_ffmpeg
    except:
        return None

def baixar_audio(url):
    try:
        print("🔽 Baixando o áudio do vídeo...")
        
        # Verifica o FFmpeg
        ffmpeg_path = verificar_ffmpeg()
        if not ffmpeg_path:
            print("❌ FFmpeg não encontrado em C:\\ffmpeg\\bin\\ffmpeg.exe")
            print("Por favor, verifique se o FFmpeg está instalado corretamente.")
            return None, None
        
        # Configurações do yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join('audio', 'audio.%(ext)s'),
            'quiet': True,
            'no_warnings': True,
            'ffmpeg_location': ffmpeg_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            titulo = info.get('title', 'video_sem_titulo')
            titulo_limpo = limpar_nome_arquivo(titulo)
            
            # Renomeia o arquivo de áudio com o título do vídeo
            arquivo_original = os.path.join('audio', 'audio.wav')
            arquivo_final = os.path.join('audio', f'{titulo_limpo}.wav')
            
            if os.path.exists(arquivo_original):
                os.rename(arquivo_original, arquivo_final)
            
        if not os.path.exists(arquivo_final):
            raise Exception("Arquivo de áudio não foi criado corretamente")
            
        print("✅ Áudio baixado com sucesso!")
        return arquivo_final, titulo
            
    except Exception as e:
        print(f"❌ Erro ao baixar o vídeo: {str(e)}")
        return None, None

def transcrever_audio(caminho, titulo):
    if not os.path.exists(caminho):
        print("❌ Arquivo de áudio não encontrado!")
        return

    print("🎙️ Iniciando transcrição...")
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(caminho) as source:
            # Ajusta o reconhecedor para o ruído ambiente
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            
            # Lê o áudio em partes menores para melhor precisão
            audio_data = recognizer.record(source)
            
            # Tenta reconhecer o texto com diferentes configurações
            try:
                texto = recognizer.recognize_google(audio_data, language="en-US")
            except:
                texto = recognizer.recognize_google(audio_data, language="pt-BR")
            
            if texto:
                print("\n📝 Letra reconhecida:")
                # Divide o texto em frases mais legíveis
                frases = [f.strip() for f in texto.split('.') if f.strip()]
                for frase in frases:
                    print(frase)
                    time.sleep(1)
                
                # Salva a transcrição em um arquivo
                titulo_limpo = limpar_nome_arquivo(titulo)
                nome_arquivo = f"{titulo_limpo}.txt"
                caminho_transcricao = os.path.join('transcription', nome_arquivo)
                
                with open(caminho_transcricao, 'w', encoding='utf-8') as f:
                    f.write(texto)
                print(f"\n💾 Transcrição salva em: {caminho_transcricao}")
                print(f"💾 Áudio salvo em: {caminho}")
            else:
                print("❌ Não foi possível reconhecer o texto no áudio")
                
    except Exception as e:
        print(f"❌ Erro na transcrição: {str(e)}")

if __name__ == "__main__":
    try:
        print("🎵 Transcrição de Áudio do YouTube")
        print("=" * 40)
        
        url = input("Cole a URL do YouTube: ").strip()
        if not url:
            print("❌ URL não pode estar vazia!")
            sys.exit(1)
            
        arquivo, titulo = baixar_audio(url)
        if arquivo:
            transcrever_audio(arquivo, titulo)
            
    except KeyboardInterrupt:
        print("\n👋 Programa interrompido pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {str(e)}")
