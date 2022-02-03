# YouTube Downloader (.MP4 para .MP3)
# ===================================


from pytube import YouTube
from pydub import AudioSegment
import os
import time


link = input('\nEntre com o link:')
yt = YouTube(link)

# Title of the video:
print('Titulo:\t',yt.title)

# Nro. of views:
print('Nro. de views:\t',yt.views)

# Lenght of the video:
print('Tamanho:\t',yt.length)

# # Description of the video:
# print('Descricao:\t',yt.description)

# Rating:
print('Avaliaçoes:\t',yt.rating)

# Author:
print('Publicado por:\t',yt.author)

# Getting only audio from video:
video = yt.streams.filter(only_audio=True).first()

res = input('Continuar?(y/n):\t')
destino = 'C:\\Users\\sliatecinos\\Músicas\\'

if res.lower() == 'y':
    # Starting download:
    print('Time start:', time.strftime("%b %d %Y %H:%M:%S", time.localtime()))
    print('Download em andamento....')
    out_file = video.download(destino)
    print('Download completado!!')

    mp4_audio = AudioSegment.from_file(out_file, format="mp4")

    base, ext = os.path.splitext(out_file)
    mp4_audio.export(base + '.mp3', format="mp3")

    print('Conversao pra MP3, com sucesso!!!')
    files_in_directory = os.listdir(destino)
    filtered_files = [file for file in files_in_directory if file.endswith(".mp4")]
    for file in filtered_files:
        path_to_file = os.path.join(destino, file)
        os.remove(path_to_file)
    print('Time end:', time.strftime("%b %d %Y %H:%M:%S", time.localtime()))

