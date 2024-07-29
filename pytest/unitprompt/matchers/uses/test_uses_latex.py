import re
import pytest

LATEX_PATTERNS = [
    r"\\documentclass",         # Matches document class
    r"\\begin\{[a-zA-Z]+\}",    # Matches \begin{env}
    r"\\end\{[a-zA-Z]+\}",      # Matches \end{env}
    r"\$\$[\s\S]*?\$\$",        # Matches display math with $$
    r"\$[^$]*?\$",              # Matches inline math with $
    r"\\[a-zA-Z]+"              # Matches LaTeX commands
]
latex_regex = re.compile("|".join(LATEX_PATTERNS), re.MULTILINE)

def assert_is_latex(received: str):
    is_latex = latex_regex.search(received) is not None

    if not is_latex:
        pytest.fail(f"Expected {received} to include LaTeX")
