import os

def get_prompt(prompt_filename: str) -> str:
    current_dir = os.path.dirname(__file__)  # Directory of the current script
    prompt_path = os.path.join(current_dir, "..", "prompts", prompt_filename + ".txt")
    prompt_path = os.path.abspath(prompt_path)  # Convert to absolute path

    with open(prompt_path, 'r') as f:
        return f.read()
