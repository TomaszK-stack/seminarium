import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import os

source_path = "C:\\Users\\korni\\seminarium\\semi\\exported"
dest_path = "C:\\Users\\korni\\seminarium\\semi\\data"
list = ['latino', 'rock']
# for file in os.listdir(source_path):
for file in list:
    music_type = os.listdir(os.path.join(source_path , file))
    try:
        os.mkdir(os.path.join(dest_path , file))
    except FileExistsError:
        pass

    for music in music_type:
        music_name = music.split('.')[0]
        plik_docelowy = os.path.join(source_path + '\\' + file , music)
        plik_dest = dest_path + '\\' + file +"\\"+ music_name + ".csv"
        try:

            if not os.path.exists(os.path.join(dest_path + '\\' + file , music_name + ".csv")):
                y , sr = librosa.load(plik_docelowy)  #
                librosa.feature.melspectrogram(y = y , sr = sr)

                S = librosa.feature.melspectrogram(y = y , sr = sr , n_mels = 128 , fmax = 12000)
                S_dB = librosa.power_to_db(S , ref = np.max)
                librosa.display.specshow(S_dB , x_axis = 'time' , y_axis = 'mel' , sr = sr , fmax = 12000)
                newS_DB = S_dB[:,:2375]
                np.savetxt(plik_dest, newS_DB,delimiter=",")

        except EOFError:
            print(1)

        # plt.colorbar(format = '%+2.0f dB')
        # plt.title('Mel-spektrogram')
        # plt.tight_layout()
        # plt.savefig(os.path.join(dest_path + '//' + file , music_name + '.png'))
        # plt.clf()