import re

for fname in ['step6.html', 'review.html']:
    path = f'/Users/neelamvishwanatham/Documents/saybyme-birthday/{fname}'
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Remove the broken btn-phone-next listener
    html = re.sub(
        r'// Button bindings\s*document\.getElementById\(\'btn-phone-next\'\)\.addEventListener\(\'click\',\s*\(\)\s*=>\s*\{[\s\S]*?\}\);\s*',
        '',
        html
    )

    # 2. Add inline onclick to the button and gift box
    html = html.replace(
        '<button class="btn-tap-open-main" id="btn-phone-open-action" type="button">',
        '<button class="btn-tap-open-main" id="btn-phone-open-action" type="button" onclick="openGiftBox()">'
    )
    html = html.replace(
        '<div class="gift-box-interactive" id="gift-box-interactive" title="Click to open surprise!">',
        '<div class="gift-box-interactive" id="gift-box-interactive" title="Click to open surprise!" onclick="openGiftBox()">'
    )

    # 3. Add safety checks for back and continue buttons
    safe_buttons_js = """
  // Back to Edit button: Return to step5.html
  const backEditBtn = document.getElementById('btn-back-edit');
  if (backEditBtn) {
    backEditBtn.addEventListener('click', () => {
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
  }

  // Continue button: Navigate to surprise.html
  const continueBtn = document.getElementById('btn-continue');
  if (continueBtn) {
    continueBtn.addEventListener('click', () => {
      const query = new URLSearchParams({
        from: fromName,
        to: toName,
        rel: rel,
        date: date,
        msg: msg,
        features: features
      });
      window.location.href = 'surprise.html?' + query.toString();
    });
  }
"""
    html = re.sub(
        r'// Back to Edit button[\s\S]*?window\.location\.href = \'surprise\.html\?\' \+ query\.toString\(\);\s*\}\);',
        safe_buttons_js.strip(),
        html
    )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

print("Fixed click bindings in step6.html and review.html!")
