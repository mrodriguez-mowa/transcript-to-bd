from pydub import AudioSegment
import os


audios = os.listdir("./audios")

for audio in audios:
  audiox = AudioSegment.from_file("./audios/"+audio, "gsm")
  audiox.export("./audios_ok/"+audio[:-4]+".wav", format="wav")