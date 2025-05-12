import os
from google.cloud import translate_v2 as translate
from langdetect import detect
from translators.base import BaseTranslator

class GoogleTranslator(BaseTranslator):
    def __init__(self):
        if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
            raise EnvironmentError("GOOGLE_APPLICATION_CREDENTIALS not found in .env")
        self.client = translate.Client()

    def detect_language(self, text: str) -> str:
        try:
            return detect(text)
        except Exception:
            return "unknown"

    def translate_text(self, text: str, source_lang: str, target_lang: str) -> str:
        result = self.client.translate(
            text,
            source_language=source_lang,
            target_language=target_lang,
            format_="text",
            model="nmt"
        )
        return result["translatedText"]
