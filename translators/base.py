class BaseTranslator:
    def detect_language(self, text: str) -> str:
        raise NotImplementedError

    def translate_text(self, text: str, source_lang: str, target_lang: str) -> str:
        raise NotImplementedError
