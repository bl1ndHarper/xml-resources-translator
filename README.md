Translator Project
==================

Automated translator for Android resource files (`strings.xml`, `arrays.xml`) with full support for:

*   multiple translation APIs (DeepL, Google, Stub, others)
    
*   allowed languages check (string-level language detection)
    
*   automatic insertion of comments for skipped and translated lines
    
*   selecting language-specific configuration files
    
*   detailed statistics after processing
    
*   full control over the translation flow!
    

* * *

Installation
---------------

1.  Clone or download the project.
    
2.  Install dependencies:
`pip install -r requirements.txt`

3.  Create a `.env` file in the project root to store your secret keys:
- `DEEPL_API_KEY=your_deepl_api_key_here`
- `GOOGLE_APPLICATION_CREDENTIALS` (value is the path to your local Google API credential file)

4.  Configure your translation settings inside the `configs/` folder, or use the default `config.json`.
    

* * *

Project Structure
--------------------

```
translator/
├── __main__.py                 # Main translation script
├── translator_factory.py
├── config.json                 # Default configuration
├── configs/                    # Other language-specific configurations
│   ├── config-en.json
│   ├── config-ru.json
│   └── config-cn.json
├── core/                       
│   └── translator_engine.py    # Core program logics
├── io/                         # input/output xml files
│   ├── input.xml
│   └── output.xml              # Will be generated
├── translators/                # Translator implementations
│   ├── base.py
│   ├── deepl_translator.py
│   ├── google_translator.py
│   └── stub_translator.py
├── ui/                         
│   └── interaction.py          # Runtime user inputs handling
├── utils/
│   └── progress.py             # Console progress indicator
├── .env                        # API key storage
├── google-creadentials.json    # Generated in your console.cloud.google API credentials
├── requirements.txt            # Required libraries
└── README.md                   # This documentation
```
* * *

Usage
--------
1.  Put your resource .xml file according to the specified `input_file` path in the configuration.

2.  Run the .bat or .sh depending on your system.

3.  During execution, the program will ask:
    
    *   To select a **configuration file** (or use the default).
        
    *   To select a **resource type**: `<string>` or `<item>`.

    *   To select a **translator** (be careful as some of them might be more or less capable for different situations).
        
    *   Whether to:
        
        *   **Add comments** to skipped lines.
            
        *   **Add comments** to successfully translated lines.
            
4.  The translated file will be saved according to the specified `output_file` path in the configuration.
    

* * *

Features Explained
---------------------
| Feature                     | Description                                                                          |
|-----------------------------|--------------------------------------------------------------------------------------|
| Commenting skipped lines    | Adds `<!-- TODO: [NOT_TRANSLATED: detected_lang = XX] -->` to easily find them later |
| Commenting translated lines | Adds `<!-- DO_NOT_TRANSLATE -->` to protect from reprocessing                        |
| Multi-configuration support | Easily switch languages with `configs/config-*.json`                                 |
| DO\_NOT\_TRANSLATE handling | Lines marked with this comment are never changed                                     |
| Final statistics report     | Number of translated, skipped (language mismatch), and skipped (manual mark) lines   |

* * *

Configuration File Format
----------------------------

Example `configs/config-en.json`:
```json
{
  "source_lang": "EN",
  "target_lang": "UK",
  "input_file": "io/input.xml",
  "output_file": "io/output.xml",
  "allowed_lang_codes": ["en", "de", "es", "it", "ro", "nl", "pt", "hu", "da", "fr", "pl", "no", "ca", "sv", "fi", "hr", "tl", "af"]
}
```

*   `source_lang` — source language code
    
*   `target_lang` — target translation language code
    
*   `allowed_lang_codes` — array of accepted languages for processing (empty array disables checking). - These are used to filter inappropriate for your `source_lang` strings which should lower the count of API calls to prevent quota overuse.
    
*   `input_file` — path to the input resource file
    
*   `output_file` — path to save the translated file
    

* * *

Extra Details
----------------

*   If `allowed_lang_codes` is an empty array `[]`, **all lines are translated** regardless of detected language.
    
*   Translated lines can be safely excluded from future sessions by inserting `<!-- DO_NOT_TRANSLATE -->` comment at the start of the line.
    
*   Supports multi-line text blocks (`re.DOTALL` handling).
    

* * *

Example Console Output
-------------------------

```lua
🛠️ Available configurations:
1. config-cn-uk.json
2. config-en-uk.json
3. config-ru-uk.json
Select a config (or press Enter for default): 1
Using config: config-cn-uk.json
🧠 Available translators:
1. DeepL
2. Google Cloud Translate
3. Stub (fake)
Select a translator (1 or 2): 2
🧩 Available resource types to work with:
1. strings (<string />)
2. arrays (<[type]-array><item /><[type]-array>)
Select a type (1 or 2): 1
💬 Add comments to untranslated lines? (y/n or h for help)
> y
💬 Add comments for translated lines? (y/n or h for help)
> y
📂 File detected, 257 lines found.
🚀 Translation started...
...
✅ Translation completed.
📊 Statistics:
🔵 Translated lines: 185
🟠 Skipped due to language mismatch: 12
🚫 Skipped due to DO_NOT_TRANSLATE mark: 5
📄 Output saved as: io/output.xml

```

* * *

📜 License
----------

MIT License — free for any use.

* * *
