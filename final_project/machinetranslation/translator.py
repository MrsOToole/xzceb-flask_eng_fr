import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
authenticator = IAMAuthenticator('fCueMx8HYuA03p73AcS1PS2PyJT_smeOjVu_9Rb_T4ie')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator)

language_translator.set_service_url
('https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/40a7af5a-3de6-44b2-a3a5-33dcd1033327')

def englishToFrench(englishText):
#Translates English to French
    frenchtranslation = language_translator.translate(text=englishText, model_id='en-fr').get_result()
    return french_text['translations'][0]['translation'] 

def frenchToEnglish(frenchText):
    #translates French to English
    english_text = language_translator.translate(text=frenchText, model_id= 'fr-en').get_result()
    return english_text['translations'][0]['translation'] 

