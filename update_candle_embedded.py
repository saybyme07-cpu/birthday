import re

with open('/Users/neelamvishwanatham/Documents/saybyme-birthday/candle.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add body.embedded styling so it fits inside an iframe with zero scrollbars or margins
embedded_css = """
  /* When inside iframe */
  body.embedded {
    background: transparent !important;
    width: 100% !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
  }
  body.embedded .screen {
    width: 100% !important;
    height: 100% !important;
    border-radius: 38px !important;
    box-shadow: none !important;
  }
"""

text = text.replace('</style>', embedded_css + '\n</style>')

# Update JS to detect iframe and handle back button
new_nav_js = """
  // Detect if inside iframe
  if (window.self !== window.top) {
    document.body.classList.add('embedded');
  }

  // Back button: if inside phone preview, smoothly switch back to gift
  $('#btn-back').addEventListener('click', (e) => {
    e.stopPropagation();
    try {
      if (window.parent && typeof window.parent.switchToGiftView === 'function') {
        window.parent.switchToGiftView();
        return;
      }
    } catch(err) {}
    location.href = 'step6.html?' + params.toString();
  });
"""

text = re.sub(
    r"// Back button returns to review step6\s*\$('#btn-back')\.addEventListener\('click', \(\) => \{[\s\S]*?\}\);",
    new_nav_js.strip(),
    text
)

with open('/Users/neelamvishwanatham/Documents/saybyme-birthday/candle.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated candle.html with embedded detection and seamless parent communication!")
