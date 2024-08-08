# unitprompt - pytest

`unitprompt` is a pytest extension that provides custom matchers for unit testing LLM processes. This library helps ensure that your large language model (LLM) outputs are validated correctly in your tests.

## Installation

pip install unitprompt

## Usage
```python
import pytest
from unitprompt import assert_is_latex, assert_conciseness
# mark as async because assert_conciseness requires an LLM call
@pytest.mark.asyncio
async def test_conciseness_fail():
    
    long_text = """
    First of all, you need to learn about the concept of sums. A sum is the result of adding two numbers together.
    This can be done in a variety of ways. There is the traditional method of writing the numbers one on top of the other and adding them together.

    In this instance you can take the first number, 3, and write it down. Then you can take the second number, 4, and write it down below the first number. You can then add the two numbers together to get the sum of 7.
    """
    
    with pytest.raises(pytest.fail.Exception):
        await assert_conciseness(long_text)

def test_uses_latex():
    latex_string = r'\\begin{document}\nHello, World!\n\\end{document}'
    assert_is_latex(latex_string)
    
def test_uses_latex_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_is_latex(r'Plain text without any LaTeX')
```