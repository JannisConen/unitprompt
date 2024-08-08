import pytest
from unitprompt import assert_fulfills, assert_is_html, assert_is_latex

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

given_style = """
    Nutze die Integration durch Substitution, um das folgende Integral zu berechnen:
\\[
\\int_{1}^{2} \\frac{x}{\\sqrt{4 x^{2}+1}} d x=\\int_{1}^{2} x \\cdot\\left(4 x^{2}+1\\right)^{-\\frac{1}{2}} d x
\\]

Schritt 1: Geht Substitution? \\( g^{\\prime}(x)=8 x \\approx x \\)

Schritt 2: \\( \\quad u=4 x^{2}+1 \\)

Schritt 3: \\( \\quad \\frac{d u}{d x}=8 x \\leftrightarrow d u=8 x \\cdot d x \\leftrightarrow d x=\\frac{d u}{8 x} \\)

Schritt 4: Substitution:
\\[
\\int_{1}^{2} x \\cdot\\left(4 x^{2}+1\\right)^{-\\frac{1}{2}} d x=\\int_{u(1)}^{u(2)} x \\cdot(u)^{-\\frac{1}{2}} \\frac{d u}{8 x}
\\]

Schritt 5: Kürzen und Aufleiten:
\\[
=\\int_{u(1)}^{u(2)} \\frac{1}{8} u^{-\\frac{1}{2}} d u=\\frac{1}{8}\\left[2 u^{\\frac{1}{2}}\\right]_{u(1)}^{u(2)}
\\]

Schritt 6: Resubstitution:
\\[
=\\frac{1}{4}\\left[\\left(4 x^{2}+1\\right)^{\\frac{1}{2}}\\right]_{1}^{2}
\\]

Schritt 7: Ausrechnen:
\\[
\\begin{array}{l}
=\\frac{1}{4}\\left[\\left(4 \\cdot 2^{2}+1\\right)^{\\frac{1}{2}}-\\left(4 \\cdot 1^{2}+1\\right)^{\\frac{1}{2}}\\right] \\\\
=\\frac{1}{4} \\cdot\\left(17^{\\frac{1}{2}}-5^{\\frac{1}{2}}\\right) \\\\
\\approx 0,47
\\end{array}
\\]
"""

@pytest.mark.asyncio
async def test_fulfills():
    await assert_fulfills("3", "what is 1 + 2?")
    pass

@pytest.mark.asyncio
async def test_format_solution():

    # checks it is not html
    with pytest.raises(pytest.fail.Exception):
        assert_is_html(output)
        
    # checks it is latex
    assert_is_latex(output)
    
    with pytest.raises(pytest.fail.Exception):
        await assert_fulfills(output, "Important headlines are marked with \\textit")
        
    await assert_fulfills(output, "Important headlines are marked with \\textbf")
    
@pytest.mark.asyncio
async def test_solution_in_line_with_given_task():
    await assert_fulfills(output, "The solution uses the same solving style as this one: " + given_style)

@pytest.mark.asyncio
async def test_solution_in_line_with_given_task_fail():
    output = """
    \\[
    \\begin{array}{l}
    =\\frac{1}{4}\\left[\\left(4 \\cdot 2^{2}+1\\right)^{\\frac{1}{2}}-\\left(4 \\cdot 1^{2}+1\\right)^{\\frac{1}{2}}\\right] \\\\
    =\\frac{1}{4} \\cdot\\left(17^{\\frac{1}{2}}-5^{\\frac{1}{2}}\\right) \\\\
    \\approx 0,47
    \\end{array}
    \\]
    """
    
    with pytest.raises(pytest.fail.Exception):
        await assert_fulfills(output, "The solution uses the same solving style as this one: " + given_style)