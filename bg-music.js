/**
 * SayByMe - Background Music Controller
 * Exact Circular Button UI matching design specs (Play/Mute SVG states)
 * Supports main floating button and preview phone sound toggle.
 */
(function() {
  // Prevent duplicate playback or duplicate fixed button inside iframes
  if (window.self !== window.top) {
    return;
  }

  // Resolve audio path relative to this script
  const scriptTag = document.currentScript;
  let basePath = '';
  if (scriptTag && scriptTag.src) {
    basePath = scriptTag.src.substring(0, scriptTag.src.lastIndexOf('/') + 1);
  }
  const AUDIO_SRC = basePath ? basePath + 'assets/sub_clair-happy-birthday-592177.mp3' : 'assets/sub_clair-happy-birthday-592177.mp3';
  const DEFAULT_VOLUME = 0.55;

  // Exact SVGs matching design
  const SVG_PLAYING = `
    <svg class="speaker-svg" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <!-- Speaker Horn Outline -->
      <path d="M13 6.8 L7.6 10.6 H4 C3.45 10.6 3 11.05 3 11.6 V16.4 C3 16.95 3.45 17.4 4 17.4 H7.6 L13 21.2 Z" 
            stroke="#671038" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <!-- Inner Wave -->
      <path d="M16.8 10.6 C18.1 11.6 18.8 12.7 18.8 14 C18.8 15.3 18.1 16.4 16.8 17.4" 
            stroke="#671038" stroke-width="2.3" stroke-linecap="round" fill="none"/>
      <!-- Outer Wave -->
      <path d="M20.4 7.6 C22.6 9.5 23.8 11.6 23.8 14 C23.8 16.4 22.6 18.5 20.4 20.4" 
            stroke="#671038" stroke-width="2.3" stroke-linecap="round" fill="none"/>
    </svg>
  `;

  const SVG_MUTED = `
    <svg class="speaker-svg" viewBox="0 0 28 28" fill="none" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
      <!-- Speaker Horn Outline -->
      <path d="M13 6.8 L7.6 10.6 H4 C3.45 10.6 3 11.05 3 11.6 V16.4 C3 16.95 3.45 17.4 4 17.4 H7.6 L13 21.2 Z" 
            stroke="#671038" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
      <!-- X mark -->
      <line x1="16.8" y1="11.2" x2="22.2" y2="16.8" stroke="#671038" stroke-width="2.5" stroke-linecap="round"/>
      <line x1="22.2" y1="11.2" x2="16.8" y2="16.8" stroke="#671038" stroke-width="2.5" stroke-linecap="round"/>
    </svg>
  `;

  // 1. Inject Styles
  function injectStyles() {
    if (document.getElementById('bg-music-styles')) return;
    const style = document.createElement('style');
    style.id = 'bg-music-styles';
    style.textContent = `
      .bg-music-toggle {
        position: fixed;
        top: 20px;
        right: 22px;
        z-index: 99999;
        width: 52px;
        height: 52px;
        border-radius: 50%;
        background-color: #ffffff;
        border: 4.5px solid #f9cadf;
        box-shadow: 0 4px 18px rgba(122, 22, 70, 0.15),
                    0 2px 6px rgba(0, 0, 0, 0.04);
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 0;
        cursor: pointer;
        user-select: none;
        outline: none;
        transition: transform 0.25s cubic-bezier(0.34, 1.56, 0.64, 1),
                    box-shadow 0.25s ease,
                    border-color 0.25s ease;
      }
      .bg-music-toggle:hover {
        transform: scale(1.08);
        border-color: #f7b5d2;
        box-shadow: 0 6px 24px rgba(122, 22, 70, 0.25),
                    0 2px 8px rgba(0, 0, 0, 0.06);
      }
      .bg-music-toggle:active {
        transform: scale(0.94);
      }
      .bg-music-toggle .speaker-svg {
        width: 28px;
        height: 28px;
        display: block;
        transition: transform 0.2s ease;
      }
      .bg-music-toggle.is-playing {
        border-color: #f7b5d2;
        animation: bgMusicPulse 2.8s infinite ease-in-out;
      }
      .bg-music-toggle.is-muted {
        opacity: 0.95;
      }

      /* Phone Preview Sound Button Matching Design */
      .btn-phone-sound {
        width: 38px !important;
        height: 38px !important;
        border-radius: 50% !important;
        background-color: #ffffff !important;
        border: 3.5px solid #f9cadf !important;
        box-shadow: 0 3px 12px rgba(122, 22, 70, 0.15) !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important;
        cursor: pointer !important;
        user-select: none !important;
        outline: none !important;
        transition: transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1),
                    box-shadow 0.2s ease,
                    border-color 0.2s ease !important;
      }
      .btn-phone-sound:hover {
        transform: scale(1.1) !important;
        border-color: #f7b5d2 !important;
        box-shadow: 0 4px 16px rgba(122, 22, 70, 0.25) !important;
      }
      .btn-phone-sound:active {
        transform: scale(0.92) !important;
      }
      .btn-phone-sound .speaker-svg {
        width: 22px !important;
        height: 22px !important;
        display: block !important;
      }
      .btn-phone-sound.is-playing {
        border-color: #f7b5d2 !important;
        animation: phoneSoundPulse 2.8s infinite ease-in-out !important;
      }

      @keyframes bgMusicPulse {
        0%, 100% {
          box-shadow: 0 4px 18px rgba(122, 22, 70, 0.15), 0 0 0 0 rgba(247, 181, 210, 0.5);
        }
        50% {
          box-shadow: 0 6px 22px rgba(122, 22, 70, 0.28), 0 0 0 6px rgba(247, 181, 210, 0.35);
        }
      }

      @keyframes phoneSoundPulse {
        0%, 100% {
          box-shadow: 0 3px 12px rgba(122, 22, 70, 0.15), 0 0 0 0 rgba(247, 181, 210, 0.5);
        }
        50% {
          box-shadow: 0 4px 16px rgba(122, 22, 70, 0.25), 0 0 0 4px rgba(247, 181, 210, 0.35);
        }
      }

      @media (max-width: 480px) {
        .bg-music-toggle {
          top: 14px;
          right: 14px;
          width: 46px;
          height: 46px;
          border-width: 3.5px;
        }
        .bg-music-toggle .speaker-svg {
          width: 24px;
          height: 24px;
        }
      }
    `;
    document.head.appendChild(style);
  }

  // 2. Initialize Audio & UI
  function initMusic() {
    injectStyles();

    // Ensure audio element
    let audio = document.getElementById('bg-audio');
    if (!audio) {
      audio = document.createElement('audio');
      audio.id = 'bg-audio';
      audio.src = AUDIO_SRC;
      audio.loop = true;
      audio.preload = 'auto';
      document.body.appendChild(audio);
    } else {
      if (!audio.src || !audio.src.includes('sub_clair-happy-birthday')) {
        audio.src = AUDIO_SRC;
      }
      audio.loop = true;
      audio.preload = 'auto';
    }

    audio.volume = DEFAULT_VOLUME;

    // Ensure main floating button element
    let btn = document.getElementById('bg-music-btn');
    if (!btn) {
      btn = document.createElement('button');
      btn.id = 'bg-music-btn';
      btn.className = 'bg-music-toggle is-muted';
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Toggle Background Music');
      document.body.appendChild(btn);
    } else {
      btn.className = 'bg-music-toggle is-muted';
    }

    // Phone preview sound button (if present on the page)
    const phoneSoundBtn = document.getElementById('btn-sound-toggle');

    // State from localStorage
    const savedMuted = localStorage.getItem('bg_music_muted');
    let isMuted = (savedMuted === 'true');

    // Restore playback time across page navigations
    const savedTime = parseFloat(localStorage.getItem('bg_music_time') || '0');
    if (!isNaN(savedTime) && savedTime > 0) {
      audio.currentTime = savedTime;
    }

    // Periodically sync audio time
    audio.addEventListener('timeupdate', function() {
      if (audio.currentTime > 0) {
        localStorage.setItem('bg_music_time', audio.currentTime.toString());
      }
    });

    const saveCurrentTime = function() {
      if (audio.currentTime > 0) {
        localStorage.setItem('bg_music_time', audio.currentTime.toString());
      }
    };
    window.addEventListener('pagehide', saveCurrentTime);
    window.addEventListener('beforeunload', saveCurrentTime);

    function updateUI(playing) {
      const svg = playing ? SVG_PLAYING : SVG_MUTED;
      
      // Update main floating button
      if (btn) {
        btn.innerHTML = svg;
        btn.classList.toggle('is-playing', playing);
        btn.classList.toggle('is-muted', !playing);
        btn.title = playing ? 'Mute Music' : 'Play Music';
        btn.setAttribute('aria-label', playing ? 'Mute Background Music' : 'Play Background Music');
      }

      // Update phone preview button
      if (phoneSoundBtn) {
        phoneSoundBtn.innerHTML = svg;
        phoneSoundBtn.classList.toggle('is-playing', playing);
        phoneSoundBtn.classList.toggle('is-muted', !playing);
        phoneSoundBtn.title = playing ? 'Mute Music' : 'Play Music';
        phoneSoundBtn.setAttribute('aria-label', playing ? 'Mute Background Music' : 'Play Background Music');
      }
    }

    function playAudio() {
      isMuted = false;
      localStorage.setItem('bg_music_muted', 'false');
      audio.muted = false;
      return audio.play().then(function() {
        updateUI(true);
      }).catch(function(err) {
        console.warn('Playback error or policy:', err);
        updateUI(false);
      });
    }

    function muteAudio() {
      isMuted = true;
      localStorage.setItem('bg_music_muted', 'true');
      audio.pause();
      updateUI(false);
    }

    function toggleMusic(e) {
      if (e) {
        e.stopPropagation();
        e.preventDefault();
      }
      if (audio.paused || isMuted) {
        playAudio();
      } else {
        muteAudio();
      }
    }

    if (btn) btn.onclick = toggleMusic;
    if (phoneSoundBtn) phoneSoundBtn.onclick = toggleMusic;

    // Initial playback attempt
    if (!isMuted) {
      audio.play().then(function() {
        updateUI(true);
      }).catch(function() {
        // Autoplay blocked by browser until user gesture
        updateUI(false);

        const onFirstInteraction = function() {
          if (!isMuted && audio.paused) {
            audio.play().then(function() {
              updateUI(true);
            }).catch(function() {});
          }
          cleanupInteractionListeners();
        };

        function cleanupInteractionListeners() {
          document.removeEventListener('click', onFirstInteraction);
          document.removeEventListener('touchstart', onFirstInteraction);
          document.removeEventListener('keydown', onFirstInteraction);
        }

        document.addEventListener('click', onFirstInteraction, { once: true });
        document.addEventListener('touchstart', onFirstInteraction, { once: true });
        document.addEventListener('keydown', onFirstInteraction, { once: true });
      });
    } else {
      updateUI(false);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMusic);
  } else {
    initMusic();
  }
})();
