candle_html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover, user-scalable=no">
<title>SayByMe – Make a Wish</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Kaushan+Script&family=Nunito:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
  :root{--crimson:#9b1c4a;--rose:#e8236f;--mauve:#5c4a57;--pill:#b0194f}
  *{box-sizing:border-box;margin:0;padding:0;-webkit-tap-highlight-color:transparent}
  html,body{height:100%;overflow:hidden;background:#f9cfe0;touch-action:none}
  body{display:flex;align-items:center;justify-content:center;font-family:'Nunito',system-ui,sans-serif}
  .screen{
    position:relative;width:min(100vw,430px);height:min(100dvh,900px);overflow:hidden;
    display:flex;flex-direction:column;
    background:radial-gradient(ellipse at 50% 38%,#fff0f6 0%,transparent 60%),linear-gradient(180deg,#fcdce9,#f8c8dc 70%,#f9cde0);
    user-select:none;-webkit-user-select:none;-webkit-touch-callout:none;cursor:pointer;
  }
  @media(min-width:520px){.screen{border-radius:44px;box-shadow:0 30px 80px rgba(160,40,90,.28)}}

  /* Top Navigation Bar */
  .top-nav {
    position: absolute;
    top: 14px;
    left: 16px;
    right: 16px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    z-index: 10;
  }
  .btn-nav-back {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    background: rgba(255, 255, 255, 0.75);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(232, 35, 111, 0.25);
    border-radius: 999px;
    padding: 6px 14px;
    font-size: 13px;
    font-weight: 700;
    color: var(--crimson);
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 4px 12px rgba(160, 40, 90, 0.08);
    transition: transform 0.2s ease, background 0.2s ease;
  }
  .btn-nav-back:hover {
    background: #ffffff;
    transform: scale(1.04);
  }

  /* lights */
  .lights{position:absolute;top:0;left:0;width:100%;height:auto;z-index:3;pointer-events:none}
  .bulb{animation:twinkle 2.4s ease-in-out infinite alternate}
  @keyframes twinkle{from{opacity:.75}to{opacity:1}}

  /* header */
  .top{position:relative;z-index:4;text-align:center;padding:clamp(90px,14vh,130px) 20px 0}
  h1{font-family:'Kaushan Script',cursive;font-weight:400;color:var(--crimson);font-size:clamp(40px,12vw,54px);line-height:1.08;text-wrap:balance;
     transition:opacity .25s,transform .25s}
  .sub{margin-top:8px;font-size:clamp(17px,5vw,22px);font-weight:600;color:var(--mauve);transition:opacity .25s,transform .25s}
  .swap{opacity:0;transform:translateY(8px)}
  .divider{display:flex;align-items:center;justify-content:center;gap:14px;margin-top:20px}
  .divider i{display:block;width:34%;height:1.5px;background:var(--crimson);opacity:.7}
  .divider svg{width:28px;height:26px;fill:var(--crimson);animation:beat 1.6s ease-in-out infinite}
  @keyframes beat{0%,100%{transform:scale(1)}15%{transform:scale(1.18)}30%{transform:scale(1)}45%{transform:scale(1.12)}}

  /* decorations */
  .deco{position:absolute;z-index:1;pointer-events:none;filter:blur(1.6px);opacity:.9}
  .balloon{right:-34px;top:36%;width:100px}
  .balloon.b2{right:-20px;top:46%;width:90px;opacity:.5;filter:blur(5px)}
  .gift{left:-26px;top:48%;width:100px}
  .gift.g2{left:auto;right:-30px;top:63%;width:86px}
  .bit{position:absolute;z-index:2;border-radius:2px;pointer-events:none}

  /* cake */
  .stageWrap{position:relative;flex:1;min-height:0;display:flex;align-items:center;justify-content:center;z-index:3;padding:8px 4px 0}
  .glow{position:absolute;left:50%;top:38%;width:115%;aspect-ratio:1;transform:translate(-50%,-50%);
        background:radial-gradient(circle,rgba(255,226,150,.6),rgba(255,226,150,0) 60%);transition:opacity .7s;pointer-events:none}
  #cake{position:relative;width:100%;height:100%;overflow:visible}

  .lean{transition:opacity .5s}
  .out .lean{opacity:0;transition-duration:.1s}
  .flick{animation:flick 1.1s ease-in-out infinite alternate}
  @keyframes flick{
    0%{transform:scale(1,1) rotate(-1.5deg)}
    35%{transform:scale(.94,1.07) rotate(1.8deg)}
    70%{transform:scale(1.04,.96) rotate(-.6deg)}
    100%{transform:scale(.97,1.05) rotate(1.2deg)}
  }
  .smoke circle{opacity:0}
  .smoke.puff circle{animation:smoke 1.9s ease-out forwards}
  @keyframes smoke{
    0%{opacity:.55;transform:translate(0,0) scale(.4)}
    100%{opacity:0;transform:translate(var(--dx),-80px) scale(2.2)}
  }

  /* hint pill & action buttons */
  .bottom-actions-wrap {
    position: relative;
    z-index: 5;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
    margin-bottom: clamp(24px, 5vh, 48px);
    width: 100%;
  }
  .pill{
    position:relative;overflow:hidden;
    display:flex;align-items:center;gap:18px;width:min(84%,330px);padding:13px 24px;
    border-radius:999px;border:1.5px solid #f4a3c2;color:var(--pill);font:700 clamp(16px,4.6vw,19px)/1.25 'Nunito',sans-serif;
    background:linear-gradient(180deg,rgba(255,255,255,.65),rgba(253,215,230,.7));box-shadow:0 10px 24px rgba(220,80,130,.18);
    transition:transform .2s;
  }
  .pill::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(255,150,190,.38),rgba(240,48,111,.4));
    transform:scaleX(var(--p,0));transform-origin:left;pointer-events:none}
  .pill>*{position:relative}
  .pill svg{flex:none;width:38px;height:42px;fill:none;stroke:var(--pill);stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round;animation:tap 1.8s ease-in-out infinite}
  @keyframes tap{0%,100%{transform:translateY(0) scale(1)}50%{transform:translateY(3px) scale(.92)}}
  .blowing .pill{transform:scale(.96)}
  .blowing .pill svg{animation:none;transform:scale(.9)}
  .pill:focus-visible{outline:3px solid var(--crimson);outline-offset:3px}

  /* Continue to next surprise button (appears when candles are out) */
  .btn-next-surprise {
    display: none;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 13px 34px;
    background: linear-gradient(90deg, #e8236f 0%, #9b1c4a 100%);
    color: #ffffff;
    border: none;
    border-radius: 999px;
    font-family: inherit;
    font-size: 16px;
    font-weight: 800;
    cursor: pointer;
    box-shadow: 0 8px 24px rgba(232, 35, 111, 0.45);
    animation: popIn 0.35s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  @keyframes popIn {
    from { opacity: 0; transform: scale(0.85); }
    to { opacity: 1; transform: scale(1); }
  }
  .btn-next-surprise:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 12px 28px rgba(232, 35, 111, 0.55);
  }

  #fx{position:absolute;inset:0;width:100%;height:100%;z-index:6;pointer-events:none}
  @media(prefers-reduced-motion:reduce){.bulb,.divider svg,.pill svg{animation:none}}
</style>
</head>
<body>
<div class="screen" id="screen">

  <!-- Top Nav Bar -->
  <div class="top-nav">
    <button type="button" class="btn-nav-back" id="btn-back">
      <span>←</span> Review
    </button>
  </div>

  <!-- string lights -->
  <svg class="lights" viewBox="0 0 430 130" aria-hidden="true">
    <defs><filter id="bl"><feGaussianBlur stdDeviation="5"/></filter></defs>
    <path d="M0 92Q90 78 160 18M430 92Q340 78 270 18" fill="none" stroke="#d9a35e" stroke-width="1.6" opacity=".8"/>
    <g id="bulbs"></g>
  </svg>

  <!-- background decorations -->
  <svg class="deco balloon" viewBox="0 0 100 150" aria-hidden="true"><ellipse cx="50" cy="55" rx="46" ry="54" fill="#f27fb0"/><ellipse cx="32" cy="34" rx="9" ry="16" fill="#fff" opacity=".4"/></svg>
  <svg class="deco balloon b2" viewBox="0 0 100 150" aria-hidden="true"><ellipse cx="50" cy="55" rx="46" ry="54" fill="#fbc3d8"/></svg>
  <svg class="deco gift" viewBox="0 0 110 130" aria-hidden="true">
    <rect x="6" y="40" width="104" height="90" rx="4" fill="#fff4ee"/><rect x="40" y="40" width="22" height="90" fill="#f27fa7"/>
    <path d="M51 40C30 8 4 16 18 34c8 8 28 6 33 6zM51 40c21-32 47-24 33-6-8 8-28 6-33 6z" fill="#f48fb5"/>
  </svg>
  <svg class="deco gift g2" viewBox="0 0 110 130" aria-hidden="true">
    <rect x="0" y="50" width="104" height="80" rx="4" fill="#fff4ee"/><rect x="40" y="50" width="22" height="80" fill="#f27fa7"/>
    <path d="M51 50C34 24 12 30 24 44c7 7 22 6 27 6z" fill="#f48fb5"/>
  </svg>
  <span class="bit" style="left:7%;top:71%;width:16px;height:9px;background:#f7b24a;transform:rotate(-12deg)"></span>
  <span class="bit" style="left:20%;top:77%;width:14px;height:8px;background:#f06a9b;transform:rotate(18deg)"></span>
  <span class="bit" style="left:82%;top:73%;width:15px;height:8px;background:#f06a9b;transform:rotate(-14deg)"></span>
  <span class="bit" style="left:90%;top:70%;width:14px;height:8px;background:#f7b24a;transform:rotate(8deg)"></span>
  <span class="bit" style="left:14%;top:84%;width:12px;height:7px;background:#f7a46a;transform:rotate(6deg)"></span>

  <div class="top">
    <h1 id="title">Make a Wish</h1>
    <p class="sub" id="sub">Blow Out the Candles</p>
    <div class="divider"><i></i>
      <svg viewBox="0 0 30 28" aria-hidden="true"><path d="M15 27C2 18 0 8 6 3.500c4-3 8-1 9 3 1-4 5-6 9-3 6 4.500 4 14.500-9 23.500z"/></svg><i></i></div>
  </div>

  <div class="stageWrap">
    <div class="glow" id="glow"></div>
    <svg id="cake" viewBox="0 -10 400 370" aria-label="Birthday cake with five lit candles" role="img">
      <defs>
        <linearGradient id="bodyG" x1="0" x2="1"><stop offset="0" stop-color="#f7d3c6"/><stop offset=".45" stop-color="#fff1e8"/><stop offset="1" stop-color="#f4cdbf"/></linearGradient>
        <linearGradient id="icingG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fbb9d2"/><stop offset="1" stop-color="#f48db4"/></linearGradient>
        <linearGradient id="flameG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffab2e"/><stop offset=".5" stop-color="#ffd85a"/><stop offset="1" stop-color="#fff3b8"/></linearGradient>
        <radialGradient id="glowG"><stop offset="0" stop-color="#ffd778" stop-opacity=".8"/><stop offset="1" stop-color="#ffd778" stop-opacity="0"/></radialGradient>
        <pattern id="stripe" width="12" height="12" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><rect width="12" height="12" fill="#fff"/><rect width="6" height="12" fill="#f26aa0"/></pattern>
        <filter id="soft"><feGaussianBlur stdDeviation="6"/></filter>
      </defs>
      <!-- plate -->
      <ellipse cx="200" cy="306" rx="196" ry="50" fill="#f6c3d0"/>
      <ellipse cx="200" cy="302" rx="186" ry="43" fill="#ffe9ef"/>
      <ellipse cx="200" cy="323" rx="168" ry="26" fill="#c9708f" opacity=".3" filter="url(#soft)"/>
      <!-- body -->
      <path d="M30 180V280A170 38 0 0 0 370 280V180Z" fill="url(#bodyG)"/>
      <g id="spr"></g>
      <!-- icing -->
      <ellipse cx="200" cy="178" rx="170" ry="44" fill="url(#icingG)"/>
      <rect x="30" y="178" width="340" height="26" fill="#f79cc0"/>
      <g fill="#f79cc0" id="drips"></g>
      <ellipse cx="200" cy="176" rx="170" ry="44" fill="url(#icingG)" clip-path="inset(0 0 60% 0)"/>
      <ellipse cx="150" cy="168" rx="80" ry="11" fill="#fff" opacity=".22"/>
      <g id="sticks"></g>
      <g id="swirls"></g>
      <g id="flames"></g>
      <g id="smokes" fill="#fff"></g>
    </svg>
  </div>

  <div class="bottom-actions-wrap">
    <button class="pill" id="pill" type="button" aria-live="polite">
      <svg viewBox="0 0 48 52" aria-hidden="true"><path d="M13 9a10.500 10.500 0 0 1 21 0M20 32V13a3.500 3.500 0 0 1 7 0v13M27 25a3 3 0 0 1 6 0v3M33 27a3 3 0 0 1 6 0v6c0 8-5 13-12 13h-3c-5 0-8-3-11-8l-4-6a3 3 0 0 1 5-3l3 3"/></svg>
      <span id="pillText">Press &amp; Hold to<br>Blow the Candles</span>
    </button>

    <button class="btn-next-surprise" id="btn-next-surprise" type="button">
      Next: Cut the Cake 🍰 →
    </button>
  </div>

  <canvas id="fx"></canvas>
</div>

<script>
(() => {
  const $ = s => document.querySelector(s);
  const screen = $('#screen'), pill = $('#pill'), glow = $('#glow'), cakeEl = $('#cake');
  const cv = $('#fx'), ctx = cv.getContext('2d');
  const nextSurpriseBtn = $('#btn-next-surprise');

  /* ---------- URL params ---------- */
  const params = new URLSearchParams(location.search);
  const name = params.get('to') || 'Sanjana';
  const fromName = params.get('from') || 'Rohan';
  const rel = params.get('rel') || 'Girlfriend';
  const date = params.get('date') || '';
  const msg = params.get('msg') || '';
  const features = params.get('features') || 'candles,cake,celebration';

  // Back button returns to review step6
  $('#btn-back').addEventListener('click', () => {
    location.href = 'step6.html?' + params.toString();
  });

  // Next surprise button advances to surprise.html
  nextSurpriseBtn.addEventListener('click', () => {
    location.href = 'surprise.html?' + params.toString();
  });

  /* ---------- config ---------- */
  const X    = [110, 155, 203, 251, 291];
  const BASE = [172, 168, 164, 168, 172];
  const H    = [96, 104, 116, 100, 96];
  const TH   = [.50, .68, .92, .60, .80];
  const HOLD_SECONDS = 2.4;

  /* ---------- build artwork ---------- */
  let seed = 7; const rnd = () => (seed = (seed * 16807) % 2147483647) / 2147483647;
  const add = (id, html) => $(id).insertAdjacentHTML('beforeend', html);

  // lights
  [[0,92],[43.8,82.1],[85,66.5],[123.8,45.1],[160,18]].forEach(([x,y],i) => {
    [x, 430 - x].forEach((px, k) => add('#bulbs',
      `<g class="bulb" style="animation-delay:-${(i*.5+k*.8).toFixed(1)}s"><circle cx="${px}" cy="${y}" r="15" fill="#ffe27a" opacity=".5" filter="url(#bl)"/><circle cx="${px}" cy="${y}" r="7" fill="#fff8d6"/></g>`));
  });

  // drips
  [[36,28,246],[104,30,240],[186,30,266],[262,30,244],[336,26,250]].forEach(([x,w,e]) =>
    add('#drips', `<rect x="${x}" y="190" width="${w}" height="${e-190}" rx="${w/2}"/>`));

  // sprinkles on the lower side
  const cols = ['#f45b9a','#f7b24a','#5bc0e8','#a77ad8','#ffffff','#7ccf8a'];
  for (let i = 0; i < 110; i++) {
    const x = 38 + rnd() * 324, yb = 280 + 38 * Math.sqrt(1 - ((x - 200) / 170) ** 2);
    const y = yb - 6 - rnd() * 34, c = cols[(rnd() * cols.length) | 0], r = (rnd() * 180) | 0;
    add('#spr', `<rect x="${x.toFixed(1)}" y="${y.toFixed(1)}" width="3.600" height="9" rx="1.800" fill="${c}" transform="rotate(${r} ${x.toFixed(1)} ${y.toFixed(1)})"/>`);
  }

  // candles
  X.forEach((x, i) => {
    const top = BASE[i] - H[i];
    add('#sticks',
      `<rect x="${x-7}" y="${top}" width="14" height="${H[i]}" rx="7" fill="url(#stripe)" stroke="#f3a0c0" stroke-width=".8"/>
       <ellipse cx="${x}" cy="${BASE[i]}" rx="14" ry="4.500" fill="#f9a8c8"/>
       <path d="M${x} ${top} v-6" stroke="#4a2a22" stroke-width="2" stroke-linecap="round"/>`);
    add('#flames',
      `<g class="fl" data-i="${i}" transform="translate(${x} ${top-5})"><g class="lean"><g class="flick" style="animation-delay:-${(i*.27).toFixed(2)}s">
         <circle r="40" cy="-22" fill="url(#glowG)"/>
         <path d="M0 3C-11-8-10-25 0-45 10-25 11-8 0 3Z" fill="url(#flameG)"/>
         <path d="M0 1C-5-4-5-13 0-23 5-13 5-4 0 1Z" fill="#fff8d6"/>
       </g></g></g>`);
    add('#smokes',
      `<g class="smoke" data-i="${i}" transform="translate(${x} ${top-14})">
         <circle r="6" style="--dx:-8px"/><circle r="5" style="--dx:6px;animation-delay:.15s"/><circle r="4" style="--dx:-2px;animation-delay:.3s"/></g>`);
  });

  // cream swirls + strawberries
  [[72,182,.8],[130,206,1],[205,216,1.1],[275,206,1],[332,182,.8]].forEach(([x,y,s]) =>
    add('#swirls',
      `<g transform="translate(${x} ${y}) scale(${s})">
         <ellipse cy="5" rx="33" ry="13" fill="#e9cdb8" opacity=".55"/>
         <ellipse rx="30" ry="12" fill="#fffaf2"/><ellipse cy="-8" rx="23" ry="10" fill="#fffdf8"/><ellipse cy="-15" rx="14" ry="8" fill="#fff"/>
         <path d="M-24-4q12 6 24 0t24 0M-18-12q9 5 18 0t18 0" stroke="#f2e0cf" stroke-width="2" fill="none"/>
         <g transform="translate(0 -27)">
           <path d="M-13-9Q0-18 13-9Q11 9 0 17Q-11 9-13-9Z" fill="#e5322d"/>
           <path d="M-9-8Q-5-13 0-12" stroke="#ff9a90" stroke-width="3" fill="none" stroke-linecap="round" opacity=".7"/>
           <g fill="#ffd9a0"><circle cx="-5" cy="-1" r="1.200"/><circle cx="4" cy="-2" r="1.200"/><circle cx="0" cy="5" r="1.200"/><circle cx="-4" cy="9" r="1"/><circle cx="5" cy="8" r="1"/></g>
           <path d="M-8-12l8 4 8-4-4-5-4 3-4-3z" fill="#58a845"/>
         </g></g>`));

  /* ---------- state ---------- */
  const fl = [...document.querySelectorAll('.fl')];
  const lean = fl.map(f => f.querySelector('.lean'));
  const smoke = [...document.querySelectorAll('.smoke')];
  const out = [false, false, false, false, false];
  let p = 0, holding = false, done = false, last = 0;
  let parts = [], W = 0, Hh = 0, dpr = 1;

  function resize() {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = screen.clientWidth; Hh = screen.clientHeight;
    cv.width = W * dpr; cv.height = Hh * dpr;
  }
  addEventListener('resize', resize); resize();

  const rel = el => { const a = el.getBoundingClientRect(), b = screen.getBoundingClientRect(); return { x: a.left - b.left, y: a.top - b.top, w: a.width, h: a.height }; };

  function setText(t, s, pt) {
    const T = $('#title'), S = $('#sub');
    T.classList.add('swap'); S.classList.add('swap');
    setTimeout(() => {
      T.textContent = t; S.textContent = s; $('#pillText').innerHTML = pt;
      T.classList.remove('swap'); S.classList.remove('swap');
    }, 250);
  }

  function extinguish(i) {
    out[i] = true;
    fl[i].classList.add('out');
    lean[i].setAttribute('transform', 'rotate(0) scale(1 1)');
    const s = smoke[i]; s.classList.remove('puff'); void s.getBoundingClientRect(); s.classList.add('puff');
  }

  function burst(ox, oy, n, spread) {
    const c = ['#f45b9a','#f7b24a','#ffd95a','#5bc0e8','#a77ad8','#ff7aa8','#ffffff'];
    for (let i = 0; i < n; i++) {
      const a = -Math.PI / 2 + (Math.random() - .5) * spread, sp = 300 + Math.random() * 520;
      parts.push({ k: 'c', x: ox, y: oy, vx: Math.cos(a) * sp, vy: Math.sin(a) * sp, r: Math.random() * 6.3, vr: (Math.random() - .5) * 14,
                   w: 6 + Math.random() * 6, h: 3 + Math.random() * 5, col: c[(Math.random() * c.length) | 0], life: 2.2 + Math.random() * 1.2, age: 0 });
    }
  }

  function finish() {
    done = true; holding = false; screen.classList.remove('blowing');
    glow.style.opacity = .3;
    const c = rel(cakeEl);
    burst(c.x + c.w / 2, c.y + c.h * .3, 130, Math.PI * 1.1);
    setTimeout(() => { burst(c.x + c.w * .2, c.y + c.h * .45, 50, 1.2); burst(c.x + c.w * .8, c.y + c.h * .45, 50, 1.2); }, 260);
    setText(name ? 'Happy Birthday, ' + name + '!' : 'Happy Birthday!', 'Your wish is on its way ✨', 'Tap to<br>Relight the Candles');
    nextSurpriseBtn.style.display = 'inline-flex';
    try { navigator.vibrate && navigator.vibrate([40, 40, 80]); } catch (e) {}
  }

  function reset() {
    done = false; p = 0;
    out.forEach((_, i) => setTimeout(() => { out[i] = false; fl[i].classList.remove('out'); }, i * 140));
    glow.style.opacity = 1;
    setText('Make a Wish', 'Blow Out the Candles', 'Press &amp; Hold to<br>Blow the Candles');
    nextSurpriseBtn.style.display = 'none';
  }

  /* ---------- input ---------- */
  const start = () => { if (!done) { holding = true; screen.classList.add('blowing'); } };
  const stop  = () => { holding = false; screen.classList.remove('blowing'); };
  screen.addEventListener('pointerdown', e => { if (done) { if (e.target.closest('#pill')) reset(); return; } start(); });
  ['pointerup', 'pointercancel'].forEach(n => addEventListener(n, stop));
  addEventListener('blur', stop);
  addEventListener('contextmenu', e => e.preventDefault());
  addEventListener('keydown', e => { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) { e.preventDefault(); done ? reset() : start(); } });
  addEventListener('keyup', e => { if (e.key === ' ' || e.key === 'Enter') stop(); });

  /* ---------- main loop ---------- */
  function frame(t) {
    const dt = Math.min(.05, (t - last) / 1000 || 0); last = t;

    if (!done) {
      p = holding ? Math.min(1, p + dt / HOLD_SECONDS) : Math.max(0, p - dt / .8);
      let lit = 0;
      for (let i = 0; i < 5; i++) {
        if (!out[i] && holding && p >= TH[i]) extinguish(i);
        if (!out[i]) {
          lit++;
          const wob = Math.sin(t / 55 + i * 1.7) * 5 * p;
          lean[i].setAttribute('transform', `rotate(${(p * 34 + wob).toFixed(2)}) scale(${(1 - p * .22).toFixed(3)} ${(1 - p * .4).toFixed(3)})`);
        }
      }
      glow.style.opacity = (.25 + .75 * lit / 5 * (1 - p * .25)).toFixed(2);
      if (lit === 0) finish();

      // breath particles
      if (holding && Math.random() < dt * 55) {
        const a = rel(pill), c = rel(cakeEl), d = .9;
        const ox = a.x + a.w / 2 + (Math.random() - .5) * 60, oy = a.y;
        const tx = c.x + c.w / 2 + (Math.random() - .5) * 90, ty = c.y + c.h * .22;
        parts.push({ k: 'b', x: ox, y: oy, vx: (tx - ox) / d, vy: (ty - oy) / d, r0: 5, life: d + Math.random() * .3, age: 0 });
      }
    }
    pill.style.setProperty('--p', done ? 0 : p.toFixed(3));

    // draw particles
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, Hh);
    parts = parts.filter(q => (q.age += dt) < q.life && q.y < Hh + 30);
    for (const q of parts) {
      q.x += q.vx * dt; q.y += q.vy * dt;
      if (q.k === 'b') {
        const k = q.age / q.life; ctx.globalAlpha = .32 * (1 - k);
        ctx.fillStyle = '#fff'; ctx.beginPath(); ctx.arc(q.x, q.y, q.r0 + k * 26, 0, 6.283); ctx.fill();
      } else {
        q.vy += 900 * dt; q.vx *= .992; q.r += q.vr * dt;
        ctx.globalAlpha = Math.min(1, (q.life - q.age) * 2);
        ctx.save(); ctx.translate(q.x, q.y); ctx.rotate(q.r); ctx.fillStyle = q.col; ctx.fillRect(-q.w / 2, -q.h / 2, q.w, q.h); ctx.restore();
      }
    }
    ctx.globalAlpha = 1;
    requestAnimationFrame(frame);
  }
  requestAnimationFrame(frame);
})();
</script>
</body>
</html>"""

with open('/Users/neelamvishwanatham/Documents/saybyme-birthday/candle.html', 'w', encoding='utf-8') as f:
    f.write(candle_html_content)

print("Saved candle.html successfully!")
