"""Funtions to translate text from one language to another """
import os
from logging import getLogger
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

# Read the .env file
load_dotenv()
# Get the service URL and API key from the environment variables
apikey = os.environ['apikey']
url = os.environ['url']

# Create an authenticator object
authenticator = IAMAuthenticator(apikey)

# Create a Language Translator object
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

# Print a list of all the languages supported by the service
# languages = language_translator.list_identifiable_languages().get_result()
# print(json.dumps(languages, indent=2))


def english_to_french(english_text):
    """Translates English to French"""
    try:
        french_text = language_translator.translate(
            text=english_text, model_id='en-fr').get_result()
        return french_text['translations'][0]['translation']
    except Exception as excption:
        # Log the error
        getLogger().error(excption)
        # Return an empty string
        return ""


def french_to_english(french_text):
    """Translates French to English"""
    try:
        english_text = language_translator.translate(
            text=french_text, model_id='fr-en').get_result()
        return english_text['translations'][0]['translation']
    except Exception as excption:
        # Log the error
        getLogger().error(excption)
        return ""
