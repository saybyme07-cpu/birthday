import re

clean_step6_html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>SayByMe – Your Birthday Surprise is Ready! 🎂💖</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Caveat:wght@500;600;700&family=Kaushan+Script&family=Nunito:wght@400;500;600;700;800&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --plum: #7a1646;
    --rose: #e8236f;
    --rose-dark: #a01b4e;
    --rose-deep: #5a1032;
    --pink-1: #fde3ee;
    --pink-2: #f9c9dd;
    --pink-light: #fff0f6;
    --pink-tag: #ffeaf2;
    --ink: #3d1630;
    --text-muted: #6d3852;
    --card-bg: #ffffff;
    --shadow-card: 0 16px 40px rgba(160, 27, 78, 0.08);
    --shadow-phone: 0 24px 60px rgba(160, 27, 78, 0.22);
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { min-height: 100%; }
  body {
    font-family: 'Nunito', system-ui, -apple-system, sans-serif;
    color: var(--ink);
    background:
      radial-gradient(ellipse at 25% 20%, #fff2f7 0%, transparent 55%),
      radial-gradient(ellipse at 80% 65%, #fbd8e8 0%, transparent 60%),
      linear-gradient(160deg, #fde8f2 0%, #f7cde1 100%);
    min-height: 100vh;
    overflow-x: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
  }

  .stage {
    position: relative;
    min-height: 100vh;
    width: 100%;
    max-width: 1380px;
    margin: 0 auto;
    display: flex;
    flex-direction: column;
    padding: 16px 28px 24px;
    z-index: 5;
  }

  /* Floating heart petals */
  .floating-heart {
    position: absolute;
    pointer-events: none;
    z-index: 1;
    color: #e8236f;
    opacity: 0.45;
    animation: floatHeart 6s ease-in-out infinite alternate;
  }
  @keyframes floatHeart {
    0% { transform: translateY(0) scale(1) rotate(0deg); }
    100% { transform: translateY(-16px) scale(1.08) rotate(12deg); }
  }

  /* ---------- Top Bar ---------- */
  .top-bar {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    margin-bottom: 4px;
  }
  .logo-wrap {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
  }
  .logo-heart {
    width: 24px;
    height: 24px;
    color: var(--rose);
  }
  .logo-text {
    font-family: 'Outfit', sans-serif;
    font-size: 22px;
    font-weight: 800;
    color: var(--rose-deep);
    letter-spacing: -0.3px;
  }
  .top-quote {
    font-family: 'Caveat', cursive;
    font-size: 20px;
    color: var(--rose-dark);
    line-height: 1.15;
    text-align: right;
    position: relative;
    font-weight: 600;
  }
  .top-quote .underline-squiggle {
    position: absolute;
    bottom: -6px;
    right: 0;
    width: 70px;
    height: 4px;
  }

  /* ---------- Header Title ---------- */
  .header-center {
    text-align: center;
    margin: 4px auto 20px;
    max-width: 800px;
  }
  h1 {
    font-family: 'Kaushan Script', cursive;
    font-size: clamp(30px, 3.2vw, 44px);
    color: var(--rose-dark);
    font-weight: 400;
    margin-bottom: 6px;
    line-height: 1.15;
    display: inline-flex;
    align-items: center;
    gap: 10px;
    flex-wrap: wrap;
    justify-content: center;
  }
  .sub {
    font-size: clamp(14px, 1.05vw, 16px);
    color: var(--text-muted);
    font-weight: 600;
    max-width: 650px;
    margin: 0 auto;
  }

  /* ---------- Two Column Layout ---------- */
  .main-layout {
    display: grid;
    grid-template-columns: 430px 1fr;
    gap: 40px;
    align-items: center;
    justify-content: center;
    width: 100%;
    max-width: 1180px;
    margin: 0 auto 10px;
    z-index: 10;
  }

  /* ========== Left Column: Authentic iPhone Mockup ========== */
  .phone-container {
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 10px 0;
  }
  .phone-mockup {
    width: 350px;
    height: 690px;
    background: #111114;
    border-radius: 52px;
    position: relative;
    box-shadow:
      0 0 0 2px #3e3e46,
      0 0 0 4px #1c1c20,
      0 28px 65px rgba(160, 27, 78, 0.22);
    border: 3.5px solid #2c2c34;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* iPhone Physical Buttons on side edges */
  .phone-mockup::before {
    content: '';
    position: absolute;
    left: -7px;
    top: 105px;
    width: 4px;
    height: 28px;
    background: #383842;
    border-radius: 3px 0 0 3px;
    box-shadow:
      0 42px 0 #383842,
      0 58px 0 #383842,
      0 102px 0 #383842;
  }
  .phone-mockup::after {
    content: '';
    position: absolute;
    right: -7px;
    top: 155px;
    width: 4px;
    height: 68px;
    background: #383842;
    border-radius: 0 3px 3px 0;
  }

  .phone-screen {
    width: calc(100% - 10px);
    height: calc(100% - 10px);
    background: radial-gradient(ellipse at 50% 25%, #fff7fa 0%, #fdf0f4 55%, #fce3ee 100%);
    border-radius: 44px;
    overflow: hidden;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: inset 0 0 6px rgba(0, 0, 0, 0.08);
    border: 5px solid #000000;
    padding: 42px 18px 20px;
    text-align: center;
  }

  /* Floating Dynamic Island inside screen */
  .dynamic-island {
    position: absolute;
    top: 14px;
    left: 50%;
    transform: translateX(-50%);
    width: 82px;
    height: 20px;
    background: #000000;
    border-radius: 999px;
    z-index: 45;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.18);
  }

  /* iOS Home Indicator Bar */
  .phone-home-indicator {
    position: absolute;
    bottom: 6px;
    left: 50%;
    transform: translateX(-50%);
    width: 110px;
    height: 4px;
    background: #111111;
    border-radius: 999px;
    z-index: 40;
    pointer-events: none;
  }

  /* Phone Screen Top Header */
  .phone-screen-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 4px;
    z-index: 20;
  }
  .phone-gift-icon-wrap {
    width: 44px;
    height: 44px;
    border-radius: 50%;
    background: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 4px 12px rgba(232, 35, 111, 0.15);
    margin-bottom: 8px;
    transition: transform 0.25s ease;
  }
  .phone-gift-icon-wrap:hover {
    transform: scale(1.1) rotate(6deg);
  }
  .phone-main-heading {
    font-family: 'Outfit', system-ui, sans-serif;
    font-size: 23px;
    font-weight: 800;
    color: #4a122e;
    margin: 0;
    line-height: 1.2;
    letter-spacing: -0.2px;
  }
  .phone-sub-heading {
    font-size: 15px;
    font-weight: 600;
    color: #72425b;
    margin-top: 2px;
  }
  .phone-divider-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    margin: 6px auto;
    width: 140px;
  }
  .p-div-line {
    flex-grow: 1;
    height: 1px;
    background: #e3a5be;
  }
  .p-div-heart {
    color: var(--rose);
    font-size: 10px;
    line-height: 1;
  }
  .phone-for-row {
    font-size: 16px;
    font-weight: 600;
    color: #6b3f55;
    margin-top: 1px;
  }
  .phone-recipient-highlight {
    font-family: 'Kaushan Script', cursive;
    color: var(--rose);
    font-size: 21px;
    font-weight: 700;
    margin-left: 3px;
  }

  /* Phone Gift Box Center */
  .phone-gift-stage {
    position: relative;
    width: 250px;
    height: 250px;
    margin: 10px auto;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .phone-gift-stage:hover {
    transform: scale(1.04);
  }
  .phone-gift-stage img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    filter: drop-shadow(0 14px 24px rgba(160, 27, 78, 0.18));
    animation: gentleFloat 4s ease-in-out infinite alternate;
  }
  @keyframes gentleFloat {
    0% { transform: translateY(0); }
    100% { transform: translateY(-7px); }
  }

  /* Tap to Open main pill button */
  .btn-tap-open-main {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    width: 84%;
    max-width: 260px;
    padding: 14px 26px;
    margin: 0 auto 10px;
    background: linear-gradient(90deg, #e8236f 0%, #b3124d 100%);
    border: none;
    border-radius: 999px;
    font-family: inherit;
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 8px 24px rgba(232, 35, 111, 0.42);
    transition: all 0.24s cubic-bezier(0.34, 1.56, 0.64, 1);
    z-index: 25;
  }
  .btn-tap-open-main:hover {
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 12px 30px rgba(232, 35, 111, 0.55);
  }
  .btn-arrow {
    font-size: 18px;
    transition: transform 0.2s ease;
  }
  .btn-tap-open-main:hover .btn-arrow {
    transform: translateX(4px);
  }

  /* Bottom Sound Toggle */
  .phone-bottom-bar {
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 6px;
    z-index: 25;
  }
  .btn-phone-sound {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.9);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 14px;
    color: var(--rose-dark);
    cursor: pointer;
    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.08);
    transition: transform 0.2s ease;
  }
  .btn-phone-sound:hover {
    transform: scale(1.08);
  }

  /* ========== Right Column: Confirmation Card ========== */
  .review-card {
    background: var(--card-bg);
    border: 1.5px solid #f6d5e3;
    border-radius: 28px;
    padding: 28px 32px;
    box-shadow: var(--shadow-card);
    display: flex;
    flex-direction: column;
    position: relative;
  }

  /* Card Header */
  .card-header-row {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 20px;
  }
  .card-gift-icon {
    font-size: 26px;
    line-height: 1;
  }
  .card-main-title {
    font-size: 24px;
    font-weight: 800;
    color: var(--rose-deep);
  }

  /* Metadata Rows */
  .meta-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-bottom: 18px;
  }
  .meta-item {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .meta-label {
    font-size: 15px;
    font-weight: 700;
    color: #8b5574;
  }
  .meta-pill {
    background: var(--pink-tag);
    color: var(--rose-dark);
    font-size: 14.5px;
    font-weight: 700;
    padding: 4px 14px;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    gap: 6px;
  }

  /* Dashed Divider */
  .dashed-divider {
    border-bottom: 1.5px dashed #f0c5d7;
    margin: 18px 0;
    width: 100%;
  }

  /* Section Title with round icon */
  .sec-heading {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 16px;
    font-weight: 800;
    color: var(--rose-deep);
    margin-bottom: 14px;
  }
  .sec-icon-badge {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 1.5px solid var(--rose);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    color: var(--rose);
    font-weight: 800;
  }

  /* Included Features 4 Mini Cards */
  .mini-cards-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 12px;
  }
  .mini-card {
    background: #fff5f9;
    border: 1.5px solid #f9d1e2;
    border-radius: 16px;
    padding: 10px 8px 12px;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    position: relative;
    box-shadow: 0 4px 12px rgba(160, 27, 78, 0.04);
    transition: all 0.2s ease;
  }
  .mini-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 16px rgba(160, 27, 78, 0.1);
  }
  .mini-card-check {
    position: absolute;
    top: 6px;
    right: 6px;
    width: 18px;
    height: 18px;
    border-radius: 50%;
    background: var(--rose);
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 10px;
    font-weight: 800;
    box-shadow: 0 2px 6px rgba(232, 35, 111, 0.35);
  }
  .mini-card-img {
    width: 58px;
    height: 58px;
    border-radius: 12px;
    object-fit: cover;
    margin-bottom: 8px;
    background: #ffffff;
  }
  .mini-card-label {
    font-size: 12px;
    font-weight: 700;
    color: var(--ink);
    line-height: 1.3;
  }

  /* Experience Flow sequence */
  .flow-row {
    display: flex;
    align-items: center;
    justify-content: flex-start;
    gap: 10px;
    flex-wrap: wrap;
  }
  .flow-step {
    display: flex;
    align-items: center;
    gap: 8px;
    cursor: pointer;
    transition: transform 0.2s ease;
  }
  .flow-step:hover {
    transform: scale(1.05);
  }
  .flow-badge {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    background: var(--rose-dark);
    color: #ffffff;
    font-size: 12px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .flow-text {
    font-size: 14px;
    font-weight: 700;
    color: var(--ink);
  }
  .flow-arrow {
    color: #e09fb9;
    font-size: 16px;
    font-weight: 700;
  }

  /* Bottom Actions under review card */
  .action-buttons-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin-top: 24px;
    width: 100%;
  }
  .btn-back-edit {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 13px 32px;
    background: #ffffff;
    border: 1.8px solid var(--rose-dark);
    border-radius: 999px;
    font-family: inherit;
    font-size: 15px;
    font-weight: 700;
    color: var(--rose-dark);
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 4px 14px rgba(160, 27, 78, 0.08);
    transition: all 0.22s ease;
  }
  .btn-back-edit:hover {
    background: #fff0f6;
    transform: translateY(-2px);
    box-shadow: 0 6px 18px rgba(160, 27, 78, 0.14);
  }
  .btn-continue {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 14px 44px;
    background: linear-gradient(90deg, #e8236f 0%, #a01b4e 100%);
    border: none;
    border-radius: 999px;
    font-family: inherit;
    font-size: 16px;
    font-weight: 700;
    color: #ffffff;
    cursor: pointer;
    text-decoration: none;
    box-shadow: 0 8px 24px rgba(232, 35, 111, 0.38);
    transition: all 0.24s cubic-bezier(0.34, 1.56, 0.64, 1);
  }
  .btn-continue:hover {
    transform: translateY(-3px) scale(1.02);
    box-shadow: 0 12px 30px rgba(232, 35, 111, 0.48);
  }

  /* Responsive styles */
  @media (max-width: 1024px) {
    .main-layout {
      grid-template-columns: 1fr;
      justify-items: center;
      gap: 30px;
    }
    .review-card {
      max-width: 540px;
      width: 100%;
    }
  }

  @media (max-width: 600px) {
    .stage {
      padding: 12px 14px 20px;
    }
    .phone-mockup {
      width: 100%;
      max-width: 340px;
      height: 620px;
      padding: 6px;
    }
    .mini-cards-grid {
      grid-template-columns: repeat(2, 1fr);
    }
    .action-buttons-wrap {
      flex-direction: column-reverse;
      gap: 12px;
    }
    .btn-back-edit, .btn-continue {
      width: 100%;
      justify-content: center;
    }
  }
</style>
</head>
<body>

<!-- Floating Hearts -->
<div class="floating-heart" style="top:20%; left:5%; font-size:24px;">♥</div>
<div class="floating-heart" style="top:42%; left:4%; font-size:18px; animation-delay:1.5s;">♥</div>
<div class="floating-heart" style="top:72%; left:7%; font-size:22px; animation-delay:2.5s;">♥</div>
<div class="floating-heart" style="top:22%; right:6%; font-size:20px; animation-delay:1s;">♥</div>
<div class="floating-heart" style="top:68%; right:5%; font-size:24px; animation-delay:2s;">♥</div>

<div class="stage">
  <!-- Top Bar -->
  <header class="top-bar">
    <div class="logo-wrap">
      <svg class="logo-heart" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
        <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
      </svg>
      <span class="logo-text">SayByMe</span>
    </div>
    <div class="top-quote">
      Small things...<br>Big emotions...
      <svg class="underline-squiggle" viewBox="0 0 100 10" preserveAspectRatio="none">
        <path d="M0,6 Q25,1 50,6 T100,6" fill="none" stroke="#e8236f" stroke-width="2.5" stroke-linecap="round"/>
      </svg>
    </div>
  </header>

  <!-- Title section -->
  <div class="header-center">
    <h1>Your Birthday Surprise is Ready! 🎂💖</h1>
    <p class="sub">Here's a quick preview of what they will see. Tap through the experience and continue when you're happy.</p>
  </div>

  <!-- Two Column Main Layout -->
  <main class="main-layout">
    <!-- Left Column: Realistic Interactive Phone Mockup -->
    <div class="phone-container">
      <div class="phone-mockup">
        <div class="phone-screen">
          <!-- Sleek Floating Dynamic Island inside screen -->
          <div class="dynamic-island"></div>
          <!-- iOS Home Indicator Bar -->
          <div class="phone-home-indicator"></div>

          <!-- Top Header matching user screenshot -->
          <div class="phone-screen-header">
            <div class="phone-gift-icon-wrap">
              <svg viewBox="0 0 24 24" width="28" height="28" fill="none" stroke="#e8236f" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 12 20 22 4 22 4 12"></polyline>
                <rect x="2" y="7" width="20" height="5"></rect>
                <line x1="12" y1="22" x2="12" y2="7"></line>
                <path d="M12 7H7.5a2.5 2.5 0 0 1 0-5C11 2 12 7 12 7z"></path>
                <path d="M12 7h4.5a2.5 2.5 0 0 0 0-5C13 2 12 7 12 7z"></path>
              </svg>
            </div>

            <h2 class="phone-main-heading">A Birthday Surprise</h2>
            <div class="phone-sub-heading">is Waiting for You!</div>

            <div class="phone-divider-row">
              <span class="p-div-line"></span>
              <span class="p-div-heart">♥</span>
              <span class="p-div-line"></span>
            </div>

            <div class="phone-for-row">
              For <span class="phone-recipient-highlight" id="phone-recipient-text">Sanjana</span>
            </div>
          </div>

          <!-- 3D Gift Box (Clicking opens or goes directly to candle.html) -->
          <div class="phone-gift-stage" id="phone-gift-box" title="Tap to open surprise!">
            <img src="assets/gift_box_perfect.png" alt="Birthday Gift Box">
          </div>

          <!-- Tap to Open Button: Goes directly to candle.html! -->
          <button class="btn-tap-open-main" id="btn-tap-to-open" type="button">
            <span>Tap to Open</span>
            <span class="btn-arrow">→</span>
          </button>

          <!-- Bottom Sound Toggle -->
          <div class="phone-bottom-bar">
            <button class="btn-phone-sound" id="btn-sound-toggle" aria-label="Toggle Sound" type="button">
              🔊
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Right Column: Review Details Card -->
    <div class="review-column">
      <div class="review-card">
        <!-- Card Header -->
        <div class="card-header-row">
          <span class="card-gift-icon">🎁</span>
          <h2 class="card-main-title">Your Surprise</h2>
        </div>

        <!-- Metadata Rows -->
        <div class="meta-list">
          <div class="meta-item">
            <span class="meta-label">From</span>
            <span class="meta-pill" id="meta-from">You</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">For</span>
            <span class="meta-pill" id="meta-to">Sanjana</span>
          </div>
          <div class="meta-item">
            <span class="meta-label">Occasion</span>
            <span class="meta-pill">Birthday 🎂</span>
          </div>
        </div>

        <!-- Dashed Divider -->
        <div class="dashed-divider"></div>

        <!-- Included in this Surprise Section -->
        <div class="sec-heading">
          <div class="sec-icon-badge">★</div>
          <span>Included in this Surprise</span>
        </div>
        <div class="mini-cards-grid">
          <!-- Mini Card 1 -->
          <div class="mini-card" onclick="goToCandlePage()" style="cursor: pointer;" title="Preview Blow Out the Candles">
            <div class="mini-card-check">✓</div>
            <img src="assets/feature_candles.jpg" alt="Blow Out the Candles" class="mini-card-img">
            <span class="mini-card-label">Blow Out the Candles</span>
          </div>

          <!-- Mini Card 2 -->
          <div class="mini-card">
            <div class="mini-card-check">✓</div>
            <img src="assets/feature_cake_slice.jpg" alt="Cut the Cake" class="mini-card-img">
            <span class="mini-card-label">Cut the Cake</span>
          </div>

          <!-- Mini Card 3 -->
          <div class="mini-card">
            <div class="mini-card-check">✓</div>
            <img src="assets/feature_celebration.jpg" alt="Celebration" class="mini-card-img">
            <span class="mini-card-label">Celebration</span>
          </div>

          <!-- Mini Card 4 -->
          <div class="mini-card">
            <div class="mini-card-check">✓</div>
            <img src="assets/feature_letter.jpg" alt="Personal Letter" class="mini-card-img">
            <span class="mini-card-label">Personal Letter</span>
          </div>
        </div>

        <!-- Dashed Divider -->
        <div class="dashed-divider"></div>

        <!-- Experience Flow Section -->
        <div class="sec-heading">
          <div class="sec-icon-badge">▷</div>
          <span>Experience Flow</span>
        </div>
        <div class="flow-row">
          <div class="flow-step" onclick="goToCandlePage()" title="Blow Out Candles">
            <div class="flow-badge">1</div>
            <span class="flow-text">Candles</span>
          </div>
          <span class="flow-arrow">→</span>
          <div class="flow-step">
            <div class="flow-badge">2</div>
            <span class="flow-text">Cake</span>
          </div>
          <span class="flow-arrow">→</span>
          <div class="flow-step">
            <div class="flow-badge">3</div>
            <span class="flow-text">Celebration</span>
          </div>
          <span class="flow-arrow">→</span>
          <div class="flow-step">
            <div class="flow-badge">4</div>
            <span class="flow-text">Letter</span>
          </div>
        </div>
      </div>

      <!-- Action Buttons below the Card -->
      <div class="action-buttons-wrap">
        <button class="btn-back-edit" id="btn-back-edit" type="button">
          <span>←</span> Back to Edit
        </button>
        <button class="btn-continue" id="btn-continue" type="button">
          Continue <span>→</span>
        </button>
      </div>
    </div>
  </main>
</div>

<script>
  // Parse query parameters
  const params = new URLSearchParams(window.location.search);
  const fromName = params.get('from') || 'Rohan';
  const toName = params.get('to') || 'Sanjana';
  const rel = params.get('rel') || 'Girlfriend';
  const date = params.get('date') || '';
  const msg = params.get('msg') || '';
  const features = params.get('features') || 'candles,cake,celebration';

  // Populate metadata fields
  document.getElementById('meta-from').textContent = fromName || 'You';
  document.getElementById('meta-to').textContent = toName || 'Sanjana';

  const phoneRecipient = document.getElementById('phone-recipient-text');
  if (phoneRecipient && toName) {
    phoneRecipient.textContent = toName;
  }

  // Navigation function: GO TO CANDLE ANIMATION PAGE!
  function goToCandlePage() {
    const query = new URLSearchParams({
      from: fromName,
      to: toName,
      rel: rel,
      date: date,
      msg: msg,
      features: features
    });
    window.location.href = 'candle.html?' + query.toString();
  }

  // When clicking "Tap to Open" on phone screen -> Go to candle page!
  document.getElementById('btn-tap-to-open').addEventListener('click', goToCandlePage);
  document.getElementById('phone-gift-box').addEventListener('click', goToCandlePage);

  // When clicking "Continue" on review card -> Go to candle page!
  document.getElementById('btn-continue').addEventListener('click', goToCandlePage);

  // Back to Edit button: Return to step5.html
  document.getElementById('btn-back-edit').addEventListener('click', () => {
    const query = new URLSearchParams({
      from: fromName,
      to: toName,
      rel: rel,
      date: date,
      msg: msg,
      features: features
    });
    window.location.href = 'step5.html?' + query.toString();
  });

  // Sound toggle button in phone
  let soundOn = true;
  const soundBtn = document.getElementById('btn-sound-toggle');
  if (soundBtn) {
    soundBtn.addEventListener('click', () => {
      soundOn = !soundOn;
      soundBtn.textContent = soundOn ? '🔊' : '🔇';
    });
  }
</script>
</body>
</html>
"""

for fname in ['step6.html', 'review.html']:
    with open(f'/Users/neelamvishwanatham/Documents/saybyme-birthday/{fname}', 'w', encoding='utf-8') as f:
        f.write(clean_step6_html)

print("step6.html and review.html cleanly rewritten!")
