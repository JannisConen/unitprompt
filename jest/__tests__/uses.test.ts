import { unitPromptMatchers } from '../src/unitPromptMatchers';

expect.extend(unitPromptMatchers);

describe('Custom Format Matchers', () => {

    test('should detect Markdown format correctly', () => {
        expect('# Heading\n**Bold text**').toUseMarkdown();
        expect('Plain text without any Markdown').not.toUseMarkdown();
    });

    test('should detect LaTeX format correctly', () => {
        expect('\\begin{document}\nHello, World!\n\\end{document}').toUseLatex();
        expect('Plain text without any LaTeX').not.toUseLatex();
    });

    test('should detect HTML format correctly', () => {
        expect('<div><p>Hello World</p></div>').toUseHtml();
        expect('Hello World').not.toUseHtml();
    });
});