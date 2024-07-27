const HTML_PATTERNS = [
    "<(div|span|p|a|img|ul|ol|li|h[1-6]|header|footer|section|article|nav|aside|main|figure|figcaption|blockquote|code|pre|table|thead|tbody|tfoot|tr|td|th|button|input|form|label|textarea|select|option|iframe|video|audio|source|canvas|svg|path|g|circle|rect|line|polygon|polyline|text|tspan|use|symbol|defs|clipPath|mask|pattern|filter|linearGradient|radialGradient|stop|animate|animateTransform|animateMotion|animateColor|desc|title|metadata|foreignObject|switch|symbol|altGlyph|altGlyphDef|altGlyphItem|altGlyphSet|path|view|color-profile|cursor|font|glyph|glyphRef|hkern|vkern|font-face|font-face-format|font-face-name|font-face-src|font-face-uri|missing-glyph|linearGradient|radialGradient|stop|a|altGlyph|animate|circle|clipPath|defs|desc|ellipse|filter|g|image|line|linearGradient|marker|mask|metadata|path|pattern|polygon|polyline|radialGradient|rect|stop|svg|switch|symbol|text|textPath|title|use|view)[\\s/>]", // Matches HTML tags
    "class\\s*=\\s*['\"]", // Matches class attribute
    "id\\s*=\\s*['\"]", // Matches id attribute
    "style\\s*=\\s*['\"]", // Matches style attribute
].join("|");

const htmlRegex = new RegExp(HTML_PATTERNS, "gm");

export function toUseHtml(received: string){
    const isHtml = htmlRegex.test(received);

    if (isHtml) {
        return {
            message: () => `expected ${received} not to have HTML format`,
            pass: true,
        };
    } else {
        return {
            message: () => `expected ${received} to have HTML format`,
            pass: false,
        };
    }
}