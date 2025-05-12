import os
import deepl
from dotenv import load_dotenv
from langdetect import detect
from translators.base import BaseTranslator

load_dotenv()

class DeepLTranslator(BaseTranslator):
    def __init__(self):
        api_key = os.getenv("DEEPL_API_KEY")
        if not api_key:
            raise ValueError("Couldn't find DEEPL_API_KEY in .env")
        self.translator = deepl.Translator(api_key)

    def detect_language(self, text: str) -> str:
        try:
            return detect(text)
        except Exception:
            return "unknown"

    def translate_text(self, text: str, source_lang: str, target_lang: str) -> str:
        result = self.translator.translate_text(
            text,
            source_lang=source_lang,
            target_lang=target_lang,
            tag_handling="xml"
        )
        return result.text
