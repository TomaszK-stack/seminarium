from pydub import AudioSegment
import os

source_path = "C:\\Users\\korni\\seminarium\\semi\\source"
dest_path = "C:\\Users\\korni\\seminarium\\semi\\exported"

for file in os.listdir(source_path):
    music_type = os.listdir(os.path.join(source_path , file))
    try:
        os.mkdir(os.path.join(dest_path , file))
    except FileExistsError:
        pass

    for music in music_type:
        # mp3 = os.path.join(source_path + "\\" + file,  music)
        mp3 = source_path + "\\"+file+"\\"+music
        print(mp3)
        audio = AudioSegment.from_mp3(mp3)
        export = dest_path+ "\\" + file + "\\" + music
        audio.export(export , format = "mp3")
print("Udało się ")
