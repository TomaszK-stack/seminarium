from pydub import AudioSegment
import os
from pathlib import Path

AudioSegment.converter = "C:\\Users\\korni\\Downloads\\ffmpeg-2023-11-02-git-4dbfb52230-full_build\\bin\\ffmpeg.exe"
AudioSegment.ffmpeg = "C:\\Users\\korni\\Downloads\\ffmpeg-2023-11-02-git-4dbfb52230-full_build\\bin\\ffmpeg.exe"
AudioSegment.ffprobe = "C:\\Users\\korni\\Downloads\\ffmpeg-2023-11-02-git-4dbfb52230-full_build\\bin\\ffprobe.exe"
source_path = r"C:\\Users\\korni\\seminarium\\semi\\source"
dest_path = r"C:\\Users\\korni\\seminarium\\semi\\exported"

for file in os.listdir(source_path):
    music_type = os.listdir(os.path.join(source_path , file))
    try:
        os.mkdir(os.path.join(dest_path , file))
    except FileExistsError:
        pass

    for music in music_type:
        mp3 = os.path.join(source_path + "\\" + file,  music)
        # mp3 = source_path + "\\"+file+"\\"+music
        print(mp3)
        audio = AudioSegment.from_mp3(mp3)
        export = dest_path+ "\\" + file + "\\" + music
        audio.export(export , format = "mp3")


