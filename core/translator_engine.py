import re
from utils.progress import print_status

def get_pattern(resource_type):
    if resource_type == "string":
        return re.compile(r'(<string name="[^"]+">)(.*?)(</string>)', re.DOTALL)
    else:
        return re.compile(r'(<item>)(.*?)(</item>)', re.DOTALL)


def process_file(config, translator, resource_type, add_comments_to_skipped, add_comments_to_translated):
    source_lang = config["source_lang"]
    target_lang = config["target_lang"]
    input_file = config["input_file"]
    output_file = config["output_file"]
    allowed_langs = [lang.lower() for lang in config.get("allowed_lang_codes", [])]

    with open(input_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    print(f"📂 Successfully reached input file. There are {len(lines)} lines in it.")
    print("🚀 Starting translation...")

    pattern = get_pattern(resource_type)

    translated_count = 0
    skipped_lang_count = 0
    skipped_do_not_translate_count = 0

    content = ''.join(lines)

    matches = list(pattern.finditer(content))

    for idx, match in enumerate(matches, 1):
        full = match.group(0)
        prefix = match.group(1)
        text = match.group(2)
        suffix = match.group(3)
        original_text = text.strip()

        if not original_text:
            continue

        # Перевірка на DO_NOT_TRANSLATE перед тегом
        preceding_comment_pattern = re.compile(r'<!--\s*DO_NOT_TRANSLATE\s*-->\s*' + re.escape(full))
        if preceding_comment_pattern.search(content):
            print(f"\n🚫 Block {idx}: marked as DO_NOT_TRANSLATE, skipping the line.")
            skipped_do_not_translate_count += 1
            continue

        detected_lang = translator.detect_language(original_text).lower()

        if allowed_langs and detected_lang not in allowed_langs:
            print(f"\n⚠️ Block {idx}: detected lang '{detected_lang}' ≠ allowed {allowed_langs}")
            skipped_lang_count += 1
            if add_comments_to_skipped:
                mark = f"<!-- TODO: [NOT_TRANSLATED: detected_lang = {detected_lang}] -->"
                content = content.replace(full, mark + full)
            continue

        try:
            translated_text = translator.translate_text(original_text, source_lang, target_lang)
            new_block = f"{prefix}{translated_text}{suffix}"
            if add_comments_to_translated:
                new_block = "<!-- DO_NOT_TRANSLATE -->" + new_block
            content = content.replace(full, new_block)
            translated_count += 1
            print_status(idx, len(matches), original_text, "Translated")
        except Exception as e:
            print(f"\n❌ Block {idx}: translation error: {e}")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"\n✅ Translation ended.")
    print(f"📊 Statistics:")
    print(f"🔵 Successfully translated: {translated_count} lines")
    print(f"🟠 Skipped due to the lang: {skipped_lang_count} lines")
    print(f"🚫 Skipped due to DO_NOT_TRANSLATE mark: {skipped_do_not_translate_count} lines")
    print(f"📄 Translated resource saved in a file: {output_file}")