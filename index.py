import psycopg2
import os
from pydub import AudioSegment
import uuid

conn = psycopg2.connect("dbname=voice_text_dev user=postgres password=admin")

# Open a cursor to perform database operations
cur = conn.cursor()

transcripts = os.listdir("./transcripts")

audios_ok= os.listdir("./audios_ok")
tiene = 0
no_tiene = 0



for audio in audios_ok[:1]:
  expected_transcript = "medium-"+audio.split(".wav")[0].replace(" ", "")+".txt"
  length = AudioSegment.from_file(f"./audios_ok/{audio}").duration_seconds
  
  if expected_transcript in transcripts:
    tiene += 1
    audio_code = str(uuid.uuid4())
    #cur.execute("INSERT INTO audios (name, audio_code, length, delivered) VALUES (%s, %s, %s, %s)", (audio,audio_code,length,True))

    valid_transcript = []

    with open(f"./transcripts/{expected_transcript}", 'r', encoding='utf-8') as file:
      transcript = file.read()
    
    # SE QUITAN LOS TIMESTAMPS Y SPEAKERS #
    new_transcript = ""
    text = transcript.split('\n')
    


    current_obj = {}
    current_obj["audio_code"] = audio_code

    idx = 0

    #last_speaker = ""
    #last_message = ""

    conversation_parts = []

    for line in text:
      #print(line)

      last_message = ""
      last_speaker = ""


      if len(line) != 0:
        print("no vacia")

        if line.__contains__('SPEAKER'):
          
          last_speaker = line.split(" ")[0] + line.split(" ")[1]

          current_obj["speaker"] = last_speaker 
          
        
        if not line.upper().__contains__('SPEAKER'):
          #valid_transcript.append(line)
          current_obj["text"] = line
          
          # print(current_obj)
        idx += 1
      else:

        if idx > 0:
          print(current_obj)
          #cur.execute("INSERT INTO conversations(message, audio_code, original_speaker) VALUES (%s, %s, %s)", (current_obj["text"], audio_code, current_obj["speaker"]))
          

#conn.commit()


# print(conversation_parts)

#for xd in conversation_parts:
  #print(xd)
  #print("---------------")

#conn.commit()

print(tiene)
print(no_tiene)