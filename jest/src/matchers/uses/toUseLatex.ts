const LATEX_PATTERNS = [
    "\\\\documentclass", // Matches document class
    "\\\\begin\\{[a-zA-Z]+\\}", // Matches \begin{env}
    "\\\\end\\{[a-zA-Z]+\\}", // Matches \end{env}
    "\\$\\$[\\s\\S]*?\\$\\$", // Matches display math with $$
    "\\$[^$]*?\\$", // Matches inline math with $
    "\\\\[a-zA-Z]+", // Matches LaTeX commands
].join("|");

const latexRegex = new RegExp(LATEX_PATTERNS, "gm");

export function toUseLatex(received: string){
    const isLatex = latexRegex.test(received);

    if (isLatex) {
        return {
            message: () => `expected ${received} not to have LaTeX format`,
            pass: true,
        };
    } else {
        return {
            message: () => `expected ${received} to have LaTeX format`,
            pass: false,
        };
    }
}