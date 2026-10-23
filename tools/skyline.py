# Usage: python3 skyline.py OUT_DIR  (needs the SVGs produced by landmarks.py)
# Compose a wide, seamlessly tileable skyline from the landmark SVGs.
import re, sys, os
D = sys.argv[1]
def inner(name):
    s = open(os.path.join(D, name + ".svg")).read()
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    attrs = re.search(r'<svg ([^>]*)>', s).group(1)
    stroke = re.sub(r'xmlns="[^"]*"|viewBox="[^"]*"', '', attrs)
    body = s[s.index('>')+1:s.rindex('</svg>')]
    return vb, stroke, body
def place(name, x, w, ground=270):
    vb, stroke, body = inner(name)
    vx, vy, vw, vh = map(float, vb.split())
    h = w * vh / vw
    return f'<svg x="{x}" y="{ground-h:.1f}" width="{w}" height="{h:.1f}" viewBox="{vb}" {stroke} overflow="visible">{body}</svg>'
W = 1800
items = [
  place("hills", 0, 900, 272), place("hills", 900, 900, 272),
  place("cypress", 12, 20), place("colosseum", 40, 330), place("cypress", 388, 22), place("cypress", 414, 18),
  place("duomo", 450, 250), place("pine", 718, 110), place("houses", 846, 270),
  place("cypress", 1134, 22), place("pisa", 1172, 82), place("rialto", 1290, 300, 272), place("pine", 1606, 100), place("cypress", 1724, 22), place("cypress", 1752, 18),
]
ground = '<rect x="0" y="268" width="1800" height="32" fill="#E9D8B8"/><rect x="0" y="268" width="1800" height="4" fill="#D9C39C"/>'
svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} 300" preserveAspectRatio="xMinYMax meet">{"".join(items)}{ground}</svg>'
open(os.path.join(D, "skyline.svg"), "w").write(svg)
print(len(svg))
