import json
import re
import sys
from pathlib import Path
from thefuzz import process
import ollama

def load_prompt(filepath: Path) -> str:
    """Loads the system prompt from a file."""
    try:
        return filepath.read_text()
    except FileNotFoundError:
        print(f"Error: Prompt file not found at {filepath}")
        return ""

def load_glossary(filepath: Path) -> dict:
    """Loads the glossary from a JSON file."""
    try:
        with filepath.open('r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: Glossary file not found at {filepath}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}")
        return {}

def find_relevant_glossary_entries(text: str, glossary: dict, score_cutoff: int = 85) -> dict:
    """Finds relevant glossary entries in the text using fuzzy matching."""
    relevant_entries = {}
    # Modified regex to include apostrophes in words and convert to lower for matching
    words = set(re.findall(r"[\w']+", text.lower()))
    glossary_terms = list(glossary.keys())

    for word in words:
        # Find the best match for the word in the glossary keys
        best_match = process.extractOne(word, glossary_terms, score_cutoff=score_cutoff)
        
        if best_match:
            matched_term = best_match[0]
            if matched_term not in relevant_entries:
                relevant_entries[matched_term] = glossary[matched_term]
                
    return relevant_entries

def build_final_prompt(system_prompt_template: str, glossary_entries: dict, user_text: str) -> str:
    """Builds the final prompt to be sent to the Ollama API."""
    
    if not glossary_entries:
        glossary_section = "Nenhum termo do glossário encontrado neste texto."
    else:
        glossary_section = "\n".join([f"- {term}: {translation}" for term, translation in glossary_entries.items()])

    # Replace placeholders
    prompt = system_prompt_template.replace('{{glossario}}', glossary_section)
    prompt = prompt.replace('{{cole aqui o texto a ser traduzido}}', user_text)
    
    return prompt

def call_ollama_api(prompt: str, model: str = 'gemma3') -> str:
    """Calls the Ollama API with the given prompt and returns the translated text."""
    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    'role': 'user',
                    'content': prompt,
                }
            ],
            format='json' # Requesting structured output
        )
        translated_content = json.loads(response['message']['content'])
        return translated_content.get('translated_text', 'Translation not found in JSON response.')
    except Exception as e:
        print(f"Error calling Ollama API: {e}")
        return "Error during translation."

def main():
    """Main function to run the translator."""
    base_path = Path(__file__).parent
    system_prompt_file = base_path / "system_prompt.txt"
    glossary_file = base_path / "glossario.json"

    # 1. Load files
    system_prompt_template = load_prompt(system_prompt_file)
    glossary = load_glossary(glossary_file)

    if not system_prompt_template or not glossary:
        print("Exiting due to missing files.")
        return

    # 2. Get user input from command line arguments
    if len(sys.argv) < 2:
        print("Usage: uv run main.py \"<text to translate>\"")
        return
    user_text = sys.argv[1]

    # 3. Find relevant glossary entries
    relevant_entries = find_relevant_glossary_entries(user_text, glossary)

    # 4. Build the final prompt
    final_prompt = build_final_prompt(system_prompt_template, relevant_entries, user_text)

    # 5. Call Ollama API
    print("--- Calling Ollama API ---")
    translated_text = call_ollama_api(final_prompt)
    print("--- Translated Text ---")
    print(translated_text)
    print("-------------------------")


if __name__ == "__main__":
    main()

