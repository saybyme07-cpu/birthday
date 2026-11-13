import re, math

# Generate all SVG elements for the static cake
X = [110, 155, 203, 251, 291]
BASE = [172, 168, 164, 168, 172]
H = [96, 104, 116, 100, 96]

seed = 7
def rnd():
    global seed
    seed = (seed * 16807) % 2147483647
    return seed / 2147483647

cols = ['#f45b9a', '#f7b24a', '#5bc0e8', '#a77ad8', '#ffffff', '#7ccf8a']
spr_svg = []
for i in range(90):
    x = 38 + rnd() * 324
    yb = 280 + 38 * math.sqrt(max(0, 1 - math.pow((x - 200) / 170, 2)))
    y = yb - 6 - rnd() * 34
    c = cols[int(rnd() * len(cols))]
    r = int(rnd() * 180)
    spr_svg.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="3.6" height="9" rx="1.8" fill="{c}" transform="rotate({r} {x:.1f} {y:.1f})"/>')

drips_svg = []
for x, w, e in [[36, 28, 246], [104, 30, 240], [186, 30, 266], [262, 30, 244], [336, 26, 250]]:
    drips_svg.append(f'<rect x="{x}" y="190" width="{w}" height="{e - 190}" rx="{w/2}"/>')

sticks_svg = []
flames_svg = []
smokes_svg = []
for i, x in enumerate(X):
    top = BASE[i] - H[i]
    sticks_svg.append(f'''<rect x="{x-7}" y="{top}" width="14" height="{H[i]}" rx="7" fill="url(#stripe)" stroke="#f3a0c0" stroke-width=".8"/>
<ellipse cx="{x}" cy="{BASE[i]}" rx="14" ry="4.5" fill="#f9a8c8"/>
<path d="M{x} {top} v-6" stroke="#4a2a22" stroke-width="2" stroke-linecap="round"/>''')

    delay = -(i * 0.27)
    flames_svg.append(f'''<g class="fl" data-i="{i}" transform="translate({x} {top - 5})">
  <g class="lean" style="transition: opacity .4s ease;">
    <g class="flick" style="animation-delay:{delay:.2f}s">
      <circle r="40" cy="-22" fill="url(#glowG)"/>
      <path d="M0 3C-11-8-10-25 0-45 10-25 11-8 0 3Z" fill="url(#flameG)"/>
      <path d="M0 1C-5-4-5-13 0-23 5-13 5-4 0 1Z" fill="#fff8d6"/>
    </g>
  </g>
</g>''')

    smokes_svg.append(f'''<g class="smoke" data-i="{i}" transform="translate({x} {top - 14})">
  <circle r="6" style="--dx:-8px"/>
  <circle r="5" style="--dx:6px;animation-delay:.15s"/>
  <circle r="4" style="--dx:-2px;animation-delay:.3s"/>
</g>''')

swirls_svg = []
for x, y, s in [[72, 182, 0.8], [130, 206, 1], [205, 216, 1.1], [275, 206, 1], [332, 182, 0.8]]:
    swirls_svg.append(f'''<g transform="translate({x} {y}) scale({s})">
  <ellipse cy="5" rx="33" ry="13" fill="#e9cdb8" opacity=".55"/>
  <ellipse rx="30" ry="12" fill="#fffaf2"/><ellipse cy="-8" rx="23" ry="10" fill="#fffdf8"/><ellipse cy="-15" rx="14" ry="8" fill="#fff"/>
  <path d="M-24-4q12 6 24 0t24 0M-18-12q9 5 18 0t18 0" stroke="#f2e0cf" stroke-width="2" fill="none"/>
  <g transform="translate(0 -27)">
    <path d="M-13-9Q0-18 13-9Q11 9 0 17Q-11 9-13-9Z" fill="#e5322d"/>
    <path d="M-9-8Q-5-13 0-12" stroke="#ff9a90" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>
    <g fill="#ffd9a0"><circle cx="-5" cy="-1" r="1.2"/><circle cx="4" cy="-2" r="1.2"/><circle cx="0" cy="5" r="1.2"/><circle cx="-4" cy="9" r="1"/><circle cx="5" cy="8" r="1"/></g>
    <path d="M-8-12l8 4 8-4-4-5-4 3-4-3z" fill="#58a845"/>
  </g>
</g>''')

static_cake_svg = f"""<svg id="candle-cake" viewBox="0 -10 400 370" aria-label="Birthday cake with five lit candles" role="img">
  <defs>
    <linearGradient id="bodyG" x1="0" x2="1"><stop offset="0" stop-color="#f7d3c6"/><stop offset=".45" stop-color="#fff1e8"/><stop offset="1" stop-color="#f4cdbf"/></linearGradient>
    <linearGradient id="icingG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbb9d2"/><stop offset="1" stop-color="#f48db4"/></linearGradient>
    <linearGradient id="flameG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffab2e"/><stop offset=".5" stop-color="#ffd85a"/><stop offset="1" stop-color="#fff3b8"/></linearGradient>
    <radialGradient id="glowG"><stop offset="0" stop-color="#ffd778" stop-opacity=".85"/><stop offset="1" stop-color="#ffd778" stop-opacity="0"/></radialGradient>
    <pattern id="stripe" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="12" height="12" fill="#fff"/><rect width="6" height="12" fill="#f26aa0"/></pattern>
    <filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
  </defs>
  <!-- Plate -->
  <ellipse cx="200" cy="306" rx="196" ry="50" fill="#f6c3d0"/>
  <ellipse cx="200" cy="302" rx="186" ry="43" fill="#ffe9ef"/>
  <ellipse cx="200" cy="323" rx="168" ry="26" fill="#c9708f" opacity=".3" filter="url(#soft)"/>
  <!-- Cake Body -->
  <path d="M30 180V280A170 38 0 0 0 370 280V180Z" fill="url(#bodyG)"/>
  <g id="cake-sprinkles">{''.join(spr_svg)}</g>
  <!-- Icing -->
  <ellipse cx="200" cy="178" rx="170" ry="44" fill="url(#icingG)"/>
  <rect x="30" y="178" width="340" height="26" fill="#f79cc0"/>
  <g fill="#f79cc0" id="cake-drips">{''.join(drips_svg)}</g>
  <ellipse cx="200" cy="176" rx="170" ry="44" fill="url(#icingG)" clip-path="inset(0 0 60% 0)"/>
  <ellipse cx="150" cy="168" rx="80" ry="11" fill="#fff" opacity=".22"/>
  <!-- Interactive candle elements (Statically embedded for 100% reliability!) -->
  <g id="cake-sticks">{''.join(sticks_svg)}</g>
  <g id="cake-swirls">{''.join(swirls_svg)}</g>
  <g id="cake-flames">{''.join(flames_svg)}</g>
  <g id="cake-smokes" fill="#fff">{''.join(smokes_svg)}</g>
</svg>"""

for fname in ['step6.html', 'review.html']:
    path = f'/Users/neelamvishwanatham/Documents/saybyme-birthday/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the CSS for phone slides: bulletproof display toggle!
    css_fix = """
  .phone-slides-wrap {
    position: relative;
    width: 100%;
    height: 100%;
    flex-grow: 1;
    overflow: hidden;
  }
  .phone-slide {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: none !important;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 38px 16px 20px;
    z-index: 5;
  }
  .phone-slide.active {
    display: flex !important;
    z-index: 10;
    animation: fadeInSlide 0.28s ease-out;
  }
  @keyframes fadeInSlide {
    from { opacity: 0; transform: scale(0.98); }
    to { opacity: 1; transform: scale(1); }
  }
  .candle-experience-slide {
    display: none !important;
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    padding: 38px 14px 18px;
    user-select: none;
    -webkit-user-select: none;
    touch-action: none;
    z-index: 5;
  }
  .candle-experience-slide.active {
    display: flex !important;
    z-index: 10;
    animation: fadeInSlide 0.28s ease-out;
  }
"""
    # Replace slide CSS
    html = re.sub(r'\.phone-slides-wrap \{[\s\S]*?\.candle-experience-slide \{[\s\S]*?\}', css_fix.strip(), html)

    # 2. Replace the SVG inside Slide 1 with static_cake_svg
    html = re.sub(r'<svg id="candle-cake"[\s\S]*?</svg>', static_cake_svg, html)

    # 3. Update the openGiftBox and button click logic:
    # Clicking "Tap to Open" triggers the gift open and transitions smoothly to Slide 1
    new_open_logic = """
  let isNavigatingToSlide1 = false;
  function openGiftBox() {
    if (isNavigatingToSlide1) return;
    isNavigatingToSlide1 = true;

    // Trigger lid pop, chime, and confetti
    if (giftStage) {
      giftStage.classList.add('is-open');
    }
    playMagicChime();
    triggerBoxConfetti();

    if (openActionLabel) openActionLabel.textContent = 'Opening Surprise...';
    if (openActionBtn) openActionBtn.classList.add('opened-mode');

    // Immediately after quick burst (450ms), transition directly into Slide 1 (Candles)
    setTimeout(() => {
      goToSlide(1);
      isNavigatingToSlide1 = false;
    }, 450);
  }
"""
    html = re.sub(r'let isNavigatingToSlide1 = false;\s*function openGiftBox\(\) \{[\s\S]*?isNavigatingToSlide1 = false;\s*\}, 950\);\s*\}', new_open_logic.strip(), html)

    # Also add direct onclick on the button so it is 100% guaranteed to trigger
    html = html.replace(
        '<button class="btn-tap-open-main" id="btn-phone-open-action" type="button">',
        '<button class="btn-tap-open-main" id="btn-phone-open-action" type="button" onclick="openGiftBox()">'
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Applied bulletproof slide display and pre-rendered SVG cake to both step6.html and review.html!")
