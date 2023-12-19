import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import re
from pygame import mixer
from time import sleep

mixer.init(buffer=512)

def audio_p_texto(caminho_audio, idioma):
    r = sr.Recognizer()
    with sr.AudioFile(caminho_audio) as source:
        audio = r.record(source)
    try:
        texto = r.recognize_google(audio, language=idioma)
        return texto
    except:
        return "Me desculpe entendi o que você falou, tente outro áudio."
    
def tradutor(texto_original, idioma_destino):
    translator = Translator()
    traducao = translator.translate(texto_original, dest=idioma_destino)
    return traducao.text

def nome_arquivo(file_path):
    pattern = r'/([^/]+)\.wav$'
    match = re.search(pattern, file_path)
    if match:
        file_name = match.group(1)
        return file_name
    else:
        return "traducao"

def sintetizador(texto, idioma, nome_arquivo):
    tts = gTTS(texto, lang=idioma)
    tts.save("ponderada_8/falas_traduzidas/" + nome_arquivo + ".mp3")
    return 

def reproduzir_audio(caminho_audio):
    objeto_audio = mixer.Sound(caminho_audio)
    duracao_audio = objeto_audio.get_length()
    objeto_audio.play()
    sleep(duracao_audio)
    return

def exemplo():
    print("\nBem vindo ao tradutor de voz em texto e de texto em voz.")
    print("\n Reproduzindo um exemplo")

    caminho = "ponderada_8/falas_originais/verdade_absoluta.wav"

    transcricao = audio_p_texto(caminho, "pt-BR")
    print("\nTranscição no idioma original: "+transcricao)

    traducao = tradutor(transcricao, "en")
    print("\nTradução: "+traducao)

    nome = nome_arquivo(caminho)
    sintetizador(traducao, "en", nome)
    print("\nReproduzindo áudio da tradução da transcrição original.")
    reproduzir_audio("ponderada_8/falas_traduzidas/" + nome + ".mp3")

    return "\nExemplo executado com sucesso!"

def main():
    exemplo()
    print("\n Iniciando modo de tradução de áudio para texto e de texto para áudio.")
    print("\n Para sair digite 'sair'.")

    terminar = False
    while terminar != True:
        caminho_audio = input("\nDigite o caminho do áudio que deseja traduzir: ")
        idoma_origem = input("\nDigite o idioma do áudio que deseja traduzir [pt-BR, en, es, fr, de, it, ru, ja, zh-CN]: ")
        idioma_destino = input("\nDigite o idioma para qual deseja traduzir [pt-BR, en, es, fr, de, it, ru, ja, zh-CN]: ")

        transcricao = audio_p_texto(caminho_audio, idoma_origem)
        print("\nTranscição no idioma original: "+transcricao)

        traducao = tradutor(transcricao, idioma_destino)
        print("\nTradução: "+traducao)

        nome = nome_arquivo(caminho_audio)
        sintetizador(traducao, idioma_destino, nome)
        print("\nReproduzindo áudio da tradução da transcrição original.")
        reproduzir_audio("ponderada_8/falas_traduzidas/" + nome + ".mp3")

    return "\nPrograma finalizado com sucesso!"

if __name__ == "__main__":
    main()