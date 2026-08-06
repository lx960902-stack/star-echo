"""
Pixel-art block buttons generator for Star Resonance (星穹回响)
Generates 32x32 base pixel art, scaled 4x to 128x128 PNG with transparent background.
"""
import os
from PIL import Image

OUT_DIR = os.path.join(os.path.dirname(__file__), "buttons")
os.makedirs(OUT_DIR, exist_ok=True)

# ---- Color palette ----
C = {
    'transparent': (0, 0, 0, 0),
    'white':       (240, 244, 252, 255),
    'black':       (20, 22, 38, 255),
    'shadow':      (12, 14, 28, 255),
    'outline':     (40, 44, 68, 255),
    # Red theme
    'red_d':       (120, 30, 36, 255),
    'red_m':       (200, 50, 54, 255),
    'red_l':       (240, 90, 88, 255),
    'red_h':       (255, 140, 130, 255),
    # Blue theme
    'blue_d':      (30, 64, 120, 255),
    'blue_m':      (50, 110, 200, 255),
    'blue_l':      (80, 160, 255, 255),
    'blue_h':      (130, 200, 255, 255),
    # Green theme
    'green_d':     (30, 80, 48, 255),
    'green_m':     (50, 140, 80, 255),
    'green_l':     (80, 210, 130, 255),
    'green_h':     (130, 240, 170, 255),
    # Gold theme
    'gold_d':      (120, 88, 20, 255),
    'gold_m':      (200, 160, 40, 255),
    'gold_l':      (240, 210, 80, 255),
    'gold_h':      (255, 240, 140, 255),
    # Purple theme
    'purple_d':    (70, 40, 100, 255),
    'purple_m':    (130, 80, 180, 255),
    'purple_l':    (170, 120, 230, 255),
    'purple_h':    (210, 170, 255, 255),
    # Orange theme
    'orange_d':    (110, 60, 20, 255),
    'orange_m':    (200, 110, 30, 255),
    'orange_l':    (250, 150, 50, 255),
    'orange_h':    (255, 195, 100, 255),
    # Gray theme
    'gray_d':      (60, 64, 80, 255),
    'gray_m':      (100, 105, 125, 255),
    'gray_l':      (150, 155, 175, 255),
    'gray_h':      (200, 205, 220, 255),
    # Skin/hair for icons if needed
    'silver':      (180, 185, 200, 255),
}

def make_canvas():
    """32x32 RGBA transparent canvas."""
    return Image.new('RGBA', (32, 32), C['transparent'])

def px(img, x, y, color):
    """Set a single pixel, bounds-safe."""
    if 0 <= x < 32 and 0 <= y < 32:
        img.putpixel((x, y), color)

def rect(img, x0, y0, x1, y1, color):
    """Fill rectangle inclusive."""
    for y in range(y0, y1 + 1):
        for x in range(x0, x1 + 1):
            px(img, x, y, color)

def hline(img, x0, x1, y, color):
    for x in range(x0, x1 + 1):
        px(img, x, y, color)

def vline(img, x, y0, y1, color):
    for y in range(y0, y1 + 1):
        px(img, x, y, color)

def draw_button_bg(img, d, m, l):
    """
    Draw a beveled button background.
    d=dark(border/shadow), m=mid(base), l=light(highlight)
    Layout: 2px border, 28x28 inner area, beveled corners.
    """
    # Outer border (dark)
    rect(img, 2, 2, 29, 29, d)
    # Inner fill (mid)
    rect(img, 3, 3, 28, 28, m)
    # Top-left highlight (light) - 2px bevel
    hline(img, 3, 28, 3, l)
    hline(img, 3, 28, 4, l)
    vline(img, 3, 3, 28, l)
    vline(img, 4, 3, 28, l)
    # Bottom-right shadow (dark, darker than border)
    hline(img, 3, 28, 28, C['shadow'])
    hline(img, 3, 28, 27, d)
    vline(img, 28, 3, 28, d)
    vline(img, 27, 3, 28, d)
    # Corner pixels for rounded feel
    px(img, 2, 2, C['transparent'])
    px(img, 29, 2, C['transparent'])
    px(img, 2, 29, C['transparent'])
    px(img, 29, 29, C['transparent'])
    px(img, 3, 3, l)
    px(img, 28, 28, d)

def save_button(img, name, scale=4):
    """Scale up and save. Nearest-neighbor for crisp pixels."""
    sized = img.resize((32 * scale, 32 * scale), Image.NEAREST)
    path = os.path.join(OUT_DIR, f"btn_{name}.png")
    sized.save(path)
    print(f"  Saved: {path} ({32*scale}x{32*scale})")
    return path


# ============================================================
# Button icon drawing functions
# ============================================================

def draw_attack(img):
    """Sword icon - red theme."""
    draw_button_bg(img, C['red_d'], C['red_m'], C['red_l'])
    hl = C['red_h']
    # Sword blade (diagonal from bottom-left to top-right)
    blade = C['silver']
    blade_h = C['white']
    # Blade pixels
    for i in range(8):
        px(img, 10+i, 22-i, blade)
        px(img, 11+i, 22-i, blade_h)  # highlight edge
        px(img, 10+i, 23-i, C['outline'])
    # Blade tip
    px(img, 19, 13, blade_h)
    px(img, 18, 14, blade)
    # Crossguard
    hline(img, 7, 13, 22, C['gold_d'])
    hline(img, 7, 13, 23, C['gold_m'])
    hline(img, 7, 13, 24, C['gold_d'])
    px(img, 7, 22, C['gold_l'])
    px(img, 13, 22, C['gold_l'])
    # Handle
    vline(img, 6, 22, 27, C['gold_d'])
    vline(img, 7, 22, 27, C['gold_m'])
    vline(img, 8, 22, 27, C['gold_d'])
    # Pommel
    rect(img, 5, 26, 9, 28, C['gold_m'])
    px(img, 6, 27, C['gold_l'])

def draw_defend(img):
    """Shield icon - blue theme."""
    draw_button_bg(img, C['blue_d'], C['blue_m'], C['blue_l'])
    # Shield outline
    s_o = C['outline']
    s_m = C['blue_h']
    s_l = C['white']
    s_d = C['blue_l']
    # Shield shape (pointed bottom)
    # Top edge
    hline(img, 9, 22, 7, s_o)
    hline(img, 9, 22, 8, s_m)
    # Sides going down to point
    for i in range(8):
        px(img, 9, 8+i, s_o)
        px(img, 10, 8+i, s_m)
        px(img, 22, 8+i, s_o)
        px(img, 21, 8+i, s_m)
    # Bottom point
    for i in range(4):
        px(img, 9+i, 16+i, s_o)
        px(img, 22-i, 16+i, s_o)
        px(img, 10+i, 16+i, s_m)
        px(img, 21-i, 16+i, s_m)
    px(img, 15, 20, s_o)
    px(img, 16, 20, s_o)
    px(img, 16, 21, s_o)
    # Shield inner highlight
    hline(img, 11, 20, 9, s_l)
    hline(img, 11, 20, 10, s_d)
    px(img, 11, 11, s_l)
    # Center boss
    rect(img, 14, 12, 17, 14, C['gold_m'])
    px(img, 15, 13, C['gold_l'])

def draw_item(img):
    """Backpack/bag icon - green theme."""
    draw_button_bg(img, C['green_d'], C['green_m'], C['green_l'])
    b = C['outline']
    f = C['green_d']
    h = C['green_h']
    # Bag body
    # Top flap
    hline(img, 8, 23, 8, b)
    hline(img, 8, 23, 9, f)
    hline(img, 8, 23, 10, f)
    hline(img, 8, 23, 11, b)
    # Body
    rect(img, 8, 11, 23, 24, f)
    # Outline
    vline(img, 8, 11, 24, b)
    vline(img, 23, 11, 24, b)
    hline(img, 8, 23, 24, b)
    # Highlight on flap
    hline(img, 9, 22, 9, h)
    # Highlight on body
    vline(img, 9, 12, 23, h)
    # Buckle
    rect(img, 14, 10, 17, 12, C['gold_m'])
    px(img, 15, 11, C['gold_l'])
    # Strap
    vline(img, 15, 8, 10, C['gold_d'])
    vline(img, 16, 8, 10, C['gold_d'])

def draw_endturn(img):
    """End turn arrow - purple theme."""
    draw_button_bg(img, C['purple_d'], C['purple_m'], C['purple_l'])
    a = C['white']
    a_h = C['purple_h']
    a_d = C['outline']
    # Curved arrow (clockwise)
    # Arrow head pointing right
    for i in range(5):
        px(img, 18, 12-i, a)
        px(img, 19, 12-i, a)
        px(img, 20, 12-i, a)
    px(img, 21, 10, a)
    px(img, 22, 11, a)
    px(img, 21, 12, a)
    # Arrow head highlight
    px(img, 19, 8, a_h)
    px(img, 20, 9, a_h)
    # Arrow shaft (curving)
    hline(img, 10, 18, 14, a)
    hline(img, 10, 18, 15, a)
    vline(img, 10, 14, 20, a)
    vline(img, 11, 14, 20, a)
    hline(img, 10, 16, 20, a)
    hline(img, 10, 16, 21, a)
    vline(img, 16, 18, 21, a)
    vline(img, 15, 18, 21, a)
    # Highlight
    hline(img, 11, 17, 14, a_h)
    px(img, 10, 19, a_h)
    # Outline accents
    px(img, 18, 13, a_d)

def draw_shop(img):
    """Coin/shop icon - gold theme."""
    draw_button_bg(img, C['gold_d'], C['gold_m'], C['gold_l'])
    c = C['gold_h']
    c_d = C['gold_d']
    o = C['outline']
    w = C['white']
    # Coin circle
    # Outer ring
    for angle_pts in [
        [(11,7),(12,7),(19,7),(20,7)],
        [(9,9),(10,8),(21,8),(22,9)],
        [(8,11),(8,12),(8,19),(8,20)],
        [(9,22),(10,23),(21,23),(22,22)],
        [(11,24),(12,25),(19,25),(20,24)],
        [(23,20),(24,19),(24,12),(23,11)],
    ]:
        for x, y in angle_pts:
            px(img, x, y, o)
    # Inner coin fill
    for y in range(9, 24):
        for x in range(10, 23):
            # Simple circle test
            dx, dy = x - 15.5, y - 16
            if dx*dx + dy*dy <= 36:
                px(img, x, y, c)
    # Inner ring
    for y in range(9, 24):
        for x in range(10, 23):
            dx, dy = x - 15.5, y - 16
            if 25 <= dx*dx + dy*dy <= 36:
                px(img, x, y, c_d)
    # Highlight
    px(img, 12, 10, w)
    px(img, 13, 10, w)
    px(img, 12, 11, w)
    # Center symbol (star/diamond)
    px(img, 15, 13, c_d)
    px(img, 16, 13, c_d)
    hline(img, 14, 17, 14, c_d)
    hline(img, 14, 17, 15, c_d)
    px(img, 15, 16, c_d)
    px(img, 16, 16, c_d)
    hline(img, 14, 17, 17, c_d)
    hline(img, 14, 17, 18, c_d)
    px(img, 15, 19, c_d)
    px(img, 16, 19, c_d)

def draw_rest(img):
    """Campfire icon - orange theme."""
    draw_button_bg(img, C['orange_d'], C['orange_m'], C['orange_l'])
    f = C['gold_l']
    f_h = C['gold_h']
    f_d = C['red_m']
    o = C['outline']
    w = C['white']
    # Flame shape
    # Outer flame (red)
    px(img, 15, 8, f_d)
    px(img, 16, 8, f_d)
    px(img, 14, 9, f_d)
    px(img, 15, 9, f_d)
    px(img, 16, 9, f_d)
    px(img, 17, 9, f_d)
    for y in range(10, 18):
        for x in range(13, 19):
            dx, dy = x - 15.5, y - 13
            if abs(dx) + abs(dy - 2) <= 5:
                px(img, x, y, f_d)
    # Inner flame (gold)
    for y in range(10, 17):
        for x in range(14, 18):
            dx, dy = x - 15.5, y - 13
            if abs(dx) + abs(dy - 2) <= 3.5:
                px(img, x, y, f)
    # Core (white-hot)
    px(img, 15, 12, w)
    px(img, 16, 12, w)
    px(img, 15, 13, f_h)
    px(img, 16, 13, f_h)
    # Logs
    hline(img, 9, 22, 22, o)
    hline(img, 9, 22, 23, C['brown'] if 'brown' in C else C['orange_d'])
    hline(img, 9, 22, 24, o)
    # Log cross
    # Left log (diagonal)
    for i in range(7):
        px(img, 9+i, 24-i//2, C['orange_d'])
    # Right log (diagonal)
    for i in range(7):
        px(img, 22-i, 24-i//2, C['orange_d'])

def draw_event(img):
    """Question mark - purple theme."""
    draw_button_bg(img, C['purple_d'], C['purple_m'], C['purple_l'])
    q = C['white']
    q_h = C['purple_h']
    o = C['outline']
    # Question mark shape (pixel art style)
    # Top curve
    hline(img, 12, 19, 7, q)
    hline(img, 12, 19, 8, q)
    px(img, 11, 9, q)
    px(img, 20, 9, q)
    px(img, 11, 10, q)
    px(img, 20, 10, q)
    vline(img, 11, 11, 13, q)
    vline(img, 20, 11, 13, q)
    # Curve into stem
    hline(img, 12, 19, 14, q)
    px(img, 16, 15, q)
    px(img, 16, 16, q)
    px(img, 15, 17, q)
    px(img, 16, 17, q)
    # Dot
    px(img, 16, 20, q)
    px(img, 15, 20, q)
    px(img, 16, 21, q)
    px(img, 15, 21, q)
    # Highlights
    px(img, 12, 7, q_h)
    px(img, 13, 7, q_h)
    px(img, 11, 9, q_h)

def draw_settings(img):
    """Gear icon - gray theme."""
    draw_button_bg(img, C['gray_d'], C['gray_m'], C['gray_l'])
    g = C['gray_h']
    g_d = C['outline']
    w = C['white']
    # Gear body - circle with teeth
    center_x, center_y = 15.5, 15.5
    # Outer gear ring with teeth
    for y in range(6, 26):
        for x in range(6, 26):
            dx, dy = x - center_x, y - center_y
            dist = (dx*dx + dy*dy) ** 0.5
            # Teeth (8 points)
            angle = (abs(dx) > 0.1 or abs(dy) > 0.1) and (abs(dx) + abs(dy))
            if 8.5 <= dist <= 10.5:
                # Check if on a tooth position
                import math
                a = math.atan2(dy, dx)
                tooth = (round(a / (math.pi / 4)) * (math.pi / 4))
                diff = abs(a - tooth)
                if diff < 0.35 or diff > math.pi - 0.35:
                    px(img, x, y, g)
            elif 7 <= dist <= 8.5:
                px(img, x, y, g_d)
    # Inner circle
    for y in range(10, 22):
        for x in range(10, 22):
            dx, dy = x - center_x, y - center_y
            dist = (dx*dx + dy*dy) ** 0.5
            if dist <= 5:
                px(img, x, y, g_d)
            if dist <= 3.5:
                px(img, x, y, C['gray_m'])
    # Center hole
    for y in range(13, 19):
        for x in range(13, 19):
            dx, dy = x - center_x, y - center_y
            if dx*dx + dy*dy <= 3:
                px(img, x, y, C['shadow'])
    # Highlight
    px(img, 12, 9, w)
    px(img, 13, 9, w)

def draw_boss(img):
    """Skull/crown icon - red theme (for boss battles)."""
    draw_button_bg(img, C['red_d'], C['red_m'], C['red_l'])
    s = C['white']
    s_d = C['gray_l']
    o = C['outline']
    r = C['red_h']
    # Crown shape
    hline(img, 9, 22, 20, s)
    hline(img, 9, 22, 21, s)
    hline(img, 9, 22, 22, o)
    # Crown spikes
    vline(img, 9, 14, 20, s)
    vline(img, 10, 14, 20, s)
    vline(img, 15, 8, 20, s)
    vline(img, 16, 8, 20, s)
    vline(img, 21, 14, 20, s)
    vline(img, 22, 14, 20, s)
    # Spike tips
    px(img, 9, 13, s)
    px(img, 10, 13, s)
    px(img, 9, 12, s)
    px(img, 10, 12, o)
    px(img, 15, 7, s)
    px(img, 16, 7, s)
    px(img, 15, 6, r)
    px(img, 16, 6, r)
    px(img, 21, 13, s)
    px(img, 22, 13, s)
    px(img, 22, 12, s)
    px(img, 21, 12, o)
    # Gems on crown
    px(img, 15, 10, r)
    px(img, 16, 10, r)
    px(img, 10, 16, r)
    px(img, 21, 16, r)
    # Crown base detail
    hline(img, 10, 21, 18, s_d)
    # Highlight
    hline(img, 10, 21, 21, C['white'])

def draw_card(img):
    """Card icon - blue theme (for card/deck related actions)."""
    draw_button_bg(img, C['blue_d'], C['blue_m'], C['blue_l'])
    c = C['white']
    c_d = C['gray_l']
    o = C['outline']
    h = C['blue_h']
    # Card shape (tilted)
    # Back card
    rect(img, 11, 9, 20, 23, c_d)
    rect(img, 11, 9, 20, 23, o)  # outline
    rect(img, 12, 10, 19, 22, c_d)
    # Front card (offset)
    rect(img, 9, 7, 18, 21, c)
    # Outline
    vline(img, 9, 7, 21, o)
    vline(img, 18, 7, 21, o)
    hline(img, 9, 18, 7, o)
    hline(img, 9, 18, 21, o)
    # Inner area
    rect(img, 10, 8, 17, 20, c)
    # Card content lines
    hline(img, 11, 16, 10, h)
    hline(img, 11, 16, 11, h)
    rect(img, 12, 13, 15, 16, h)
    hline(img, 11, 16, 18, c_d)
    hline(img, 11, 16, 19, c_d)
    # Highlight
    vline(img, 10, 8, 20, C['white'])


# ============================================================
# Generate all buttons
# ============================================================
buttons = {
    'attack':   draw_attack,
    'defend':   draw_defend,
    'item':     draw_item,
    'endturn':  draw_endturn,
    'shop':     draw_shop,
    'rest':     draw_rest,
    'event':    draw_event,
    'settings': draw_settings,
    'boss':     draw_boss,
    'card':     draw_card,
}

print("Generating pixel-art buttons...")
for name, draw_fn in buttons.items():
    img = make_canvas()
    draw_fn(img)
    save_button(img, name)

print(f"\nDone! {len(buttons)} buttons generated in {OUT_DIR}")
