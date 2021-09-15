"""
Translator Module
"""
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv
load_dotenv()
apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(str(apikey))
translator_instance = LanguageTranslatorV3(
    version="2018-05-01", authenticator=authenticator)
translator_instance.set_service_url(str(url))

def english_to_french(english_text):
    """
    Translator
    """
    if not isinstance(english_text, str):
        return None
    if english_text is None:
        return None
    response = translator_instance.translate(
        text=english_text, model_id="en-fr").get_result()
    translation = response['translations'][0]['translation']
    return translation

def french_to_english(french_text):
    """
    translator
    """
    if not isinstance(french_text, str):
        return None
    if french_text is None:
        return None
    response = translator_instance.translate(
        text=french_text, model_id="fr-en").get_result()
    translation = response['translations'][0]['translation']
    return translation
