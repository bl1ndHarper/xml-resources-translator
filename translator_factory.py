from translators.deepl_translator import DeepLTranslator
from translators.stub_translator import StubTranslator
from translators.google_translator import GoogleTranslator

def get_translator():
    print("🧠 Available translators:")
    print("1. DeepL")
    print("2. Google Cloud Translate")
    print("3. Stub (fake)")
    choice = input("Select a translator (1 або 2): ").strip()

    if choice == "1":
        return DeepLTranslator()
    elif choice == "2":
        return GoogleTranslator()
    elif choice == "3":
        return StubTranslator()
    else:
        print("❌ Out of range. Using default Stub.")
        return StubTranslator()
