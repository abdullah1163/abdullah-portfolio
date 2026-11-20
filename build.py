"""Build index.html for GitHub Pages from page.html (the Claude artifact source).

The artifact host adds the document skeleton itself, so page.html has none.
GitHub Pages serves files as they are, so this wraps page.html in a full document.
Run: python build.py
"""
from pathlib import Path

HERE = Path(__file__).parent
src = (HERE / "page.html").read_text(encoding="utf-8")
head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]

out = (
    "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
    "<meta name=\"description\" content=\"Abdullah Nazir: GoHighLevel, Voice AI and CRM integration "
    "engineer. AI voice agents, CRM migrations, integrations and client portals.\">\n"
    + head
    + "\n<style>html,body{margin:0}:root{padding-top:env(safe-area-inset-top,0px);"
    "padding-bottom:env(safe-area-inset-bottom,0px)}img{max-width:100%}</style>\n</head>\n<body>\n"
    + body
    + "\n</body>\n</html>\n"
)
(HERE / "index.html").write_text(out, encoding="utf-8")
print(f"index.html written ({len(out):,} bytes)")
