import pytest
from unitprompt import assert_fulfills, assert_is_html, assert_is_latex

@pytest.mark.asyncio
async def test_fulfills():
    await assert_fulfills("3", "what is 1 + 2?")
    pass

@pytest.mark.asyncio
async def test_format_solution():
    output = """
        Nutze die Integration durch Substitution, um das folgende Integral zu
berechnen:
\\[
\\int \\frac{x}{1+x^{2}} \\, dx
\\]

\\textbf{Schritt 1: Substitution}
\\begin{enumerate}
    \\item Setzen wir \\( u = 1 + x^2 \\).
\\end{enumerate}

\\textbf{Schritt 2: Ableitung von \\( u \\)}
\\[
\\frac{du}{dx} = 2x \\implies du = 2x \\, dx \\implies dx = \\frac{du}{2x}
\\]

\\textbf{Schritt 3: Substitution in das Integral}
Ersetzen wir \\(1 + x^2\\) durch \\(u\\) und \\(dx\\) durch \\(\\frac{du}{2x}\\),
erhalten wir:
\\[
\\int \\frac{x}{1+x^2} \\, dx = \\int \\frac{x}{u} \\cdot \\frac{du}{2x}
\\]

\\textbf{Schritt 4: Vereinfachung des Integrals}
Kürzen wir \\(x\\) im Zähler und Nenner:
\\[
= \\int \\frac{1}{2u} \\, du = \\frac{1}{2} \\int \\frac{1}{u} \\, du
\\]

\\textbf{Schritt 5: Integration}
Das Integral von \\(\\frac{1}{u}\\) ist \\(\\ln|u|\\):
\\[
= \\frac{1}{2} \\ln|u| + C
\\]

\\textbf{Schritt 6: Rücksubstitution}
Ersetzen wir \\(u\\) wieder durch \\(1 + x^2\\):
\\[
= \\frac{1}{2} \\ln|1 + x^2| + C
\\]

Da \\(1 + x^2\\) immer positiv ist, können wir die Betragsstriche weglassen:
\\[
= \\frac{1}{2} \\ln(1 + x^2) + C
\\]

\\textbf{Endergebnis}
\\[
\\int \\frac{x}{1+x^2} \\, dx = \\frac{1}{2} \\ln(1 + x^2) + C
\\]
    """
    # checks it is not html
    with pytest.raises(pytest.fail.Exception):
        assert_is_html(output)
        
    # checks it is latex
    assert_is_latex(output)
    
    with pytest.raises(pytest.fail.Exception):
        await assert_fulfills(output, "Important headlines are marked with \\textit")
        
    await assert_fulfills(output, "Important headlines are marked with \\textbf")
