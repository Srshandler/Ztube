from pytube import YouTube
import moviepy as mp 
import re
import os

link = input('Digite o link do vídeo que deseja baixar: ')
patch = input('Digie a pasta que deseja salvar: ')
yt = YouTube(link)

print('Baixando...')
ys = yt.streams.filter(only_audio=True).first().download(patch)
print('Download completo!')

print('Convertendo arquivos...')
for file in os.listdir(patch):
    if re.search('mp4',file):
        mp4_patch = os.path.join(patch, file)
        mp3_patch = os.path.join(patch, os.path.splitext (file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_patch)
        new_file.write_audiofile(mp3_patch)
        os.remove(mp4_patch)
print('Sucesso!')