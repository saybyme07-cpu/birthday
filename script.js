/**
 * SayByMe - Birthday Edition
 * Interactive celebration web application
 */

// State
const state = {
  recipient: 'Celebrant',
  sender: 'Your Best Friend',
  message: '',
  candlesLit: 3,
  isPlayingMusic: false,
  audioCtx: null
};

// Birthday Melody Notes & Durations (Happy Birthday to You)
// frequencies in Hz
const NOTES = {
  C4: 261.63,
  D4: 293.66,
  E4: 329.63,
  F4: 349.23,
  G4: 392.00,
  A4: 440.00,
  B4: 493.88,
  C5: 523.25,
  D5: 587.33,
  E5: 659.25,
  F5: 698.46
};

const BIRTHDAY_TUNE = [
  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.D4, duration: 0.6, rest: 0.1 },
  { note: NOTES.C4, duration: 0.6, rest: 0.1 },
  { note: NOTES.F4, duration: 0.6, rest: 0.1 },
  { note: NOTES.E4, duration: 1.0, rest: 0.3 },

  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.D4, duration: 0.6, rest: 0.1 },
  { note: NOTES.C4, duration: 0.6, rest: 0.1 },
  { note: NOTES.G4, duration: 0.6, rest: 0.1 },
  { note: NOTES.F4, duration: 1.0, rest: 0.3 },

  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.C4, duration: 0.3, rest: 0.1 },
  { note: NOTES.C5, duration: 0.6, rest: 0.1 },
  { note: NOTES.A4, duration: 0.6, rest: 0.1 },
  { note: NOTES.F4, duration: 0.6, rest: 0.1 },
  { note: NOTES.E4, duration: 0.6, rest: 0.1 },
  { note: NOTES.D4, duration: 0.8, rest: 0.3 },

  { note: NOTES.B4, duration: 0.3, rest: 0.1 },
  { note: NOTES.B4, duration: 0.3, rest: 0.1 },
  { note: NOTES.A4, duration: 0.6, rest: 0.1 },
  { note: NOTES.F4, duration: 0.6, rest: 0.1 },
  { note: NOTES.G4, duration: 0.6, rest: 0.1 },
  { note: NOTES.F4, duration: 1.2, rest: 0.6 }
];

// Balloon Compliment Messages
const BALLOON_WISHES = [
  "✨ Your smile lights up every room!",
  "💖 Wishing you 365 days of nonstop joy!",
  "🎂 May all your secret wishes come true!",
  "🌟 Keep shining bright, you absolute legend!",
  "🎉 Another fabulous chapter starts today!",
  "🚀 May this year take you to incredible heights!",
  "🍰 More cake, more laughter, more memories!"
];

const BALLOON_COLORS = ['#ff758f', '#ffb3c1', '#ffd166', '#a2d2ff', '#bde0fe', '#cdb4db', '#ffc6ff'];

// Sound Synthesizer via Web Audio API
function getAudioContext() {
  if (!state.audioCtx) {
    const AudioContextClass = window.AudioContext || window.webkitAudioContext;
    state.audioCtx = new AudioContextClass();
  }
  if (state.audioCtx.state === 'suspended') {
    state.audioCtx.resume();
  }
  return state.audioCtx;
}

function playNote(freq, duration, type = 'sine', gainVal = 0.25) {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();

    osc.type = type;
    osc.frequency.setValueAtTime(freq, ctx.currentTime);

    // Warm music box envelope
    gain.gain.setValueAtTime(gainVal, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);

    osc.connect(gain);
    gain.connect(ctx.destination);

    osc.start();
    osc.stop(ctx.currentTime + duration);
  } catch (e) {
    console.warn("Audio playback not allowed or not supported yet", e);
  }
}

// Chime effect
function playChime() {
  const notes = [523.25, 659.25, 783.99, 1046.50];
  notes.forEach((freq, idx) => {
    setTimeout(() => playNote(freq, 0.4, 'triangle', 0.2), idx * 80);
  });
}

// Pop sound effect
function playPop() {
  try {
    const ctx = getAudioContext();
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.type = 'triangle';
    osc.frequency.setValueAtTime(450, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(80, ctx.currentTime + 0.08);

    gain.gain.setValueAtTime(0.3, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.01, ctx.currentTime + 0.08);

    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.08);
  } catch (e) {}
}

let tuneTimeout = null;
let currentTuneIndex = 0;

function playBirthdayMelody() {
  if (!state.isPlayingMusic) return;

  const current = BIRTHDAY_TUNE[currentTuneIndex];
  playNote(current.note, current.duration, 'triangle', 0.18);

  const nextStepTime = (current.duration + current.rest) * 1000;
  currentTuneIndex = (currentTuneIndex + 1) % BIRTHDAY_TUNE.length;

  tuneTimeout = setTimeout(playBirthdayMelody, nextStepTime);
}

function toggleMusic() {
  const btn = document.getElementById('music-toggle-btn');
  const icon = btn.querySelector('.music-icon');
  const text = btn.querySelector('.music-text');

  if (state.isPlayingMusic) {
    state.isPlayingMusic = false;
    clearTimeout(tuneTimeout);
    icon.textContent = '🎵';
    text.textContent = 'Play Birthday Melody';
  } else {
    getAudioContext();
    state.isPlayingMusic = true;
    currentTuneIndex = 0;
    playBirthdayMelody();
    icon.textContent = '⏸️';
    text.textContent = 'Playing Melody';
  }
}

// High Performance Canvas Confetti
const canvas = document.getElementById('confetti-canvas');
const ctx = canvas.getContext('2d');
let particles = [];

function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener('resize', resizeCanvas);
resizeCanvas();

class ConfettiParticle {
  constructor(x, y, isExplosion = false) {
    this.x = x !== undefined ? x : Math.random() * canvas.width;
    this.y = y !== undefined ? y : -10;
    this.size = Math.random() * 8 + 6;
    this.colors = ['#ff007f', '#ff758f', '#ffb703', '#fb8500', '#8ecae6', '#219ebc', '#b5179e', '#7209b7'];
    this.color = this.colors[Math.floor(Math.random() * this.colors.length)];
    this.rotation = Math.random() * 360;
    this.rotSpeed = (Math.random() - 0.5) * 8;
    this.shape = Math.random() > 0.5 ? 'rect' : 'circle';

    if (isExplosion) {
      const angle = Math.random() * Math.PI * 2;
      const velocity = Math.random() * 12 + 4;
      this.vx = Math.cos(angle) * velocity;
      this.vy = Math.sin(angle) * velocity - 3;
      this.gravity = 0.25;
      this.drag = 0.96;
      this.opacity = 1;
      this.fade = Math.random() * 0.015 + 0.005;
    } else {
      this.vx = (Math.random() - 0.5) * 2;
      this.vy = Math.random() * 3 + 2;
      this.gravity = 0.03;
      this.drag = 0.99;
      this.opacity = 0.85;
      this.fade = 0;
    }
  }

  update() {
    this.vx *= this.drag;
    this.vy = (this.vy + this.gravity) * this.drag;
    this.x += this.vx;
    this.y += this.vy;
    this.rotation += this.rotSpeed;

    if (this.fade > 0) {
      this.opacity -= this.fade;
    }
  }

  draw() {
    ctx.save();
    ctx.translate(this.x, this.y);
    ctx.rotate((this.rotation * Math.PI) / 180);
    ctx.globalAlpha = Math.max(0, this.opacity);
    ctx.fillStyle = this.color;

    if (this.shape === 'rect') {
      ctx.fillRect(-this.size / 2, -this.size / 2, this.size, this.size * 1.4);
    } else {
      ctx.beginPath();
      ctx.arc(0, 0, this.size / 2, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }
}

function burstConfetti(count = 80, x = canvas.width / 2, y = canvas.height / 2) {
  for (let i = 0; i < count; i++) {
    particles.push(new ConfettiParticle(x, y, true));
  }
}

function loopConfetti() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  for (let i = particles.length - 1; i >= 0; i--) {
    const p = particles[i];
    p.update();
    p.draw();

    if (p.opacity <= 0 || p.y > canvas.height + 20) {
      particles.splice(i, 1);
    }
  }
  requestAnimationFrame(loopConfetti);
}
loopConfetti();

// Balloon Spawner
const balloonsContainer = document.getElementById('balloons-container');
let activeBalloonsCount = 0;

function createBalloon() {
  if (activeBalloonsCount > 8) return;

  const balloon = document.createElement('div');
  balloon.className = 'balloon';

  const color = BALLOON_COLORS[Math.floor(Math.random() * BALLOON_COLORS.length)];
  balloon.style.background = color;
  balloon.style.left = `${Math.random() * 88 + 4}%`;
  const duration = Math.random() * 8 + 10;
  balloon.style.animationDuration = `${duration}s`;

  balloon.innerHTML = `<span>🎈</span>`;

  balloon.addEventListener('click', (e) => {
    e.stopPropagation();
    popBalloon(balloon, e.clientX, e.clientY);
  });

  balloonsContainer.appendChild(balloon);
  activeBalloonsCount++;

  setTimeout(() => {
    if (balloon.parentNode) {
      balloon.remove();
      activeBalloonsCount--;
    }
  }, duration * 1000);
}

function popBalloon(balloonEl, x, y) {
  playPop();
  burstConfetti(25, x, y);

  const randomWish = BALLOON_WISHES[Math.floor(Math.random() * BALLOON_WISHES.length)];
  showToast(randomWish);

  balloonEl.remove();
  activeBalloonsCount--;
}

setInterval(createBalloon, 2500);

// Toast Notification
const toast = document.getElementById('toast');
let toastTimer = null;
function showToast(msg) {
  clearTimeout(toastTimer);
  toast.textContent = msg;
  toast.classList.add('show');
  toastTimer = setTimeout(() => {
    toast.classList.remove('show');
  }, 2600);
}

// Stage Navigation
function goToStage(stageId) {
  document.querySelectorAll('.stage-card').forEach(card => card.classList.remove('active'));
  const target = document.getElementById(stageId);
  if (target) {
    target.classList.add('active');
    target.scrollIntoView({ behavior: 'smooth', block: 'center' });
  }
}

// Candle Blowing Logic
const candles = document.querySelectorAll('.candle');
const cakeInstruction = document.getElementById('cake-instruction');
const blowAllBtn = document.getElementById('blow-all-btn');
const successBox = document.getElementById('cake-success-actions');

function extinguishCandle(candle) {
  if (candle.getAttribute('data-lit') === 'false') return;

  candle.setAttribute('data-lit', 'false');
  state.candlesLit--;

  const rect = candle.getBoundingClientRect();
  burstConfetti(18, rect.left + rect.width / 2, rect.top);
  playPop();

  if (state.candlesLit <= 0) {
    onAllCandlesExtinguished();
  } else {
    cakeInstruction.textContent = `${state.candlesLit} candle${state.candlesLit > 1 ? 's' : ''} left! Keep going ✨`;
  }
}

function onAllCandlesExtinguished() {
  cakeInstruction.style.display = 'none';
  blowAllBtn.style.display = 'none';
  successBox.classList.add('show');
  playChime();
  burstConfetti(120, canvas.width / 2, canvas.height * 0.4);

  // Play celebration melody if user hasn't already toggled it
  if (!state.isPlayingMusic) {
    toggleMusic();
  }
}

candles.forEach(candle => {
  candle.addEventListener('click', () => extinguishCandle(candle));
});

blowAllBtn.addEventListener('click', () => {
  candles.forEach(candle => extinguishCandle(candle));
});

// Gift Unboxing
const giftBox = document.getElementById('gift-box');
const giftPrompt = document.getElementById('gift-prompt');

giftBox.addEventListener('click', () => {
  giftBox.classList.add('opened');
  giftPrompt.textContent = "Unwrapped with love! ✨";
  playChime();
  burstConfetti(100, canvas.width / 2, canvas.height * 0.5);

  setTimeout(() => {
    goToStage('step-letter');
    burstConfetti(60, canvas.width / 2, canvas.height * 0.3);
  }, 1200);
});

// Personalization URL Params & Local State
function updateDOMNames() {
  document.querySelectorAll('.recipient-name').forEach(el => el.textContent = state.recipient);
  document.querySelectorAll('.sender-name').forEach(el => el.textContent = state.sender);
  if (state.message) {
    document.getElementById('letter-content').innerHTML = state.message.replace(/\n/g, '<br>');
  }
}

function loadFromURL() {
  const params = new URLSearchParams(window.location.search);
  const to = params.get('to');
  const from = params.get('from');
  const msg = params.get('msg');

  if (to) state.recipient = decodeURIComponent(to);
  if (from) state.sender = decodeURIComponent(from);
  if (msg) state.message = decodeURIComponent(msg);

  updateDOMNames();
}

// Modal handling
const modal = document.getElementById('customize-modal');
const customizeBtn = document.getElementById('customize-btn');
const closeBtn = document.getElementById('modal-close-btn');
const form = document.getElementById('customize-form');
const copyLinkBtn = document.getElementById('copy-custom-link-btn');

customizeBtn.addEventListener('click', () => {
  document.getElementById('input-recipient').value = state.recipient !== 'Celebrant' ? state.recipient : '';
  document.getElementById('input-sender').value = state.sender !== 'Your Best Friend' ? state.sender : '';
  document.getElementById('input-message').value = state.message;
  modal.classList.add('open');
});

closeBtn.addEventListener('click', () => modal.classList.remove('open'));
modal.addEventListener('click', (e) => {
  if (e.target === modal) modal.classList.remove('open');
});

form.addEventListener('submit', (e) => {
  e.preventDefault();
  const to = document.getElementById('input-recipient').value.trim();
  const from = document.getElementById('input-sender').value.trim();
  const msg = document.getElementById('input-message').value.trim();

  if (to) state.recipient = to;
  if (from) state.sender = from;
  if (msg) state.message = msg;

  updateDOMNames();
  modal.classList.remove('open');
  showToast('✨ Birthday surprise personalized!');
  burstConfetti(40);
});

copyLinkBtn.addEventListener('click', () => {
  const to = encodeURIComponent(document.getElementById('input-recipient').value.trim() || state.recipient);
  const from = encodeURIComponent(document.getElementById('input-sender').value.trim() || state.sender);
  const msg = encodeURIComponent(document.getElementById('input-message').value.trim() || state.message);

  const url = `${window.location.origin}${window.location.pathname}?to=${to}&from=${from}&msg=${msg}`;

  navigator.clipboard.writeText(url).then(() => {
    showToast('🔗 Link copied to clipboard!');
  }).catch(() => {
    showToast('Link generated in URL!');
    window.history.replaceState(null, '', `?to=${to}&from=${from}&msg=${msg}`);
  });
});

// Event Listeners for primary buttons
document.getElementById('btn-start-surprise').addEventListener('click', () => {
  goToStage('step-cake');
  burstConfetti(50);
});

document.getElementById('btn-next-gift').addEventListener('click', () => {
  goToStage('step-gift');
});

document.getElementById('music-toggle-btn').addEventListener('click', toggleMusic);

document.getElementById('btn-burst-confetti').addEventListener('click', () => {
  burstConfetti(140, canvas.width / 2, canvas.height * 0.4);
  playChime();
  showToast("🎆 Happy Birthday! Let's celebrate!");
});

document.getElementById('btn-replay').addEventListener('click', () => {
  state.candlesLit = 3;
  candles.forEach(c => c.setAttribute('data-lit', 'true'));
  cakeInstruction.style.display = 'block';
  cakeInstruction.textContent = "Tap the flames to blow them out! ✨";
  blowAllBtn.style.display = 'inline-block';
  successBox.classList.remove('show');
  giftBox.classList.remove('opened');
  giftPrompt.textContent = "Click the gift box to open!";
  goToStage('step-welcome');
});

document.getElementById('btn-share-modal').addEventListener('click', () => {
  customizeBtn.click();
});

// Init
window.addEventListener('DOMContentLoaded', () => {
  loadFromURL();
  burstConfetti(40, canvas.width / 2, 80);
});
