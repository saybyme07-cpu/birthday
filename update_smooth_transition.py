import re

for fname in ['step6.html', 'review.html']:
    path = f'/Users/neelamvishwanatham/Documents/saybyme-birthday/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Move .phone-screen-header inside Slide 0
    # Find from <div class="phone-content"> to <!-- Slide 1:
    old_content_pattern = r'<div class="phone-content">\s*<!-- Top Header matching user screenshot -->\s*<div class="phone-screen-header">[\s\S]*?</div>\s*<!-- Slides: Can be tapped through -->\s*<div class="phone-slides-wrap">\s*<!-- Slide 0: Interactive Dynamic Opening Gift Box -->\s*<div class="phone-slide active" data-slide="0">'

    # New layout: phone-content contains phone-slides-wrap, and Slide 0 contains phone-screen-header
    new_content_start = """<div class="phone-content">
            <!-- Slides Container -->
            <div class="phone-slides-wrap">
              <!-- Slide 0: Interactive Dynamic Opening Gift Box -->
              <div class="phone-slide active" data-slide="0" id="gift-slide">
                <!-- Top Header for Gift Box Slide -->
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
                </div>"""

    if re.search(old_content_pattern, html):
        html = re.sub(old_content_pattern, new_content_start, html)
        print(f"Moved header inside Slide 0 in {fname}")
    else:
        print(f"Could not find exact pattern in {fname}, trying manual adjustment...")

    # 2. Update CSS for .phone-content and .phone-slides-wrap and .phone-slide
    # Ensure each slide takes 100% of the phone height and width
    slide_css = """
  .phone-content {
    position: relative;
    z-index: 15;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    padding: 0;
    overflow: hidden;
  }
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
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-between;
    padding: 38px 16px 20px;
    opacity: 0;
    pointer-events: none;
    transform: scale(0.96);
    transition: opacity 0.35s ease, transform 0.35s ease;
  }
  .phone-slide.active {
    opacity: 1;
    pointer-events: auto;
    transform: scale(1);
    z-index: 10;
  }
"""
    # Replace existing .phone-content and .phone-slides-wrap styles
    html = re.sub(r'\.phone-content \{[\s\S]*?\.phone-slide\.active \{[\s\S]*?\}', slide_css.strip(), html)

    # 3. Update openGiftBox logic so clicking gift or Tap to Open immediately opens box AND transitions to Slide 1!
    open_box_js = """
  let isNavigatingToSlide1 = false;
  function openGiftBox() {
    if (isNavigatingToSlide1) return;

    // Step 1: Wobble anticipation
    giftStage.classList.add('wobbling');
    setTimeout(() => {
      giftStage.classList.remove('wobbling');
      // Step 2: Open lid & burst magic
      giftStage.classList.add('is-open');
      isBoxOpen = true;
      playMagicChime();
      triggerBoxConfetti();

      // Step 3: Update button label
      openActionLabel.textContent = 'Opening Surprise...';
      openActionBtn.classList.add('opened-mode');

      // Step 4: Automatically transition smoothly to Slide 1 (Make a Wish & Blow Candles!)
      isNavigatingToSlide1 = true;
      setTimeout(() => {
        goToSlide(1);
        isNavigatingToSlide1 = false;
      }, 950);
    }, 280);
  }
"""
    html = re.sub(r'function openGiftBox\(\) \{[\s\S]*?\}\n\n  function closeGiftBox', open_box_js.strip() + '\n\n  function closeGiftBox', html)

    # 4. Enhance goToSlide to resize candle canvas and trigger animations
    goto_slide_js = """
  function goToSlide(index) {
    currentSlide = index;
    slides.forEach((s, idx) => {
      s.classList.toggle('active', idx === index);
    });

    // If navigating to Candle Slide (Slide 1), ensure canvas is resized and active
    if (index === 1 && typeof window.resizeCandleCanvas === 'function') {
      setTimeout(window.resizeCandleCanvas, 50);
    }
  }
"""
    html = re.sub(r'function goToSlide\(index\) \{[\s\S]*?\}\n\n  document\.getElementById', goto_slide_js.strip() + '\n\n  // Button bindings\n  document.getElementById', html)

    # 5. Expose resizeCandleCanvas globally inside initCandleSlideEngine
    html = html.replace('function resizeCanvas() {', 'window.resizeCandleCanvas = function() {\n      const slide = document.getElementById("candle-slide");\n      if (!slide) return;')

    # 6. Add click handler on Experience Flow steps in the review card to jump directly to preview slides
    flow_steps_js = """
  // Allow clicking on Experience Flow badges to preview that slide
  const flowSteps = document.querySelectorAll('.flow-step');
  flowSteps.forEach((st, idx) => {
    st.style.cursor = 'pointer';
    st.title = `Preview step ${idx + 1}`;
    st.addEventListener('click', () => {
      goToSlide(idx + 1);
    });
  });
"""
    html = html.replace('// Dynamic Gift Box Opening Logic', flow_steps_js + '\n  // Dynamic Gift Box Opening Logic')

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Both step6.html and review.html updated successfully!")
