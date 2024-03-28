import os
import traceback
import ollama
from ollama import Client
import pygame
from pathlib import Path
from dotenv import load_dotenv
from src.translator import translate_chatbot, translate_user

pygame.init()

dotenv_path_chatbot = Path(str(Path().resolve())+'/env/chatbot.env')
load_dotenv(dotenv_path=dotenv_path_chatbot)

PATH_LORE:str = str(Path(str(Path().resolve())+str(os.getenv('PATH_LORE'))))
PATH_SUBS:str = str(Path(str(Path().resolve())+str(os.getenv('PATH_SUBS'))))
OLLAMA_SERVER:str = os.getenv('OLLAMA_SERVER')
CHAT_MODEL:str = os.getenv('CHAT_MODEL')


lore:str = "" #This one have to be edit in the lore.tx file.


client:Client = Client(host = OLLAMA_SERVER)


def initialize()->None:
    """Function that initialize the project and the chatbot.
    """

    if (CHAT_MODEL != "" ):
        global lore
        try:
            with open(PATH_LORE, 'r', encoding='utf-8') as file:
                lore = file.read()
        except Exception:
            print("error when reading lore.txt")
            print(traceback.format_exc())
        lore = lore.replace('\n', '')
    global client
    client = Client(host = OLLAMA_SERVER)
    pygame.mixer.init()
    pygame.mixer.set_num_channels(8)
        
def generationPrompt(user_message:str)->str:
    """Function that generate a prompt from the chatbot.

    Args:
        user_message (str): The user message that discuss with the chatbot.

    Returns:
        str: The answer of the chatbot
    """

    try:
        user_message_translate:str = translate_user(user_message)
        print(user_message_translate)
        print("\nStart prompt generating")
        response = client.chat(model= CHAT_MODEL, messages=[{'role': 'system','content': lore,},{'role':'user','content': user_message_translate}],stream=False)
        print("\nEnd prompt generating!")
        chatbot_message:str = translate_chatbot(response['message']['content'])
        with open(PATH_SUBS, "w",encoding='utf-8') as subs:
            subs.write(chatbot_message)
        return chatbot_message
    except ollama.ResponseError as e:
        print('Error:', e.error)
        if e.status_code == 404:
         client.pull(CHAT_MODEL)
    
