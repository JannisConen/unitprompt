const MARKDOWN_PATTERNS = [
    "(\\*\\*?|__?)(.*?)\\1", // Matches bold (** or __) and italic (* or _) with proper escaping
    "`{3}[\\s\\S]*?`{3}", // Matches fenced code blocks with triple backticks
    "`[\\s\\S]*?`", // Matches inline code with single backticks
    "(^|\\s)[-+*]\\s", // Matches unordered lists that start with -, +, or *
    "^\\s*#{1,6}\\s", // Matches headers that start with # to ######
    "^>\\s+", // Matches blockquotes starting with >
    "^\\d+\\.\\s", // Matches ordered lists starting with 1. or 2. etc
    "!\\[.*?\\]\\(.*?\\)", // Matches images ![Alt text](URL)
    "\\[.*?\\]\\(.*?\\)", // Matches links [Link text](URL)
  ].join("|");

const markdownRegex = new RegExp(MARKDOWN_PATTERNS, "gm");

export function toUseMarkdown(received: string){

    const isMarkdown = markdownRegex.test(received);

    if (isMarkdown) {
        return {
            message: () => `expected ${received} not to have Markdown format`,
            pass: true,
        };
    } else {
        return {
            message: () => `expected ${received} to have Markdown format`,
            pass: false,
        };
    }
}