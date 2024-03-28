import requests
import pygame
import cv2
from gtts import gTTS
from dotenv import load_dotenv
from pathlib import Path
import os
import sys

dotenv_path_voice = Path(str(Path().resolve())+'/env/voice.env')
dotenv_path_avatar = Path(str(Path().resolve())+'/env/avatar.env')

load_dotenv(dotenv_path=dotenv_path_voice)
load_dotenv(dotenv_path=dotenv_path_avatar)

TTS:bool = int(os.getenv('TTS'))
GTTS_LANG:str = os.getenv('GTTS_LANG')
URL_ELEVENLAB:str = os.getenv('URL_ELEVENLAB')
API_KEY_ELEVENLAB:str = os.getenv('API_KEY_ELEVENLAB')
VOICE_ID:str = os.getenv('VOICE_ID')
PATH_AUDIO_FILE:str = str(Path(str(Path().resolve())+str(os.getenv('PATH_AUDIO_FILE'))))
MUTE_IMG:str = str(Path(str(Path().resolve())+str(os.getenv('MUTE_IMG'))))
TALK_IMG:str = str(Path(str(Path().resolve())+str(os.getenv('TALK_IMG'))))

CHUNK_SIZE = 1024

#Setup for the avatar
avatar_mute = cv2.imread(MUTE_IMG)
avatar_talk = cv2.imread(TALK_IMG)

delay_talk:int = 100
# End of setup for the avatar


headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": API_KEY_ELEVENLAB
}

data = {
  "text": "",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.43,
    "similarity_boost": 0.76
  }
}

def text_to_speech(ai_message:str):
    if (TTS):
        output = gTTS(text=ai_message, lang = GTTS_LANG, slow = False)
        output.save(PATH_AUDIO_FILE)
    else :
      data["text"] = ai_message
      response = requests.post(str(URL_ELEVENLAB+VOICE_ID), json=data, headers=headers)
      with open(PATH_AUDIO_FILE, 'wb') as f:
          for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
              if chunk:
                  f.write(chunk)
  
def talking():
  voice = pygame.mixer.Channel(5)

  sound = pygame.mixer.Sound(PATH_AUDIO_FILE)

  voice.play(sound)

  while voice.get_busy():
      if cv2.getWindowProperty("Avatar",cv2.WND_PROP_VISIBLE) < 1:
            sys.exit()
      cv2.imshow("Avatar",avatar_talk)
      cv2.waitKey(delay_talk)
  cv2.imshow("Avatar",avatar_mute)
  cv2.waitKey(20)