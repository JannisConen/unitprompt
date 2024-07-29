import re
import pytest

MARKDOWN_PATTERNS = [
    r"(\*\*?|__?)(.*?)\1",        # Matches bold (** or __) and italic (* or _) with proper escaping
    r"`{3}[\s\S]*?`{3}",          # Matches fenced code blocks with triple backticks
    r"`[\s\S]*?`",                # Matches inline code with single backticks
    r"(^|\s)[-+*]\s",             # Matches unordered lists that start with -, +, or *
    r"^\s*#{1,6}\s",              # Matches headers that start with # to ######
    r"^>\s+",                     # Matches blockquotes starting with >
    r"^\d+\.\s",                  # Matches ordered lists starting with 1. or 2. etc
    r"!\[.*?\]\(.*?\)",           # Matches images ![Alt text](URL)
    r"\[.*?\]\(.*?\)"             # Matches links [Link text](URL)
]
markdown_regex = re.compile("|".join(MARKDOWN_PATTERNS), re.MULTILINE)

def assert_is_markdown(received: str):
    is_markdown = markdown_regex.search(received) is not None

    if not is_markdown:
        pytest.fail(f"Expected {received} to include Markdown")