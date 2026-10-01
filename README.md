# 🛸 Club Drone Academy

> **Modern Interactive FPV Robotics, Aeronautical Engineering & Flight Mastery Platform**  
> *"You're gonna learn something today!"* — Inspired by Joshua Bardwell, Oscar Liang, and the open-source FPV multirotor engineering community.

Welcome to **Club Drone Academy**, a clean, modern, multi-page interactive learning application inspired by Brilliant.org, Khan Academy, and Codecademy. It teaches every aspect of FPV quadcopters: piloting dynamics, size classes, Newtonian flight physics, component selection with real math, electronics, step-by-step soldering, Betaflight logic, and race competition execution.

---

## 🌟 Architecture & Features

### 1. 📖 12 Dedicated Chapter Lessons (Multi-Page Hash Routing)
The app uses clean client-side routing (`#home`, `#ch1` through `#ch12`) so each topic has its own dedicated page with generous whitespace, focus mode, and breadcrumb navigation:

1. **Chapter 1: FPV Piloting & Flight Dynamics**
   - Mode 2 transmitter anatomy (Throttle, Yaw, Pitch, Roll).
   - Interactive visual stick gimbals with real-time attitude feedback.
   - Angle vs Horizon vs Acro (Rate mode) flight stabilization physics.
   - The camera tilt angle formula (\(F_{\text{forward}} = T \cdot \sin(\theta)\)).
   - Side-by-side interactive comparison: FPV Racing Quad vs DJI Camera Drone.
   - Simulator training roadmap (Velocidrone, Liftoff).

2. **Chapter 2: Types of Drones & Airframe Geometry**
   - Size classes: Tiny Whoop (65mm 1S), Toothpick/Micro (2.5–3.5"), 5-Inch Standard, 7-Inch Long Range, and Ducted Cinewhoops.
   - Airframe geometries: True-X, Stretch-X, Deadcat (DC), and Ducted Cinewhoop.
   - Interactive airframe geometry visualizer with dynamic SVG diagrams.
   - Carbon fiber material science (T700 3K twill, electrical conductivity danger, arm thickness 4mm vs 5–6mm).

3. **Chapter 3: Physics of Drone Flight & Calculations**
   - Newton's Laws of Motion applied to quadcopters (Law of Inertia in Acro, \(F=ma\), Action-Reaction).
   - Counter-rotating propellers & yaw generation (torque cancellation).
   - Differential thrust for Roll and Pitch authority.
   - Thrust-to-Weight Ratio (TWR) formula and standards:
     $$\text{TWR} = \frac{\text{Total Thrust}}{\text{All-Up Weight (AUW)}}$$
   - Hover throttle percentage calculation:
     $$\text{Hover Throttle} \approx \frac{1}{\text{TWR}} \times 100\%$$
   - Electrical power \(P = V \times I\) and Joule resistive heat loss \(P_{\text{loss}} = I^2 R\).
   - **Interactive Multirotor Dynamics & TWR Calculator** (AUW, motor thrust, G-force acceleration, flight rating).

4. **Chapter 4: Master Drone Spec Selection Guide (Why Each Spec is Chosen)**
   - The Component Harmony Principle: Step-by-step sizing sequence.
   - Master reference breakdown explaining **why every single specification is selected** (frame thickness, stator volume, motor KV, prop pitch, ESC continuous amps, 6S vs 4S voltage, and battery capacity).
   - **Interactive 5-Inch Spec Builder & Compatibility Validator** with live AUW, peak current, ESC thermal headroom, TWR, and automated compatibility rationale.

5. **Chapter 5: Motors: The Electromechanical Powerplant**
   - Brushless DC outrunner operation (12N14P configuration, permanent N52H neodymium magnets, copper stator coils).
   - Stator dimensions (XXYY format: 2207 vs 2306 volume comparison formula \(V = \pi (d/2)^2 h\)).
   - The KV constant (\(\text{RPM} = \text{KV} \times V\), unloaded vs working RPM).
   - The motor screw depth trap (\(L_{\text{screw}} \le t_{\text{arm}} + t_{\text{base}}\)).
   - **Interactive Motor KV & Working RPM Explorer**.

6. **Chapter 6: Propellers: Aerodynamics & Thrust**
   - Airfoil lift and induced drag.
   - Decoding naming formats (51466, 5×4.3×3).
   - Pitch dynamics (low pitch 3.0–3.8" vs high pitch 4.5–5.0"+).
   - Blade count trade-offs (2-blade efficiency vs 3-blade balance vs 4-blade grip).
   - "Props In" vs "Props Out" (reversed rotation keeps debris off camera lens).
   - **Interactive Prop Pitch Speed & Airspeed Calculator**.

7. **Chapter 7: ESC & Power Electronics**
   - 3-phase AC inversion with 6 power MOSFET half-bridges (\(R_{DS(on)}\) resistance).
   - Firmware: AM32 (open-source 32-bit standard) vs Bluejay vs BLHeli_S.
   - DShot600 digital protocol and Bidirectional DShot (eRPM telemetry for RPM filtering).
   - The mandatory Low-ESR electrolytic capacitor (absorbing inductive voltage spikes \(>45\text{V}\) from active motor braking).
   - JST harness pinout mismatch danger.
   - **Interactive ESC Safety Margin Calculator**.

8. **Chapter 8: Flight Controller: Architecture & Logic**
   - Microcontrollers: STM32F405 vs STM32F722 vs STM32H743.
   - Gyro sensors: ICM42688P low-noise vs BMI270 vibration tolerance.
   - Silicone soft-mounting physics (preventing gyro saturation).
   - Onboard voltage regulators (5V for RX/GPS, filtered 9V/10V for digital video).
   - **Interactive UART Serial Bus Planner**.

9. **Chapter 9: Battery Power Systems & Chemistry**
   - LiPo cell chemistry and voltage thresholds (4.20V full, 3.85V storage, 3.50V landing, <3.20V danger).
   - 4S vs 6S physics: 33% lower current for same wattage, 55% reduction in Joule heating (\(I^2 R\)), and eliminated voltage sag.
   - C-rating reality vs internal resistance (IR in \(m\Omega\)).
   - **Interactive LiPo Flight Time & Energy Simulator**.

10. **Chapter 10: FPV Video & Radio Link Systems**
    - The 4 video systems compared: Analog 5.8GHz vs DJI O3/O4 vs Walksnail Avatar vs HDZero.
    - Antenna circular polarization (RHCP vs LHCP, multipath rejection, the fatal 20dB cross-polarization penalty).
    - ExpressLRS (ELRS) 2.4GHz / 900MHz LoRa spread-spectrum (<3ms latency, 1000Hz packet rates).

11. **Chapter 11: Assembling the Drone & Betaflight Software**
    - Step-by-step bench assembly sequence (frame dry-fit, motor mounting, ESC soldering, Smoke Stopper tests #1 & #2, soft-mounted FC).
    - Betaflight setup walkthrough: Ports, Configuration, Receiver, Modes, Motors (Props Out), and OSD.
    - The PID control loop explained: Proportional (muscle), Integral (memory), Derivative (shock absorber), Feedforward (predictor).
    - **Interactive HTML5 Canvas PID Step Response Visualizer** (adjust P and D sliders to see underdamped, overdamped, and critically damped curves).

12. **Chapter 12: Competition Prep, Execution & Conclusion**
    - RaceBand frequency management (R1–R8, 37MHz minimum channel separation rule to avoid intermodulation distortion IMD).
    - The Golden Pit Rule: Never power up on active channels in the pit area.
    - Race timing transponders and battery warming strategy.
    - **Interactive 12-Point Master Pre-Flight Checklist** with live progress tracking and completion celebration.
    - DGCA India Digital Sky / FAA Part 107 regulations and ethical flying guidelines.

---

## 💻 Desktop Launcher

The app can be launched directly from your desktop:
- **Desktop Shortcut:** `/home/amogh/Desktop/ClubDroneAcademy.desktop`
- **Standalone HTML:** `/home/amogh/Desktop/DroneAcademy.html`
- **Project Location:** `/home/amogh/projects/Club/Drone/index.html`

Run via terminal anytime:
\`\`\`bash
/home/amogh/projects/Club/Drone/launch_app.sh
\`\`\`
Or open directly with any browser:
\`\`\`bash
xdg-open /home/amogh/Desktop/DroneAcademy.html
\`\`\`

---

## 🛠️ Offline & Self-Contained Design
- 100% self-contained single HTML file architecture.
- Real-time client-side hash routing (`#home`, `#ch1` through `#ch12`).
- Course progress persisted automatically in `localStorage`.
- Responsive design: optimized for both desktop widescreen and mobile smartphones.
- Zero build tools or server required — works directly via `file://`.
