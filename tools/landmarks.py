# Usage: python3 landmarks.py OUT_DIR  (then python3 skyline.py OUT_DIR)
# Generates flat, outlined Italian landmark SVGs in the Open Peeps line style.
import os, math, sys
OUT = sys.argv[1]
INK = "#1A1A2E"; SW = 2.6
def svg(w, h, body, pad=4):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{-pad} {-pad} {w+2*pad} {h+2*pad}" stroke="{INK}" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="round">{body}</svg>'
def arch(x, y, w, h, fill):
    r = w/2
    return f'<path d="M{x:.1f} {y+h:.1f}V{y+r:.1f}A{r:.1f} {r:.1f} 0 0 1 {x+w:.1f} {y+r:.1f}V{y+h:.1f}Z" fill="{fill}"/>'

def colosseum():
    W, H = 360, 175
    b = []
    # body silhouette: ruined right side
    b.append(f'<path d="M0 {H}V22Q0 8 14 8H235L238 22H262L266 46H300L303 62H330L334 92H360V{H}Z" fill="#EBC48E"/>')
    tiers = [(124, H, 30), (78, 124, 30), (36, 78, 30)]
    for (top, bot, step) in tiers:
        right_limit = {124:360, 78:334, 36:300}[top]
        b.append(f'<line x1="0" y1="{top}" x2="{ {124:360,78:334,36:262}[top] }" y2="{top}" stroke-width="2"/>')
        for i in range(12):
            x = 6 + i*step
            if x + 18 > right_limit: break
            b.append(arch(x, top+7, 18, bot-top-10, "#B9824A"))
    # attic windows
    for i in range(7):
        x = 14 + i*30
        b.append(f'<rect x="{x}" y="16" width="10" height="12" fill="#C9945A" stroke-width="1.8"/>')
    # shading inner wall
    b.append(f'<path d="M300 62H330L334 92H360V120H300Z" fill="#D9A867" stroke="none" opacity=".55"/>')
    return svg(W, H, "".join(b))

def pisa():
    W, H = 80, 230
    g = []
    g.append(f'<rect x="8" y="36" width="64" height="{H-36}" rx="3" fill="#F7F1E6"/>')
    floors = 7
    fh = (H-36-6)/floors
    for f in range(floors):
        y = 36 + f*fh
        g.append(f'<line x1="8" y1="{y:.1f}" x2="72" y2="{y:.1f}" stroke-width="2"/>')
        for i in range(5):
            g.append(arch(12 + i*12, y+5, 8, fh-8, "#D8CDB8").replace(f'stroke-width', 'stroke-width'))
    g.append(f'<rect x="18" y="10" width="44" height="28" rx="3" fill="#F7F1E6"/>')
    for i in range(3):
        g.append(arch(22 + i*13, 15, 9, 20, "#D8CDB8"))
    g.append('<path d="M16 12Q40 -4 64 12Z" fill="#E7DCC8"/>')
    return svg(W, H, f'<g transform="rotate(5 40 {H})">{"".join(g)}</g>', pad=22)

def duomo():
    W, H = 300, 230
    b = []
    # campanile
    b.append('<rect x="232" y="28" width="38" height="202" fill="#F7F1E6"/>')
    for i, y in enumerate(range(28, 230, 34)):
        b.append(f'<line x1="232" y1="{y}" x2="270" y2="{y}" stroke-width="2"/>')
        b.append(f'<rect x="240" y="{y+7}" width="22" height="20" rx="2" fill="{"#E7A9A0" if i%2 else "#4E8A63"}" stroke-width="1.8"/>')
    b.append('<rect x="228" y="20" width="46" height="10" fill="#F7F1E6"/>')
    # nave
    b.append('<rect x="0" y="158" width="215" height="72" fill="#F7F1E6"/>')
    for i in range(9):
        x = 6 + i*23
        b.append(f'<rect x="{x}" y="166" width="14" height="56" rx="2" fill="{["#4E8A63","#E7A9A0","#4E8A63"][i%3]}" stroke-width="1.8"/>')
    b.append('<path d="M0 158L20 142H195L215 158Z" fill="#D2693C"/>')
    # drum
    b.append('<rect x="52" y="112" width="120" height="34" fill="#F7F1E6"/>')
    for i in range(5):
        b.append(f'<circle cx="{66+i*24}" cy="129" r="7" fill="#4E8A63" stroke-width="1.8"/>')
    b.append('<rect x="48" y="104" width="128" height="10" fill="#F7F1E6"/>')
    # dome
    b.append('<path d="M52 104C52 52 82 26 112 22C142 26 172 52 172 104Z" fill="#D2693C"/>')
    for x0, cx in [(72, 92), (92, 102), (112, 112), (132, 122), (152, 132)]:
        b.append(f'<path d="M{x0} 104Q{cx} 50 112 24" fill="none" stroke="#F7F1E6" stroke-width="3"/>')
    b.append('<path d="M52 104C52 52 82 26 112 22C142 26 172 52 172 104Z" fill="none"/>')
    # lantern
    b.append('<rect x="104" y="8" width="16" height="16" fill="#F7F1E6"/><path d="M104 8L112 -6L120 8Z" fill="#F7F1E6"/>')
    return svg(W, H, "".join(b), pad=10)

def rialto():
    W, H = 330, 130
    b = []
    b.append('<rect x="-4" y="100" width="338" height="34" fill="#6FB7D9" stroke="none"/>')
    for x in range(10, 320, 46):
        b.append(f'<path d="M{x} 114q8 -6 16 0t16 0" fill="none" stroke="#FFFFFF" stroke-width="2.2"/>')
    # bridge body
    b.append('<path d="M0 100L0 84Q165 18 330 84V100H262Q165 34 68 100Z" fill="#F3E2C3"/>')
    # portico
    b.append('<path d="M128 52L165 30L202 52V66H128Z" fill="#F3E2C3"/>')
    b.append(arch(152, 44, 26, 22, "#C9A97A"))
    b.append('<path d="M150 34L165 20L180 34Z" fill="#D2693C"/>')
    for x in (100, 214):
        for i in range(3):
            b.append(arch(x + i*10, 62 if x == 100 else 62, 7, 10, "#C9A97A"))
    # gondola
    b.append('<path d="M40 118Q90 130 140 116L146 108Q136 114 128 115Q90 122 46 112L36 104Z" fill="#1A1A2E"/>')
    b.append('<path d="M104 114L104 84M100 86h8" fill="none"/><circle cx="104" cy="80" r="5" fill="#E8B794"/><path d="M98 76h12" stroke-width="3"/>')
    b.append('<line x1="118" y1="88" x2="96" y2="124" stroke-width="2.2"/>')
    return svg(W, H, "".join(b))

def houses():
    W, H = 270, 150
    cols = ["#F2B33D", "#E46F4B", "#F4A3A8", "#7FB3D5", "#F6E3B4", "#9CC57A"]
    hs = [118, 146, 104, 132, 112, 140]
    ws = [44, 46, 42, 48, 42, 48]
    b, x = [], 0
    for i, (c, h, w) in enumerate(zip(cols, hs, ws)):
        y = H - h
        b.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{c}"/>')
        b.append(f'<rect x="{x-2}" y="{y-6}" width="{w+4}" height="7" fill="#D2693C"/>')
        rows = int((h-30)//28)
        for r in range(rows):
            for k in range(2):
                wx = x + 8 + k*(w-24)//1 if False else x + 7 + k*(w/2)
                wy = y + 12 + r*28
                b.append(f'<rect x="{wx:.1f}" y="{wy}" width="{w/2-14:.1f}" height="14" fill="#2D6A3E" stroke-width="1.8"/>')
                b.append(f'<line x1="{wx + (w/2-14)/2:.1f}" y1="{wy}" x2="{wx + (w/2-14)/2:.1f}" y2="{wy+14}" stroke-width="1.4"/>')
        b.append(f'<rect x="{x + w/2 - 7:.1f}" y="{H-22}" width="14" height="22" rx="7" fill="#7A4B2A" stroke-width="1.8"/>')
        x += w
    return svg(W, H, "".join(b), pad=8)

def cypress():
    return svg(26, 100, '<path d="M13 100V90M13 0C24 22 26 56 21 90H5C0 56 2 22 13 0Z" fill="#2D6A3E"/>')

def pine():
    return svg(120, 110, '<path d="M60 110V58M60 70L44 52M60 64L80 50" fill="none" stroke-width="5" stroke="#7A4B2A"/><path d="M60 110V58" fill="none"/><path d="M6 46C0 30 22 14 44 18C52 4 84 4 92 16C112 12 124 30 112 44C100 56 18 58 6 46Z" fill="#3B7A47"/>')

def hills():
    return svg(900, 120, '<path d="M0 120V70Q120 10 260 52T520 40T760 50T900 34V120Z" fill="#B9D59A" stroke="none"/><path d="M0 120V92Q160 52 330 84T640 74T900 70V120Z" fill="#9CC57A" stroke="none"/>', pad=0)

os.makedirs(OUT, exist_ok=True)
for name, fn in [("colosseum", colosseum), ("pisa", pisa), ("duomo", duomo), ("rialto", rialto), ("houses", houses), ("cypress", cypress), ("pine", pine), ("hills", hills)]:
    open(os.path.join(OUT, f"{name}.svg"), "w").write(fn())
print("ok")
