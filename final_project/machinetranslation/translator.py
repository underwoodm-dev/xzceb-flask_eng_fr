"""
    Translator File in order to facilitate translation.
"""
import os
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']

authenticator = IAMAuthenticator(APIKEY)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2021-08-16',
    authenticator=authenticator
)

LANGUAGE_TRANSLATOR.set_service_url(URL)

def english_to_french(english_text):
    """
    Translate text from English to French
    """
    if english_text == '':
        return ''
    translation = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        model_id='en-fr').get_result()
    return translation.get('translations')[0].get('translation')

def french_to_english(french_text):
    """
    Translate text from French to English
    """
    if french_text == '':
        return ''
    translation = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        model_id='fr-en').get_result()
    return translation.get('translations')[0].get('translation')
