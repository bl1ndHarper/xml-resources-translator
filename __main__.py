import json
from translator_factory import get_translator
from ui.interaction import (
    ask_for_config,
    ask_resource_type,
    ask_comment_choice_skipped,
    ask_comment_choice_translated
)
from core.translator_engine import process_file

def load_config(config_path_):
    with open(config_path_, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    config_path = ask_for_config()
    config = load_config(config_path)
    translator = get_translator()
    resource_type = ask_resource_type()
    add_comments_to_skipped = ask_comment_choice_skipped()
    add_comments_to_translated = ask_comment_choice_translated()
    process_file(config, translator, resource_type, add_comments_to_skipped, add_comments_to_translated)
