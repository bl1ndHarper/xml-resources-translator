import os

def ask_for_config():
    configs_folder = "configs"
    available_configs = [f for f in os.listdir(configs_folder) if f.endswith(".json")]

    print("🛠️ Available configurations:")
    for idx, config_file in enumerate(available_configs, 1):
        print(f"{idx}. {config_file}")

    choice = input(f"Select a config (or press Enter for default): ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(available_configs):
        selected_config = available_configs[int(choice) - 1]
        config_path = os.path.join(configs_folder, selected_config)
        print(f"Using config: {selected_config}")
    else:
        config_path = "config.json"
        print("⚙️ Using default config.json")

    return config_path

def ask_resource_type():
    print("🧩 Available resource types to work with:")
    print("1. strings (<string />)")
    print("2. arrays (<[type]-array><item /><[type]-array>)")
    choice = input("Select a type (1 or 2): ").strip()
    if choice == "2":
        return "array"
    return "string"


def ask_comment_choice_skipped():
    while True:
        print("💬 Add comments to untranslated lines? (y/n or h for help)")
        choice = input("> ").strip().lower()
        if choice == "h":
            print("    If the detected language of an item is not in range of configs \"allowed_lang_codes\",\n"
                  "    it won't be translated and can be commented as <!-- TODO: [NOT_TRANSLATED: detected_lang = {detected_lang}] -->\n"
                  "    so you can easily find them and translate manually later.\n\n"
                  "    Please, make sure your config allows as much languages as it is relevant for your source language\n"
                  "    as some words and phrases can be mistakenly considered to be not the language they are.\n"
                  "    For example, some english words can be detected as german, italian etc. and chinese as korean or vietnamese.\n\n"
                  "    You can turn off language detection and make translator parse everything despite the language of a line.\n"
                  "    To do that, define \"allowed_lang_codes\" as an empty array in your config (\"allowed_lang_codes\":[])")
            continue
        else: break
    return choice == "y"


def ask_comment_choice_translated():
    while True:
        print("💬 Add comments to successfully translated lines? (y/n or h for help)")
        choice = input("> ").strip().lower()
        if choice == "h":
            print("    Successfully translated lines can be marked with <!-- DO_NOT_TRANSLATE --> comment.\n"
                  "    It is useful if you'll decide to commit a second pass translation or just want to see which lines are translated successfully.\n"
                  "    The Translator will ignore marked lines and will not try to translate them again.")
            continue
        else: break
    return choice == "y"
