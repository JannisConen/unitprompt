import re
import pytest

HTML_PATTERNS = [
    r"<(div|span|p|a|img|ul|ol|li|h[1-6]|header|footer|section|article|nav|aside|main|figure|figcaption|blockquote|code|pre|table|thead|tbody|tfoot|tr|td|th|button|input|form|label|textarea|select|option|iframe|video|audio|source|canvas|svg|path|g|circle|rect|line|polygon|polyline|text|tspan|use|symbol|defs|clipPath|mask|pattern|filter|linearGradient|radialGradient|stop|animate|animateTransform|animateMotion|animateColor|desc|title|metadata|foreignObject|switch|symbol|altGlyph|altGlyphDef|altGlyphItem|altGlyphSet|path|view|color-profile|cursor|font|glyph|glyphRef|hkern|vkern|font-face|font-face-format|font-face-name|font-face-src|font-face-uri|missing-glyph|linearGradient|radialGradient|stop|a|altGlyph|animate|circle|clipPath|defs|desc|ellipse|filter|g|image|line|linearGradient|marker|mask|metadata|path|pattern|polygon|polyline|radialGradient|rect|stop|svg|switch|symbol|text|textPath|title|use|view)[\s/>]",  # Matches HTML tags
    r"class\s*=\s*['\"]",  # Matches class attribute
    r"id\s*=\s*['\"]",     # Matches id attribute
    r"style\s*=\s*['\"]"   # Matches style attribute
]
html_regex = re.compile("|".join(HTML_PATTERNS), re.MULTILINE)

def assert_is_html(received: str):
    is_html = html_regex.search(received) is not None

    if not is_html:
        pytest.fail(f"Expected {received} to include HTML")
