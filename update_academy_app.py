#!/usr/bin/env python3
"""
Script to update Club Drone Academy with:
1. Student login modal & profile management
2. Embedded YouTube tutorials for every chapter
3. Interactive Q&A examination modules for every chapter
4. SQLite REST API synchronization
5. Regenerating index.html and Desktop/DroneAcademy.html
"""

import re
import json

CHAPTER_VIDEOS = {
  "ch1": { "id": "SpuXqNakP2A", "title": "Learn to Fly an FPV Drone TODAY (Beginner Guide)", "author": "Joshua Bardwell" },
  "ch2": { "id": "rzpizzr3SH0", "title": "FPV Drone Frame Geometry: True-X vs Deadcat Explained", "author": "Joshua Bardwell" },
  "ch3": { "id": "E6nsJpuaTQc", "title": "Multirotor Flight Physics & Motor Thrust Dynamics", "author": "Joshua Bardwell" },
  "ch4": { "id": "SC556vEMoYs", "title": "Component Selection Guide: 5-Inch Drone Kit Architecture", "author": "Joshua Bardwell" },
  "ch5": { "id": "E6nsJpuaTQc", "title": "How to Choose Motor KV and Stator Size for Your Build", "author": "Joshua Bardwell" },
  "ch6": { "id": "p09s3f9K6s0", "title": "How to Choose Propellers: Diameter, Pitch and Blade Count", "author": "Joshua Bardwell" },
  "ch7": { "id": "kdPfiZ37nKs", "title": "Why You MUST Put a Low-ESR Capacitor on Your ESC", "author": "Joshua Bardwell" },
  "ch8": { "id": "gryW-L_U9S8", "title": "Flight Controller Selection: Benefits of F7 over F4", "author": "Joshua Bardwell" },
  "ch9": { "id": "n8epgP7jlrk", "title": "4S vs 6S LiPo Batteries: Which Should You Choose?", "author": "Joshua Bardwell" },
  "ch10": { "id": "TMOeIQ4VRX4", "title": "FPV Goggles & Video Systems: DJI vs Walksnail vs HDZero vs Analog", "author": "Joshua Bardwell" },
  "ch11": { "id": "tNwHNYgWnp8", "title": "Build an FPV Drone: Final Betaflight Setup & PID Tuning", "author": "Joshua Bardwell" },
  "ch12": { "id": "DwcE68FmFrE", "title": "What are the Best Frequencies for FPV? RaceBand & Pit Mode", "author": "Joshua Bardwell" }
}

CHAPTER_QNA = {
  "ch1": [
    {
      "q": "In Mode 2 transmitter configuration, which stick controls the drone's Throttle and Yaw?",
      "options": ["Right stick", "Left stick", "Top slider dials", "Both sticks simultaneously"],
      "answer": 1,
      "explanation": "In Mode 2, the Left stick controls Throttle (vertical) and Yaw (horizontal), while the Right stick controls Pitch and Roll."
    },
    {
      "q": "Why do FPV racing pilots tilt their onboard camera upward at 30° to 50°?",
      "options": ["To look at the sky", "To keep the horizon visible when the quadcopter pitches forward at high speed", "To reduce propeller drag", "To improve antenna range"],
      "answer": 1,
      "explanation": "Multirotors must pitch their nose down to generate forward thrust. An upward-tilted camera keeps the flight path ahead visible."
    }
  ],
  "ch2": [
    {
      "q": "What critical electrical safety hazard does raw carbon fiber pose to drone electronics?",
      "options": ["It is magnetic and repels motors", "It is electrically conductive and will short-circuit bare solder pads or wires", "It blocks all radio waves completely", "It melts at room temperature"],
      "answer": 1,
      "explanation": "Carbon fiber is an electrical conductor. If bare solder joints touch the frame, it creates an immediate chassis short-circuit."
    },
    {
      "q": "What is the primary benefit of a Deadcat (DC) frame geometry?",
      "options": ["It flies upside down automatically", "It clears propellers out of the wide-angle camera field of view (FOV)", "It cuts current draw in half", "It increases top speed by 50%"],
      "answer": 1,
      "explanation": "Deadcat arms sweep front motors outward and back so spinning propellers do not appear in wide-angle HD camera footage."
    }
  ],
  "ch3": [
    {
      "q": "If a 5-inch drone has an All-Up Weight (AUW) of 600g and each motor produces 1500g of thrust, what is its Thrust-to-Weight Ratio (TWR)?",
      "options": ["2.5 : 1", "6.0 : 1", "10.0 : 1", "15.0 : 1"],
      "answer": 2,
      "explanation": "Total thrust = 4 × 1500g = 6000g. TWR = 6000g / 600g = 10.0 : 1 (Elite competition grade)."
    },
    {
      "q": "How does a quadcopter execute a Yaw rotation to the left without tilting its frame?",
      "options": ["By moving physical rudder flaps on the arms", "By speeding up the two CW motors and slowing down the two CCW motors", "By reversing all four motors", "By shifting the battery"],
      "answer": 1,
      "explanation": "Unbalancing reactive torque between clockwise and counter-clockwise motor pairs rotates the aircraft along its Z-axis."
    }
  ],
  "ch4": [
    {
      "q": "Why has the 5-inch FPV community transitioned almost universally to 6S (22.2V) batteries over 4S (14.8V)?",
      "options": ["6S batteries are half the weight", "Higher voltage requires ~33% less current for the same power, reducing Joule heat losses (I²R) by over 50% and eliminating voltage sag", "6S batteries charge in 5 seconds", "4S motors are no longer made"],
      "answer": 1,
      "explanation": "Power = V × I. Higher voltage means lower current, which dramatically reduces resistive heating and preserves punchout power."
    },
    {
      "q": "When pairing motors with an ESC, why is it recommended to choose an ESC with at least a 25% current safety margin?",
      "options": ["The extra amps make the camera sharper", "Motor peak burst current during aggressive punchouts can exceed continuous ratings, causing MOSFET thermal burnout", "To make props spin backwards", "It is legally required"],
      "answer": 1,
      "explanation": "High G punchouts push motor current draw to its limits; 25%+ headroom prevents blown MOSFETs."
    }
  ],
  "ch5": [
    {
      "q": "In motor nomenclature, what does the designation '2207' signify?",
      "options": ["2200 KV and 7 Volts", "22mm stator diameter and 7mm stator height", "22 turns of copper wire and 0.7mm magnet thickness", "220 grams of thrust on 7-inch props"],
      "answer": 1,
      "explanation": "The first two digits specify stator diameter (mm) and the last two digits specify stator height (mm)."
    },
    {
      "q": "What catastrophe occurs if motor mounting screws are too long and penetrate the stator base?",
      "options": ["The motor spins too slowly", "Screws puncture the enameled copper stator windings, creating an instant dead short that destroys motor and ESC", "The prop locknut cannot be tightened", "The gyro gets reversed"],
      "answer": 1,
      "explanation": "Motor screw length must never exceed the arm thickness plus motor base plate (~7-8mm total)."
    }
  ],
  "ch6": [
    {
      "q": "What theoretical distance would a '5146' propeller advance in one complete revolution?",
      "options": ["5.1 inches", "4.6 inches", "51.46 millimeters", "46 centimeters"],
      "answer": 1,
      "explanation": "In the 5146 code, '46' represents the pitch: 4.6 inches of linear forward travel per revolution."
    },
    {
      "q": "Why do most modern pilots configure their Betaflight rotation to 'Props Out' (Reversed Rotation)?",
      "options": ["It doubles the top speed", "Front blades spin outward, deflecting dirt, moisture, and gate clips away from the camera lens and airframe", "Motors consume zero current", "It eliminates the flight controller"],
      "answer": 1,
      "explanation": "Props Out throws grass and debris away from the FPV camera and pushes the drone off obstacles in gate collisions."
    }
  ],
  "ch7": [
    {
      "q": "Why is it strictly mandatory to solder a Low-ESR electrolytic capacitor across the ESC battery pads?",
      "options": ["To make the battery charge faster", "To absorb massive inductive voltage spikes (45V–55V on 6S) created by active motor braking that would otherwise fry electronics", "To provide 5 minutes of emergency power", "To filter microphone audio noise"],
      "answer": 1,
      "explanation": "Active motor braking dumps inductive back-EMF energy back onto the power rail; the Low-ESR capacitor clamps these destructive spikes."
    },
    {
      "q": "What is the primary benefit of Bidirectional DShot telemetry between ESC and FC?",
      "options": ["It allows you to play music on motors", "The ESC streams exact motor RPM back to the FC, enabling dynamic RPM notch filtering of motor vibrations", "It charges the radio transmitter while flying", "It replaces the radio receiver"],
      "answer": 1,
      "explanation": "Bidirectional DShot enables Betaflight to position dynamic notch filters exactly on motor frequencies, creating ultra-clean gyro signals."
    }
  ],
  "ch8": [
    {
      "q": "Why should a Flight Controller always be soft-mounted on silicone grommets rather than bolted rigidly to carbon fiber?",
      "options": ["To prevent the board from falling out", "To mechanically isolate the sensitive gyroscope from motor vibration harmonics that cause filter saturation and hot motors", "To increase electrical grounding conductivity", "To allow the USB port to bend"],
      "answer": 1,
      "explanation": "High-frequency motor vibrations will saturate the gyro sensor without silicone dampeners, causing the D-term to overheat motors."
    },
    {
      "q": "What is the golden rule when soldering a serial receiver (UART) to a flight controller?",
      "options": ["Connect TX to TX, and RX to RX", "Connect TX to RX, and RX to TX (crossover)", "Connect both wires to battery positive", "Only connect the ground wire"],
      "answer": 1,
      "explanation": "Serial communications cross over: Transmitter Transmit (TX) line feeds into Receiver Receive (RX) line."
    }
  ],
  "ch9": [
    {
      "q": "At what voltage per cell should a LiPo battery pack be stored when not flying for more than 24 hours?",
      "options": ["4.20V per cell (Fully charged)", "3.80V – 3.85V per cell (Storage voltage)", "3.00V per cell (Fully empty)", "0.00V per cell"],
      "answer": 1,
      "explanation": "Storing LiPos at 3.80V–3.85V maintains chemical equilibrium, preventing metallic lithium plating and cell degradation."
    },
    {
      "q": "What physical metric provides the most honest indicator of a LiPo battery pack's real health and performance?",
      "options": ["The color of the plastic shrink wrap", "Internal Resistance (IR) measured in milliohms (mΩ) per cell", "The printed manufacturer C-rating sticker", "How hot the pack gets during charging"],
      "answer": 1,
      "explanation": "Advertised C-ratings are often inflated; low internal resistance (1.5–3mΩ) is the true mark of a healthy high-discharge pack."
    }
  ],
  "ch10": [
    {
      "q": "What catastrophic signal loss occurs if you use an RHCP antenna on your drone and an LHCP antenna on your goggles?",
      "options": ["Video colors become inverted", "An immediate 20dB to 30dB cross-polarization penalty occurs, destroying over 90% of your operational video range", "The VTX will explode instantly", "The goggles turn off"],
      "answer": 1,
      "explanation": "Mismatching circular polarization causes the receiving antenna to actively reject the signal, drastically cutting range."
    },
    {
      "q": "Why is ExpressLRS (ELRS) 2.4GHz preferred over legacy 50Hz radio protocols for competitive FPV?",
      "options": ["It requires no antennas", "It offers sub-3ms latency, packet rates up to 1000Hz, and extreme long range using open-source LoRa technology", "It is manufactured exclusively by DJI", "It works without a battery"],
      "answer": 1,
      "explanation": "ELRS combines ultra-high packet rates (up to 1000Hz) with sub-3ms stick-to-motor latency and immense penetration range."
    }
  ],
  "ch11": [
    {
      "q": "What should you ALWAYS do before connecting a drone to the computer and configuring motors in Betaflight?",
      "options": ["Charge the battery to 100%", "REMOVE ALL PROPELLERS from the motors", "Turn off your radio transmitter", "Solder the antenna directly to the carbon frame"],
      "answer": 1,
      "explanation": "Accidental motor spin-up on the workbench with propellers on causes severe lacerations and physical injury. Always remove props!"
    },
    {
      "q": "In Betaflight PID tuning, what is the role of the 'D' (Derivative) gain?",
      "options": ["To increase raw top speed", "To act as a shock absorber that dampens P-term overshoot and prevents oscillations after quick flips", "To correct for steady wind drift over several seconds", "To make the beeper louder"],
      "answer": 1,
      "explanation": "The D-term measures the rate of error change, acting like a dynamic shock absorber to prevent P-term overshoot."
    }
  ],
  "ch12": [
    {
      "q": "Why does the international FPV racing community use the 8 RaceBand frequencies with a strict 37MHz minimum channel separation?",
      "options": ["To comply with FM radio music stations", "To prevent third-order Intermodulation Distortion (IMD) products from video transmitters jamming neighboring pilots", "Because only 8 drones can fit in the air physically", "To lower battery consumption"],
      "answer": 1,
      "explanation": "Non-linear RF mixing generates IMD interference spikes; 37MHz minimum spacing ensures 8 pilots can fly simultaneously with clear video."
    },
    {
      "q": "What is the maximum legal recreational altitude for drone flight under DGCA (India) and FAA (USA) aviation regulations?",
      "options": ["30 meters (100 feet) AGL", "120 meters (400 feet) AGL", "500 meters (1640 feet) AGL", "Unlimited in all airspace"],
      "answer": 1,
      "explanation": "Recreational drones must stay below 120m (400ft) Above Ground Level to remain well clear of manned civil aviation."
    }
  ]
}

def generate_update():
    with open('/home/amogh/projects/Club/Drone/build_full_academy.py', 'r') as f:
        src = f.read()

    # 1. Add modal styles if needed
    modal_style = '''
  /* Modal Overlay */
  .modal-overlay {
    position: fixed; inset: 0;
    background: rgba(0, 0, 0, 0.75);
    backdrop-filter: blur(6px);
    z-index: 100;
    display: none;
    align-items: center;
    justify-content: center;
    padding: 1rem;
  }
  .modal-overlay.open { display: flex; }
  .modal-box {
    background: #0E1626;
    border: 1px solid rgba(99, 102, 241, 0.3);
    border-radius: 20px;
    width: 100%;
    max-width: 440px;
    padding: 2rem;
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.6);
  }

  /* Option cards in Q&A */
  .qna-opt {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.75rem 1rem;
    cursor: pointer;
    font-size: 14px;
    color: var(--text-secondary);
    transition: all 0.2s;
    margin-bottom: 0.5rem;
  }
  .qna-opt:hover {
    background: var(--bg-card);
    border-color: rgba(99, 102, 241, 0.3);
    color: #F8FAFC;
  }
  .qna-opt.correct {
    background: rgba(16, 185, 129, 0.12) !important;
    border-color: var(--accent-emerald) !important;
    color: #6EE7B7 !important;
    font-weight: 600;
  }
  .qna-opt.wrong {
    background: rgba(244, 63, 94, 0.12) !important;
    border-color: var(--accent-rose) !important;
    color: #FDA4AF !important;
  }
'''
    src = src.replace('/* Animation */', modal_style + '\n  /* Animation */')

    # 2. Add Login Modal & Header Profile
    login_modal_html = '''
<!-- Student Login Modal -->
<div class="modal-overlay" id="loginModal">
  <div class="modal-box" style="text-align:center">
    <div style="font-size:38px;margin-bottom:0.5rem">🚁</div>
    <h2 style="font-size:22px;font-weight:800;color:#F8FAFC;margin-bottom:0.25rem">Welcome to Club Drone Academy</h2>
    <p style="font-size:13px;color:var(--text-secondary);margin-bottom:1.5rem">
      Sign in with your name and email to track your lesson progress, save Q&A scores, and sync with the instructor database.
    </p>
    <div style="text-align:left;display:flex;flex-direction:column;gap:1rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">STUDENT FULL NAME</label>
        <input type="text" id="loginName" class="spec-select" placeholder="e.g. Alex Sharma">
      </div>
      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">STUDENT EMAIL / ID</label>
        <input type="email" id="loginEmail" class="spec-select" placeholder="e.g. alex@university.edu">
      </div>
    </div>
    <button class="btn-primary" style="width:100%;justify-content:center" onclick="submitLogin()">
      Start Flight Training →
    </button>
    <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border);display:flex;justify-content:space-between;font-size:12px">
      <a href="admin.html" style="color:var(--accent-blue);text-decoration:none">Instructor Command Center ↗</a>
      <button onclick="guestContinue()" style="background:none;border:none;color:var(--text-muted);cursor:pointer">Continue as Guest</button>
    </div>
  </div>
</div>
'''

    header_profile_html = '''
    <div id="userProfileBadge" style="display:flex;align-items:center;gap:0.4rem;background:var(--bg-surface);border:1px solid var(--border);border-radius:999px;padding:0.25rem 0.65rem;cursor:pointer" onclick="promptSwitchUser()" title="Click to switch student profile">
      <div style="width:22px;height:22px;border-radius:50%;background:var(--accent-blue);color:white;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700" id="userAvatarChar">S</div>
      <span style="font-size:12px;font-weight:600;color:#F8FAFC;max-width:85px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" id="userNameLabel">Student</span>
    </div>
'''

    src = src.replace('<!-- Persistent Header -->', login_modal_html + '\n<!-- Persistent Header -->')
    src = src.replace('<div class="progress-track" style="flex:1;max-width:220px">', header_profile_html + '\n      <div class="progress-track" style="flex:1;max-width:180px">')

    # 3. Add Video & Q&A data structures and functions in JS
    js_addons = f'''
// ==========================================
// VIDEO TUTORIALS & INTERACTIVE Q&A DATABASE
// ==========================================
const CHAPTER_VIDEOS = {json.dumps(CHAPTER_VIDEOS, indent=2)};
const CHAPTER_QNA = {json.dumps(CHAPTER_QNA, indent=2)};

let currentUser = JSON.parse(localStorage.getItem('droneAcademy_activeUser') || 'null');
let userQnaScores = JSON.parse(localStorage.getItem('clubDroneAcademy_qna') || '{{}}');

function getVideoSectionHtml(id) {{
  const vid = CHAPTER_VIDEOS[id];
  if (!vid) return '';
  return `
    <div class="ch-section">
      <h2>📺 Video Tutorial</h2>
      <div style="background:#0D1424;border:1px solid rgba(99,102,241,0.25);border-radius:18px;overflow:hidden;margin:1.25rem 0;box-shadow:0 8px 30px rgba(0,0,0,0.35)">
        <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
          <iframe src="https://www.youtube-nocookie.com/embed/${{vid.id}}" 
                  title="${{vid.title}}" 
                  style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
                  allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                  allowfullscreen></iframe>
        </div>
        <div style="padding:1rem 1.25rem;display:flex;align-items:center;justify-content:space-between;gap:1rem;flex-wrap:wrap">
          <div>
            <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase">AUTHORITATIVE TUTORIAL • ${{vid.author}}</div>
            <div style="font-size:14px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">${{vid.title}}</div>
          </div>
          <a href="https://www.youtube.com/watch?v=${{vid.id}}" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.4rem 0.85rem">
            Watch on YouTube ↗
          </a>
        </div>
      </div>
    </div>
  `;
}}

function getQnaSectionHtml(id) {{
  const questions = CHAPTER_QNA[id];
  if (!questions || questions.length === 0) return '';

  const saved = userQnaScores[id] || {{ answers: {{}} }};

  return `
    <div class="ch-section">
      <h2>📝 Lesson Knowledge Check & Q&A</h2>
      <p style="font-size:14px;color:var(--text-secondary);margin-bottom:1rem">
        Answer the following technical questions to verify your comprehension. Your answers are automatically saved to your profile:
      </p>

      <div class="widget-card" style="margin-top:0.5rem">
        <div class="widget-header">
          <span class="widget-title">🧠 Examination & Mastery Check</span>
          <span style="font-size:12px;color:var(--text-muted)" id="qnaScoreBadge_${{id}}">
            ${{saved.score !== undefined ? `Score: ${{saved.score}} / ${{questions.length}}` : `2 Questions`}}
          </span>
        </div>

        <div style="display:flex;flex-direction:column;gap:1.5rem">
          ${{questions.map((q, qIdx) => {{
            const selectedOpt = saved.answers ? saved.answers[qIdx] : undefined;
            return `
              <div>
                <div style="font-size:14px;font-weight:700;color:#F8FAFC;margin-bottom:0.75rem">
                  ${{qIdx + 1}}. ${{q.q}}
                </div>
                <div id="qnaOptions_${{id}}_${{qIdx}}">
                  ${{q.options.map((opt, optIdx) => {{
                    let optClass = 'qna-opt';
                    if (selectedOpt !== undefined) {{
                      if (optIdx === q.answer) optClass += ' correct';
                      else if (selectedOpt === optIdx) optClass += ' wrong';
                    }}
                    return `
                      <div class="${{optClass}}" onclick="selectQnaOption('${{id}}', ${{qIdx}}, ${{optIdx}})">
                        <span style="font-weight:600;margin-right:0.4rem">${{String.fromCharCode(65 + optIdx)}}.</span> ${{opt}}
                      </div>
                    `;
                  }}).join('')}}
                </div>
                <div id="qnaFeedback_${{id}}_${{qIdx}}" style="font-size:12px;margin-top:0.4rem;${{selectedOpt !== undefined ? 'display:block' : 'display:none'}}">
                  <div style="padding:0.6rem 0.85rem;border-radius:8px;background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.2);color:var(--text-secondary)">
                    <strong>💡 Explanation:</strong> ${{q.explanation}}
                  </div>
                </div>
              </div>
            `;
          }}).join('')}}
        </div>
      </div>
    </div>
  `;
}}

function selectQnaOption(chId, qIdx, optIdx) {{
  const questions = CHAPTER_QNA[chId];
  if (!questions) return;
  const q = questions[qIdx];

  if (!userQnaScores[chId]) {{
    userQnaScores[chId] = {{ answers: {{}}, score: 0, total: questions.length }};
  }}

  userQnaScores[chId].answers[qIdx] = optIdx;

  // Recalculate chapter score
  let correctCount = 0;
  questions.forEach((question, idx) => {{
    if (userQnaScores[chId].answers[idx] === question.answer) {{
      correctCount++;
    }}
  }});
  userQnaScores[chId].score = correctCount;
  userQnaScores[chId].total = questions.length;

  localStorage.setItem('clubDroneAcademy_qna', JSON.stringify(userQnaScores));

  // Update UI options
  const optContainer = document.getElementById(`qnaOptions_${{chId}}_${{qIdx}}`);
  if (optContainer) {{
    const options = optContainer.querySelectorAll('.qna-opt');
    options.forEach((el, i) => {{
      el.classList.remove('correct', 'wrong');
      if (i === q.answer) el.classList.add('correct');
      else if (i === optIdx) el.classList.add('wrong');
    }});
  }}

  // Show feedback
  const feedbackEl = document.getElementById(`qnaFeedback_${{chId}}_${{qIdx}}`);
  if (feedbackEl) feedbackEl.style.display = 'block';

  // Update score badge
  const badge = document.getElementById(`qnaScoreBadge_${{chId}}`);
  if (badge) badge.textContent = `Score: ${{correctCount}} / ${{questions.length}}`;

  syncWithDatabase();
}}

// ==========================================
// USER LOGIN & DATABASE SYNCHRONIZATION
// ==========================================
function checkLogin() {{
  if (!currentUser) {{
    document.getElementById('loginModal').classList.add('open');
  }} else {{
    updateHeaderProfile();
    syncWithDatabase();
  }}
}}

async function submitLogin() {{
  const name = document.getElementById('loginName').value.trim();
  const email = document.getElementById('loginEmail').value.trim();

  if (!name || !email) {{
    alert('Please enter both your name and email to proceed.');
    return;
  }}

  currentUser = {{ name, email, loggedInAt: new Date().toISOString() }};
  localStorage.setItem('droneAcademy_activeUser', JSON.stringify(currentUser));
  document.getElementById('loginModal').classList.remove('open');
  updateHeaderProfile();

  // Attempt sync with server
  try {{
    const res = await fetch('/api/login', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{ name, email }})
    }});
    if (res.ok) {{
      const data = await res.json();
      if (data.student) {{
        // Merge progress from server if exists
        if (data.student.completed_chapters && data.student.completed_chapters.length > 0) {{
          data.student.completed_chapters.forEach(ch => progress[ch] = true);
          localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
        }}
        if (data.student.qna_scores && Object.keys(data.student.qna_scores).length > 0) {{
          userQnaScores = Object.assign(userQnaScores, data.student.qna_scores);
          localStorage.setItem('clubDroneAcademy_qna', JSON.stringify(userQnaScores));
        }}
        updateCourseProgress();
      }}
    }}
  }} catch (e) {{
    console.log('Server offline; using local database storage');
  }}

  syncWithDatabase();
}}

function guestContinue() {{
  currentUser = {{ name: 'Guest Student', email: 'guest@droneacademy.local', loggedInAt: new Date().toISOString() }};
  localStorage.setItem('droneAcademy_activeUser', JSON.stringify(currentUser));
  document.getElementById('loginModal').classList.remove('open');
  updateHeaderProfile();
}}

function promptSwitchUser() {{
  const name = currentUser ? currentUser.name : '';
  const email = currentUser ? currentUser.email : '';
  if (confirm(`Currently signed in as: ${{name}} (${{email}})\\n\\nDo you want to switch student profile or sign in as someone else?`)) {{
    document.getElementById('loginName').value = '';
    document.getElementById('loginEmail').value = '';
    document.getElementById('loginModal').classList.add('open');
  }}
}}

function updateHeaderProfile() {{
  const avatar = document.getElementById('userAvatarChar');
  const label = document.getElementById('userNameLabel');
  if (currentUser && currentUser.name) {{
    avatar.textContent = currentUser.name.charAt(0).toUpperCase();
    label.textContent = currentUser.name.split(' ')[0];
  }} else {{
    avatar.textContent = 'S';
    label.textContent = 'Student';
  }}
}}

async function syncWithDatabase() {{
  if (!currentUser || !currentUser.email) return;

  const completedList = Object.keys(progress).filter(k => progress[k]);
  const overallPct = Math.round((completedList.length / CHAPTERS.length) * 100);

  // 1. Sync to local database storage (all students)
  const localDb = JSON.parse(localStorage.getItem('droneAcademy_allStudents') || '[]');
  const idx = localDb.findIndex(s => s.email.toLowerCase() === currentUser.email.toLowerCase());
  const record = {{
    id: idx >= 0 ? localDb[idx].id : Date.now(),
    name: currentUser.name,
    email: currentUser.email,
    created_at: idx >= 0 ? localDb[idx].created_at : new Date().toISOString(),
    last_active: new Date().toISOString(),
    overall_progress: overallPct,
    completed_chapters: completedList,
    qna_scores: userQnaScores
  }};

  if (idx >= 0) localDb[idx] = record;
  else localDb.unshift(record);

  localStorage.setItem('droneAcademy_allStudents', JSON.stringify(localDb));

  // 2. Sync to Python SQLite server API if accessible
  try {{
    await fetch('/api/progress', {{
      method: 'POST',
      headers: {{ 'Content-Type': 'application/json' }},
      body: JSON.stringify({{
        email: currentUser.email,
        completed_chapters: completedList,
        qna_scores: userQnaScores,
        overall_progress: overallPct
      }})
    }});
  }} catch (e) {{
    // Server offline, silent fallback
  }}
}}
'''

    # Inject JS addons
    src = src.replace('// Persistent State', js_addons + '\n// Persistent State')

    # Wrap getChapterContentById to inject video & Q&A
    wrapped_get_content = '''
function getChapterContentById(id) {
  let raw = "";
  switch(id) {
    case 'ch1': raw = getCh1Content(); break;
    case 'ch2': raw = getCh2Content(); break;
    case 'ch3': raw = getCh3Content(); break;
    case 'ch4': raw = getCh4Content(); break;
    case 'ch5': raw = getCh5Content(); break;
    case 'ch6': raw = getCh6Content(); break;
    case 'ch7': raw = getCh7Content(); break;
    case 'ch8': raw = getCh8Content(); break;
    case 'ch9': raw = getCh9Content(); break;
    case 'ch10': raw = getCh10Content(); break;
    case 'ch11': raw = getCh11Content(); break;
    case 'ch12': raw = getCh12Content(); break;
    default: return '<p>Chapter content not found.</p>';
  }
  return getVideoSectionHtml(id) + raw + getQnaSectionHtml(id);
}
'''
    src = re.sub(r'function getChapterContentById\(id\)\s*\{.*?default:\s*return\s*\'<p>Chapter content not found\.</p>\';\s*\}\s*\}', wrapped_get_content.strip(), src, flags=re.DOTALL)

    # In toggleCompleteCurrent, add syncWithDatabase call
    src = src.replace("localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));", "localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));\n  syncWithDatabase();")

    # In window init, call checkLogin
    src = src.replace("updateCourseProgress();\n});", "updateCourseProgress();\n  checkLogin();\n});")
    src = src.replace("updateCourseProgress();\n</script>", "updateCourseProgress();\ncheckLogin();\n</script>")

    with open('/home/amogh/projects/Club/Drone/build_full_academy.py', 'w') as out:
        out.write(src)

    print("[✓] Successfully updated build_full_academy.py with Login, Videos & Q&A!")

if __name__ == '__main__':
    generate_update()
