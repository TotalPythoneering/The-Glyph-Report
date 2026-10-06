'''
Create a python program to display all emojis, icons, and non-linguistic
glyphs into a categorized html document.
'''

import html
import unicodedata

# Define the Unicode ranges for emojis, non-linguistic symbols, and icons
UNICODE_CATEGORIES = {
    "Emoticons (Faces & Expressions)": range(0x1F600, 0x1F650),
    "Miscellaneous Symbols & Pictographs": range(0x1F300, 0x1F600),
    "Transport & Map Symbols": range(0x1F680, 0x1F700),
    "Supplemental Symbols & Pictographs": range(0x1F900, 0x1FA00),
    "Symbols & Pictographs Extended-A": range(0x1FA70, 0x1FAFF),
    "Dingbats": range(0x2700, 0x27C0),
    "Miscellaneous Symbols": range(0x2600, 0x2700),
    "Ornamental Dingbats": range(0x1F100, 0x1F1FF),
    "Arrows & Technical Symbols": range(0x2190, 0x2200),
}


def generate_emoji_html(output_filename="unicode_glyphs.html"):
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Unicode Emojis, Icons & Glyphs Library</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f4f7f6;
            color: #333;
            margin: 0;
            padding: 20px;
        }
        header {
            text-align: center;
            margin-bottom: 40px;
            padding: 20px;
            background: linear-gradient(135deg, #4f46e5, #06b6d4);
            color: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
        }
        h1 { margin: 0; font-size: 2.5rem; }
        p { margin: 10px 0 0; opacity: 0.9; }
        .category-section {
            background: white;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 12px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        .category-title {
            font-size: 1.5rem;
            color: #1e293b;
            border-bottom: 2px solid #e2e8f0;
            padding-bottom: 8px;
            margin-top: 0;
            margin-bottom: 20px;
        }
        .glyph-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
            gap: 15px;
        }
        .glyph-card {
            background-color: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 8px;
            padding: 15px;
            text-align: center;
            transition: all 0.2s ease-in-out;
        }
        .glyph-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
            border-color: #cbd5e1;
        }
        .char {
            font-size: 2.5rem;
            margin-bottom: 8px;
            display: block;
        }
        .code {
            font-family: monospace;
            font-size: 0.8rem;
            color: #64748b;
            display: block;
            margin-bottom: 4px;
        }
        .name {
            font-size: 0.7rem;
            color: #334155;
            text-transform: lowercase;
            word-wrap: break-word;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }
    </style>
</head>
<body>
    <header>
        <h1>Unicode Glyphs & Emojis Catalog</h1>
        <p>A comprehensive categorized view of non-linguistic characters generated via Python</p>
    </header>
    <main>
"""

    for category_name, code_range in UNICODE_CATEGORIES.items():
        cards_html = []

        for codepoint in code_range:
            char = chr(codepoint)
            try:
                # Get the official Unicode character name
                name = unicodedata.name(char)
            except ValueError:
                # Skip unassigned or control characters inside the ranges
                continue

            # Escape strings to prevent raw HTML breakages
            escaped_name = html.escape(name)
            hex_code = f"U+{codepoint:04X}"

            card = f"""
            <div class="glyph-card" title="{escaped_name}">
                <span class="char">{char}</span>
                <span class="code">{hex_code}</span>
                <span class="name">{escaped_name}</span>
            </div>"""
            cards_html.append(card)

        # Only append the section if valid glyphs were found within the range
        if cards_html:
            html_content += f"""
        <section class="category-section">
            <h2 class="category-title">{category_name} ({len(cards_html)} items)</h2>
            <div class="glyph-grid">
                {"".join(cards_html)}
            </div>
        </section>"""

    html_content += """
    </main>
</body>
</html>
"""

    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Successfully generated visual glyph library: '{output_filename}'")


if __name__ == "__main__":
    generate_emoji_html()
