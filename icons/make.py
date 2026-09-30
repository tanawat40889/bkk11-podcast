# Renders app icons via headless Chrome. Run: python3 icons/make.py
import subprocess, os, pathlib
here = pathlib.Path(__file__).parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def svg(rounded=True, k=1.0):
    bg = f'<rect width="512" height="512" rx="{112 if rounded else 0}" fill="url(#bg)"/>'
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>
 <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9b7bff"/><stop offset="1" stop-color="#3a1f8f"/></linearGradient>
 <linearGradient id="or" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#ffcf7a"/><stop offset="1" stop-color="#ff7438"/></linearGradient>
 <radialGradient id="gl" cx=".5" cy=".3" r=".6"><stop offset="0" stop-color="#fff" stop-opacity=".35"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></radialGradient>
</defs>
{bg}
<rect width="512" height="512" rx="{112 if rounded else 0}" fill="url(#gl)"/>
<g transform="translate(256 256) scale({k}) translate(-256 -256)">
 <g fill="none" stroke-linecap="round">
  <path d="M136 290 V250 a120 120 0 0 1 240 0 V290" stroke="#1e0f52" stroke-width="34" transform="translate(12 12)"/>
  <path d="M136 290 V250 a120 120 0 0 1 240 0 V290" stroke="#fff" stroke-width="34"/>
 </g>
 <rect x="104" y="262" width="76" height="112" rx="30" fill="#1e0f52" transform="translate(12 12)"/>
 <rect x="332" y="262" width="76" height="112" rx="30" fill="#1e0f52" transform="translate(12 12)"/>
 <rect x="104" y="262" width="76" height="112" rx="30" fill="#ffd166"/>
 <rect x="332" y="262" width="76" height="112" rx="30" fill="#ffd166"/>
 <text x="256" y="300" text-anchor="middle" font-family="Kanit" font-weight="800" font-size="120" fill="#fff">?</text>
 <g transform="rotate(-4 256 405) translate(0 20)">
  <rect x="62" y="356" width="400" height="104" fill="#1e0f52" transform="translate(12 12)"/>
  <rect x="62" y="356" width="400" height="104" fill="url(#or)"/>
  <text x="262" y="440" text-anchor="middle" font-family="Kanit" font-weight="800" font-style="italic" font-size="92" fill="#1e0f52" letter-spacing="2">BKK11</text>
  <text x="257" y="435" text-anchor="middle" font-family="Kanit" font-weight="800" font-style="italic" font-size="92" fill="#fff" letter-spacing="2">BKK11</text>
 </g>
</g>
</svg>'''

def render(name, size, **kw):
    html = here / "_tmp.html"
    html.write_text(f'''<!doctype html><html><head><link href="https://fonts.googleapis.com/css2?family=Kanit:ital,wght@1,800&display=block" rel="stylesheet">
<style>html,body{{margin:0;background:transparent}}svg{{display:block;width:{size}px;height:{size}px}}</style></head><body>{svg(**kw)}</body></html>''')
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--default-background-color=00000000",
        f"--window-size={size},{size}", "--virtual-time-budget=4000", f"--screenshot={here/name}", str(html)], check=True, capture_output=True)
    html.unlink()


render("icon-512.png", 512)
render("icon-192.png", 192)
render("apple-touch-icon.png", 180, rounded=False)
render("maskable-512.png", 512, rounded=False, k=0.8)
render("favicon-64.png", 64)
print("done")
