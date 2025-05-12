from translators.base import BaseTranslator

class StubTranslator(BaseTranslator):
    def detect_language(self, text: str) -> str:
        return "CN"

    def translate_text(self, text: str, source_lang: str, target_lang: str) -> str:
        return f"[{target_lang}] {text}"
