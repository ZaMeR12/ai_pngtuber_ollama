from deep_translator import GoogleTranslator
import os
from pathlib import Path
from dotenv import load_dotenv

dotenv_path_translator = Path(str(Path().resolve())+'/env/translator.env')
load_dotenv(dotenv_path=dotenv_path_translator)

TRANSLATOR:bool = int(os.getenv('TRANSLATOR'))
USER_LANG_TRANSLATE:str = os.getenv('USER_LANG_TRANSLATE')
CHATBOT_LANG:str = os.getenv('CHATBOT_LANG')



def translate_user(user_message:str)->str:
    if (TRANSLATOR):
        test:str = GoogleTranslator(source='auto', target=USER_LANG_TRANSLATE).translate(user_message)
        return test
    else:
        return user_message
    
def translate_chatbot(chatbot_message:str)->str:
    if (TRANSLATOR):
        return GoogleTranslator(source='auto', target=CHATBOT_LANG).translate(chatbot_message)
    else:
        return chatbot_message