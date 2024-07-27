import { customMatchers } from '../src/customMatchers';

expect.extend(customMatchers);

describe('Custom Format Matchers', () => {
    test('should validate XML strings correctly', () => {
        expect('<root><child /></root>').toBeParsableXml();
        expect('<root><child></root>').not.toBeParsableXml(); // malformed XML
    });

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