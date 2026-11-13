import re

for fname in ['step6.html', 'review.html']:
    path = f'/Users/neelamvishwanatham/Documents/saybyme-birthday/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find initCandleSlideEngine and replace it with a clean version that directly attaches to pre-rendered elements
    old_engine_pattern = r'function initCandleSlideEngine\(\) \{[\s\S]*?initCandleSlideEngine\(\);'

    clean_engine = """function initCandleSlideEngine() {
    if (window.candleEngineInitialized) return;
    window.candleEngineInitialized = true;

    const slide = document.getElementById('candle-slide');
    if (!slide) return;

    const pill = document.getElementById('candle-pill-btn');
    const pillText = document.getElementById('candle-pill-text');
    const glow = document.getElementById('candle-glow');
    const cakeEl = document.getElementById('candle-cake');
    const cv = document.getElementById('candle-fx');
    const nextBtn = document.getElementById('btn-next-cake-action');
    if (!cv) return;
    const ctx = cv.getContext('2d');

    const TH = [0.50, 0.68, 0.92, 0.60, 0.80];
    const HOLD_SECONDS = 2.2;

    const fl = [...slide.querySelectorAll('.fl')];
    const lean = fl.map(f => f.querySelector('.lean'));
    const smoke = [...slide.querySelectorAll('.smoke')];
    const out = [false, false, false, false, false];
    let p = 0, holding = false, done = false, last = 0;
    let parts = [], W = 340, Hh = 680, dpr = 1;

    window.resizeCandleCanvas = function() {
      dpr = Math.min(window.devicePixelRatio || 1, 2);
      W = slide.clientWidth || 340;
      Hh = slide.clientHeight || 680;
      cv.width = W * dpr;
      cv.height = Hh * dpr;
    };
    window.resizeCandleCanvas();
    window.addEventListener('resize', window.resizeCandleCanvas);

    const relPos = el => {
      const a = el.getBoundingClientRect();
      const b = slide.getBoundingClientRect();
      return { x: a.left - b.left, y: a.top - b.top, w: a.width, h: a.height };
    };

    function setCandleText(t, s, pt) {
      const T = document.getElementById('candle-title');
      const S = document.getElementById('candle-sub');
      if (T) T.classList.add('swap');
      if (S) S.classList.add('swap');
      setTimeout(() => {
        if (T) T.textContent = t;
        if (S) S.textContent = s;
        if (pillText) pillText.innerHTML = pt;
        if (T) T.classList.remove('swap');
        if (S) S.classList.remove('swap');
      }, 250);
    }

    function extinguishCandle(i) {
      out[i] = true;
      if (fl[i]) fl[i].classList.add('out');
      if (lean[i]) lean[i].setAttribute('transform', 'rotate(0) scale(1 1)');
      const sm = smoke[i];
      if (sm) {
        sm.classList.remove('puff');
        void sm.getBoundingClientRect();
        sm.classList.add('puff');
      }
    }

    function burstConfetti(ox, oy, n, spread) {
      const c = ['#f45b9a', '#f7b24a', '#ffd95a', '#5bc0e8', '#a77ad8', '#ff7aa8', '#ffffff'];
      for (let i = 0; i < n; i++) {
        const a = -Math.PI / 2 + (Math.random() - 0.5) * spread;
        const sp = 260 + Math.random() * 450;
        parts.push({
          k: 'c', x: ox, y: oy,
          vx: Math.cos(a) * sp, vy: Math.sin(a) * sp,
          r: Math.random() * 6.3, vr: (Math.random() - 0.5) * 14,
          w: 5 + Math.random() * 5, h: 3 + Math.random() * 4,
          col: c[(Math.random() * c.length) | 0],
          life: 2.2 + Math.random() * 1.0, age: 0
        });
      }
    }

    function finishBlowing() {
      done = true;
      holding = false;
      slide.classList.remove('blowing');
      if (glow) glow.style.opacity = 0.25;

      const c = relPos(cakeEl);
      burstConfetti(c.x + c.w / 2, c.y + c.h * 0.3, 110, Math.PI * 1.1);
      setTimeout(() => {
        burstConfetti(c.x + c.w * 0.25, c.y + c.h * 0.45, 45, 1.2);
        burstConfetti(c.x + c.w * 0.75, c.y + c.h * 0.45, 45, 1.2);
      }, 240);

      const recipient = toName || 'Sanjana';
      setCandleText(`Happy Birthday, ${recipient}!`, 'Your wish is on its way ✨', 'Tap to Relight Candles ↺');
      if (nextBtn) nextBtn.style.display = 'inline-block';

      try {
        if (navigator.vibrate) navigator.vibrate([40, 40, 80]);
      } catch (e) {}
    }

    function resetCandles() {
      done = false;
      p = 0;
      out.forEach((_, i) => setTimeout(() => {
        out[i] = false;
        if (fl[i]) fl[i].classList.remove('out');
      }, i * 130));
      if (glow) glow.style.opacity = 1;
      setCandleText('Make a Wish', 'Blow Out the Candles', 'Press &amp; Hold to<br>Blow the Candles');
      if (nextBtn) nextBtn.style.display = 'none';
    }

    // Input handlers bound to slide
    const startHold = () => {
      if (!done) {
        holding = true;
        slide.classList.add('blowing');
      }
    };
    const stopHold = () => {
      holding = false;
      slide.classList.remove('blowing');
    };

    slide.addEventListener('pointerdown', e => {
      if (done) {
        if (e.target.closest('#candle-pill-btn')) resetCandles();
        return;
      }
      startHold();
    });
    ['pointerup', 'pointercancel'].forEach(ev => window.addEventListener(ev, stopHold));
    window.addEventListener('blur', stopHold);

    // Frame animation loop
    function candleFrame(t) {
      const dt = Math.min(0.05, (t - last) / 1000 || 0);
      last = t;

      if (!done) {
        p = holding ? Math.min(1, p + dt / HOLD_SECONDS) : Math.max(0, p - dt / 0.8);
        let lit = 0;
        for (let i = 0; i < 5; i++) {
          if (!out[i] && holding && p >= TH[i]) extinguishCandle(i);
          if (!out[i]) {
            lit++;
            const wob = Math.sin(t / 55 + i * 1.7) * 5 * p;
            if (lean[i]) {
              lean[i].setAttribute('transform', `rotate(${(p * 34 + wob).toFixed(2)}) scale(${(1 - p * 0.22).toFixed(3)} ${(1 - p * 0.4).toFixed(3)})`);
            }
          }
        }
        if (glow) glow.style.opacity = (0.25 + 0.75 * (lit / 5) * (1 - p * 0.25)).toFixed(2);
        if (lit === 0) finishBlowing();

        // Breath particles
        if (holding && Math.random() < dt * 45) {
          const a = relPos(pill);
          const c = relPos(cakeEl);
          const dur = 0.85;
          const ox = a.x + a.w / 2 + (Math.random() - 0.5) * 50;
          const oy = a.y;
          const tx = c.x + c.w / 2 + (Math.random() - 0.5) * 80;
          const ty = c.y + c.h * 0.25;
          parts.push({ k: 'b', x: ox, y: oy, vx: (tx - ox) / dur, vy: (ty - oy) / dur, r0: 4, life: dur + Math.random() * 0.25, age: 0 });
        }
      }

      if (pill) pill.style.setProperty('--p', done ? 0 : p.toFixed(3));

      // Draw particle layer
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      ctx.clearRect(0, 0, W, Hh);
      parts = parts.filter(q => (q.age += dt) < q.life && q.y < Hh + 20);
      for (const q of parts) {
        q.x += q.vx * dt;
        q.y += q.vy * dt;
        if (q.k === 'b') {
          const k = q.age / q.life;
          ctx.globalAlpha = 0.3 * (1 - k);
          ctx.fillStyle = '#ffffff';
          ctx.beginPath();
          ctx.arc(q.x, q.y, q.r0 + k * 22, 0, Math.PI * 2);
          ctx.fill();
        } else {
          q.vy += 850 * dt;
          q.vx *= 0.992;
          q.r += q.vr * dt;
          ctx.globalAlpha = Math.min(1, (q.life - q.age) * 2);
          ctx.save();
          ctx.translate(q.x, q.y);
          ctx.rotate(q.r);
          ctx.fillStyle = q.col;
          ctx.fillRect(-q.w / 2, -q.h / 2, q.w, q.h);
          ctx.restore();
        }
      }
      ctx.globalAlpha = 1;
      requestAnimationFrame(candleFrame);
    }
    requestAnimationFrame(candleFrame);
  }

  // Initialize Candle Engine
  initCandleSlideEngine();"""

    html = re.sub(old_engine_pattern, clean_engine, html)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated clean_candle_engine in both files!")
