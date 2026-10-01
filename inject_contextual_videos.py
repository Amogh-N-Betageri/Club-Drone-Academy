#!/usr/bin/env python3
"""
Inject contextual YouTube video tutorial spots directly into their exact topical positions
within each chapter of build_full_academy.py.
"""

def get_video_card_code(vid_id, title, author="Joshua Bardwell"):
    return f'''
  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/{vid_id}" 
              title="{title}" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • {author}</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">{title}</div>
      </div>
      <a href="https://www.youtube.com/watch?v={vid_id}" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>
'''

def update_file():
    with open('/home/amogh/projects/Club/Drone/build_full_academy.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove the generic top video call from getChapterContentById
    content = content.replace("return getVideoSectionHtml(id) + raw + getQnaSectionHtml(id);", "return raw + getQnaSectionHtml(id);")

    # Chapter 1:
    # Spot 1: Under "Flight Stabilization Modes: Angle vs Acro"
    v_ch1_acro = get_video_card_code("fiUSJgQOkOA", "Should I Learn Acro or Angle First As A New FPV Pilot?")
    content = content.replace(
        "<h2>Flight Stabilization Modes: Angle vs Acro</h2>",
        f"<h2>Flight Stabilization Modes: Angle vs Acro</h2>\n{v_ch1_acro}"
    )

    # Spot 2: Under "The Simulator Mastery Roadmap"
    v_ch1_sim = get_video_card_code("SpuXqNakP2A", "Learn to Fly an FPV Drone TODAY (Beginner Simulator Guide)")
    content = content.replace(
        "<h2>The Simulator Mastery Roadmap</h2>",
        f"<h2>The Simulator Mastery Roadmap</h2>\n{v_ch1_sim}"
    )

    # Chapter 2:
    # Spot 1: Under "FPV Drone Size Classes"
    v_ch2_size = get_video_card_code("SC556vEMoYs", "Sub-250g or 5 Inch FPV Drone Kit? Which To Get?")
    content = content.replace(
        "<h2>FPV Drone Size Classes</h2>",
        f"<h2>FPV Drone Size Classes</h2>\n{v_ch2_size}"
    )

    # Spot 2: Under "Airframe Geometry & Dynamics"
    v_ch2_geo = get_video_card_code("rzpizzr3SH0", "What Downsides Do Deadcat Frames Actually Have? Frame Geometry")
    content = content.replace(
        "<h2>Airframe Geometry & Dynamics</h2>",
        f"<h2>Airframe Geometry & Dynamics</h2>\n{v_ch2_geo}"
    )

    # Chapter 3:
    # Spot 1: Under "Newton's Laws Applied to Multirotors"
    v_ch3_phys = get_video_card_code("SpuXqNakP2A", "How Quadcopters Fly & Momentum Dynamics")
    content = content.replace(
        "<h2>Newton's Laws Applied to Multirotors</h2>",
        f"<h2>Newton's Laws Applied to Multirotors</h2>\n{v_ch3_phys}"
    )

    # Spot 2: Under "Thrust-to-Weight Ratio (TWR) Formula"
    v_ch3_twr = get_video_card_code("6t4gS-HfqT0", "Thrust to Weight Ratio for FPV Drones - How Much Power Do You Need?")
    content = content.replace(
        "<h2>Thrust-to-Weight Ratio (TWR) Formula</h2>",
        f"<h2>Thrust-to-Weight Ratio (TWR) Formula</h2>\n{v_ch3_twr}"
    )

    # Chapter 4:
    # Spot 1: Under "The Component Harmony Principle"
    v_ch4_parts = get_video_card_code("SC556vEMoYs", "How to Choose Parts for a 5-Inch FPV Drone Kit")
    content = content.replace(
        "<h2>The Component Harmony Principle</h2>",
        f"<h2>The Component Harmony Principle</h2>\n{v_ch4_parts}"
    )

    # Spot 2: Under "Why Each Specification is Chosen"
    v_ch4_4s6s = get_video_card_code("n8epgP7jlrk", "4S vs 6S LiPo Batteries - Which Do I Buy as a New Pilot?")
    content = content.replace(
        "<h2>Why Each Specification is Chosen</h2>",
        f"<h2>Why Each Specification is Chosen</h2>\n{v_ch4_4s6s}"
    )

    # Chapter 5:
    # Spot 1: Under "Stator Size Geometry (XXYY Naming)"
    v_ch5_stator = get_video_card_code("Wxpa-1FrbYM", "2306 vs 2207 Motor Size Comparison for FPV Mini Quad")
    content = content.replace(
        "<h2>Stator Size Geometry (XXYY Naming)</h2>",
        f"<h2>Stator Size Geometry (XXYY Naming)</h2>\n{v_ch5_stator}"
    )

    # Spot 2: Under "Motor KV & Stator Explorer"
    v_ch5_kv = get_video_card_code("E6nsJpuaTQc", "How Do You Choose Motor KV for a Build?")
    content = content.replace(
        "<h2>Motor KV & Stator Explorer</h2>",
        f"<h2>Motor KV & Stator Explorer</h2>\n{v_ch5_kv}"
    )

    # Chapter 6:
    # Spot 1: Under "Decoding Propeller Naming Formats"
    v_ch6_props = get_video_card_code("p09s3f9K6s0", "How to Choose FPV Drone Propellers: Pitch and Diameter")
    content = content.replace(
        "<h2>Decoding Propeller Naming Formats</h2>",
        f"<h2>Decoding Propeller Naming Formats</h2>\n{v_ch6_props}"
    )

    # Spot 2: Under "Props In vs Props Out"
    v_ch6_propsout = get_video_card_code("bZL-BBl9JnE", "Props-In (Standard) vs. Props-Out (Reversed) - Which Is Better?")
    content = content.replace(
        "<h2>\"Props In\" vs \"Props Out\" (Reversed Rotation)</h2>",
        f"<h2>\"Props In\" vs \"Props Out\" (Reversed Rotation)</h2>\n{v_ch6_propsout}"
    )

    # Chapter 7:
    # Spot 1: Under "ESC Architecture"
    v_ch7_esc = get_video_card_code("NoiqODFwU68", "How Do I Pick An ESC For My Flight Controller?")
    content = content.replace(
        "<h2>Electronic Speed Controller (ESC) Architecture</h2>",
        f"<h2>Electronic Speed Controller (ESC) Architecture</h2>\n{v_ch7_esc}"
    )

    # Spot 2: Under "The Mandatory Low-ESR Capacitor"
    v_ch7_cap = get_video_card_code("kdPfiZ37nKs", "Best Way to Mount Your Capacitor on ESC or XT60")
    content = content.replace(
        "<h2>The Mandatory Low-ESR Capacitor</h2>",
        f"<h2>The Mandatory Low-ESR Capacitor</h2>\n{v_ch7_cap}"
    )

    # Spot 3: Under "ESC Firmware: AM32 & Bidirectional DShot"
    v_ch7_rpm = get_video_card_code("2tvWimtmgd4", "How Does Betaflight RPM Filtering Work?")
    content = content.replace(
        "<h2>ESC Firmware: AM32 & Bidirectional DShot</h2>",
        f"<h2>ESC Firmware: AM32 & Bidirectional DShot</h2>\n{v_ch7_rpm}"
    )

    # Chapter 8:
    # Spot 1: Under "Compute Architecture: MCUs & Gyros"
    v_ch8_fc = get_video_card_code("gryW-L_U9S8", "What Are The Benefits Of An F7 Flight Controller Over An F4?")
    content = content.replace(
        "<h2>Compute Architecture: MCUs & Gyros</h2>",
        f"<h2>Compute Architecture: MCUs & Gyros</h2>\n{v_ch8_fc}"
    )

    # Spot 2: Under "Gyroscopes & Soft-Mounting Physics"
    v_ch8_wire = get_video_card_code("QhW-0ddGJ7A", "How to Wire a Flight Controller and Soft Mount")
    content = content.replace(
        "<h2>Gyroscopes & Soft-Mounting Physics</h2>",
        f"<h2>Gyroscopes & Soft-Mounting Physics</h2>\n{v_ch8_wire}"
    )

    # Chapter 9:
    # Spot 1: Under "LiPo Electrochemistry & Voltage Thresholds"
    v_ch9_lipo = get_video_card_code("lZKoW_ekAu0", "How to Charge and Handle LiPo Batteries Safely")
    content = content.replace(
        "<h2>LiPo Electrochemistry & Voltage Thresholds</h2>",
        f"<h2>LiPo Electrochemistry & Voltage Thresholds</h2>\n{v_ch9_lipo}"
    )

    # Spot 2: Under "The C-Rating Reality vs Marketing Claims"
    v_ch9_ir = get_video_card_code("uBPuwOyh3do", "LiPo Internal Resistance & C-Rating Truth")
    content = content.replace(
        "<h2>The C-Rating Reality vs Marketing Claims</h2>",
        f"<h2>The C-Rating Reality vs Marketing Claims</h2>\n{v_ch9_ir}"
    )

    # Chapter 10:
    # Spot 1: Under "The FPV Video Ecosystems Compared"
    v_ch10_vtx = get_video_card_code("TMOeIQ4VRX4", "Best FPV Goggles Buyer Guide: DJI vs HDZero vs Walksnail vs Analog")
    content = content.replace(
        "<h2>The FPV Video Ecosystems Compared</h2>",
        f"<h2>The FPV Video Ecosystems Compared</h2>\n{v_ch10_vtx}"
    )

    # Spot 2: Under "Antenna Circular Polarization Physics"
    v_ch10_ant = get_video_card_code("mbHl3DgnN4k", "Left vs Right Circular Polarization (LHCP vs RHCP)")
    content = content.replace(
        "<h2>Antenna Circular Polarization Physics</h2>",
        f"<h2>Antenna Circular Polarization Physics</h2>\n{v_ch10_ant}"
    )

    # Spot 3: Under "ExpressLRS: The Open-Source RC King"
    v_ch10_elrs = get_video_card_code("oHA2qhABamc", "Why I Always Bind ELRS - ExpressLRS Setup Guide")
    content = content.replace(
        "<h2>ExpressLRS: The Open-Source RC King</h2>",
        f"<h2>ExpressLRS: The Open-Source RC King</h2>\n{v_ch10_elrs}"
    )

    # Chapter 11:
    # Spot 1: Under "The Step-by-Step Bench Assembly Sequence"
    v_ch11_build = get_video_card_code("kfhHecJsS3Y", "Build an FPV Drone Step by Step - Soldering & Assembly")
    content = content.replace(
        "<h2>The Step-by-Step Bench Assembly Sequence</h2>",
        f"<h2>The Step-by-Step Bench Assembly Sequence</h2>\n{v_ch11_build}"
    )

    # Spot 2: Under "The PID Control Loop Explained"
    v_ch11_pid = get_video_card_code("M-6pq1rFtBI", "Should I Learn to PID Tune or Use Betaflight Presets?")
    v_ch11_smoke = get_video_card_code("I5a0TAmEwLE", "Why You Need a Smoke Stopper to Prevent Fires")
    content = content.replace(
        "<h2>The PID Control Loop Explained</h2>",
        f"<h2>The PID Control Loop Explained</h2>\n{v_ch11_pid}"
    )

    # Chapter 12:
    # Spot 1: Under "Race Event Frequency Management & Pit Etiquette"
    v_ch12_freq = get_video_card_code("DwcE68FmFrE", "What Are The Best Frequencies to Use For FPV? RaceBand & Pit Mode")
    content = content.replace(
        "<h2>Race Event Frequency Management & Pit Etiquette</h2>",
        f"<h2>Race Event Frequency Management & Pit Etiquette</h2>\n{v_ch12_freq}"
    )

    # Spot 2: Under "Interactive Master Pre-Flight Checklist"
    v_ch12_safe = get_video_card_code("O5ngG--_pKo", "Failsafe Setup and Test in Betaflight to Prevent Flyaways")
    content = content.replace(
        "<h2>Interactive Master Pre-Flight Checklist</h2>",
        f"<h2>Interactive Master Pre-Flight Checklist</h2>\n{v_ch12_safe}"
    )

    with open('/home/amogh/projects/Club/Drone/build_full_academy.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print("[✓] Contextual video tutorial spots successfully injected into build_full_academy.py!")

if __name__ == '__main__':
    update_file()
