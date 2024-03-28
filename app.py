from src.chatbot import generationPrompt,initialize
from src.vtuberVoice import text_to_speech,talking
import cv2
import os
from pathlib import Path
from dotenv import load_dotenv
import sys

dotenv_path_avatar = Path(str(Path().resolve())+'/env/avatar.env')
load_dotenv(dotenv_path=dotenv_path_avatar)

MUTE_IMG:str = str(Path(str(Path().resolve())+str(os.getenv('MUTE_IMG'))))
TALK_IMG:str = str(Path(str(Path().resolve())+str(os.getenv('TALK_IMG'))))

avatar_mute = cv2.imread(MUTE_IMG)
avatar_talk = cv2.imread(TALK_IMG)

def userInput():
    cv2.imshow("Avatar",avatar_mute)
    cv2.waitKey(20)
    user_message:str = input()
    user_message = user_message.replace('\n', '')
    response = generationPrompt(user_message)
    print(response)
    text_to_speech(response)
    talking()

initialize()
cv2.imshow("Avatar",avatar_mute)
cv2.waitKey(20)
while True:
    try:
        if cv2.getWindowProperty("Avatar",cv2.WND_PROP_VISIBLE) < 1:
            sys.exit()
        userInput()
        if cv2.getWindowProperty("Avatar",cv2.WND_PROP_VISIBLE) < 1:
            sys.exit()
    except KeyboardInterrupt:
        sys.exit()
