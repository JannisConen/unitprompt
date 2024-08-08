import pytest
from unitprompt.matchers.uses.test_uses_html import assert_is_html
from unitprompt import assert_is_latex
from unitprompt.matchers.uses.test_uses_markdown import assert_is_markdown

def test_uses_html():
    html_string = '<div><p>Hello World</p></div>'
    assert_is_html(html_string)
    
def test_uses_html_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_is_html('Hello World')
        
def test_uses_markdown():
    markdown_string = '# Heading\n**Bold text**'
    assert_is_markdown(markdown_string)
    
def test_uses_markdown_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_is_markdown('Plain text without any Markdown')
        
def test_uses_latex():
    latex_string = r'\\begin{document}\nHello, World!\n\\end{document}'
    assert_is_latex(latex_string)
    
def test_uses_latex_fail():
    with pytest.raises(pytest.fail.Exception):
        assert_is_latex(r'Plain text without any LaTeX')
    
