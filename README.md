# 🛸 ARC Drone

> **Modern Interactive FPV Robotics, Aeronautical Engineering & Flight Mastery Platform**  
> *"You're gonna learn something today!"* — Inspired by Joshua Bardwell, Oscar Liang, and the open-source FPV multirotor engineering community.

Welcome to **ARC Drone**, a clean, modern, multi-page interactive learning application inspired by Brilliant.org, Khan Academy, and Codecademy. It teaches every aspect of FPV quadcopters: piloting dynamics, size classes, Newtonian flight physics, component selection with real math, electronics, step-by-step soldering, Betaflight logic, and race competition execution.

---

## 🌐 Live Hosted Links (GitHub Pages)

The application is deployed live and hosted globally on GitHub Pages:

- 🎓 **Student Learning Academy (Public):**  
  👉 **[https://amogh-n-betageri.github.io/Club-Drone-Academy/](https://amogh-n-betageri.github.io/Club-Drone-Academy/)**

- 🛡️ **Instructor & Admin Command Center (Password-Protected):**  
  👉 **[https://amogh-n-betageri.github.io/Club-Drone-Academy/admin.html](https://amogh-n-betageri.github.io/Club-Drone-Academy/admin.html)**  
  *(Default Administrator Passcode: `admin123`)*

- 📦 **GitHub Source Repository:**  
  👉 **[https://github.com/Amogh-N-Betageri/Club-Drone-Academy](https://github.com/Amogh-N-Betageri/Club-Drone-Academy)**

---

## 🌟 Security & Privacy Architecture

### 1. Isolated Student Application (`index.html`)
- All references and links to the Instructor Dashboard have been **completely removed** from the student app.
- Students cannot navigate to or discover the admin portal from the learning interface.
- **Mandatory Student Sign-in**: Guest login has been completely removed. Every student must register with their Full Name and Email address to track individual lesson completion and Q&A exam scores in the database.

### 2. Password-Protected Instructor Command Center (`admin.html`)
- The instructor portal is protected behind an **Administrator Verification Gate**.
- Requires the admin passcode (`admin123` by default) before loading or displaying any student data.
- Includes a **Lock & Sign Out** button to re-arm the security gate immediately after reviewing student records.
- Features:
  - Roster of all enrolled students with live progress percentages.
  - Drill-down **"Inspect"** view to review chapter completion and Q&A answers per student.
  - One-click **Export CSV Report** to download full progress spreadsheets.
  - **Import Records** modal for merging student progress exports.

---

## 📺 26 Contextual Video Tutorials (Embedded by Sub-Topic)

Tutorials from **Joshua Bardwell** are embedded directly adjacent to their specific conceptual topics across all 12 chapters:

- **Chapter 1: FPV Piloting & Flight Dynamics**
  - *Angle vs Acro Mode:* `fiUSJgQOkOA` (Should I Learn Acro or Angle First As A New FPV Pilot?)
  - *Simulator Practice:* `SpuXqNakP2A` (Learn to Fly an FPV Drone TODAY - Beginner Simulator Guide)
- **Chapter 2: Types of Drones & Airframe Geometry**
  - *Size Classes (5" vs Sub-250g):* `SC556vEMoYs` (Sub-250g or 5 Inch FPV Drone Kit? Which To Get?)
  - *Frame Geometry (True-X vs Deadcat):* `rzpizzr3SH0` (What Downsides Do Deadcat Frames Actually Have?)
- **Chapter 3: Physics of Multirotor Flight & Calculations**
  - *Newton's Laws & Dynamics:* `SpuXqNakP2A` (How Quadcopters Fly & Momentum Dynamics)
  - *Thrust-to-Weight Ratio:* `6t4gS-HfqT0` (Thrust to Weight Ratio for FPV Drones - How Much Power Do You Need?)
- **Chapter 4: Master Drone Spec Selection (Why Each Spec is Chosen)**
  - *5-Inch Component Sizing:* `SC556vEMoYs` (How to Choose Parts for a 5-Inch FPV Drone Kit)
  - *6S vs 4S Voltage System:* `n8epgP7jlrk` (4S vs 6S LiPo Batteries - Which Do I Buy as a New Pilot?)
- **Chapter 5: Motors: The Electromechanical Powerplant**
  - *Stator Size (2207 vs 2306):* `Wxpa-1FrbYM` (2306 vs 2207 Motor Size Comparison for FPV Mini Quad)
  - *Motor KV & Voltage Matching:* `E6nsJpuaTQc` (How Do You Choose Motor KV for a Build?)
- **Chapter 6: Propellers: Aerodynamics & Thrust**
  - *Pitch & Diameter Selection:* `p09s3f9K6s0` (How to Choose FPV Drone Propellers: Pitch and Diameter)
  - *Props Out Reversed Rotation:* `bZL-BBl9JnE` (Props-In Standard vs Props-Out Reversed - Which Is Better?)
- **Chapter 7: Electronic Speed Controller (ESC) & Power Electronics**
  - *ESC Sizing & Selection:* `NoiqODFwU68` (How Do I Pick An ESC For My Flight Controller?)
  - *Low-ESR Capacitor Mounting:* `kdPfiZ37nKs` (Best Way to Mount Your Capacitor on ESC or XT60)
  - *Bidirectional DShot Telemetry:* `2tvWimtmgd4` (How Does Betaflight RPM Filtering Work?)
- **Chapter 8: Flight Controller: Architecture & Logic**
  - *F7 vs F4 Processors:* `gryW-L_U9S8` (What Are The Benefits Of An F7 Flight Controller Over An F4?)
  - *Wiring & Soft-Mounting:* `QhW-0ddGJ7A` (How to Wire a Flight Controller and Soft Mount)
- **Chapter 9: Battery Power Systems & LiPo Chemistry**
  - *LiPo Safety & Charging:* `lZKoW_ekAu0` (How to Charge and Handle LiPo Batteries Safely)
  - *Internal Resistance (IR):* `uBPuwOyh3do` (LiPo Internal Resistance & C-Rating Truth)
- **Chapter 10: FPV Video & Radio Link Systems**
  - *Video Goggles Comparison:* `TMOeIQ4VRX4` (Best FPV Goggles Buyer Guide: DJI vs HDZero vs Walksnail vs Analog)
  - *Antenna Polarization (RHCP vs LHCP):* `mbHl3DgnN4k` (Left vs Right Circular Polarization)
  - *ExpressLRS RC Protocol:* `oHA2qhABamc` (Why I Always Bind ELRS - ExpressLRS Setup Guide)
- **Chapter 11: Assembling the Drone & Betaflight Software**
  - *Step-by-Step Soldering:* `kfhHecJsS3Y` (Build an FPV Drone Step by Step - Soldering & Assembly)
  - *Smoke Stopper Testing:* `I5a0TAmEwLE` (Why You Need a Smoke Stopper to Prevent Fires)
  - *Betaflight Configuration:* `tNwHNYgWnp8` (Final Betaflight Setup & Motor Direction Check)
  - *PID Loop Tuning:* `M-6pq1rFtBI` (Should I Learn to PID Tune or Use Betaflight Presets?)
- **Chapter 12: Competition Prep, Execution & Conclusion**
  - *RaceBand Frequencies & Pit Mode:* `DwcE68FmFrE` (What Are The Best Frequencies to Use For FPV?)
  - *Failsafe Testing:* `O5ngG--_pKo` (Failsafe Setup and Test in Betaflight to Prevent Flyaways)

---

## 💻 Local Desktop Access & Multi-PC Sharing

- **Student App (This PC):** Double-click [`ClubDroneAcademy.desktop`](file:///home/amogh/Desktop/ClubDroneAcademy.desktop) or open `http://localhost:5000/index.html`
- **Instructor Dashboard (This PC):** Double-click [`DroneAcademyAdmin.desktop`](file:///home/amogh/Desktop/DroneAcademyAdmin.desktop) or open `http://localhost:5000/admin.html`
- **Start Local Server:** `python3 server.py` (Runs on port 5000 with SQLite database `drone_academy.db`)

### 🏠 Connecting Other PCs on the Same Wi-Fi Network (Lab / Classroom)
When students and the instructor are on the same Wi-Fi:
1. Run `python3 server.py` on the instructor's PC (detects your Wi-Fi IP automatically, e.g. `192.168.1.4`).
2. Students on other computers or phones open:  
   👉 `http://<YOUR_IP>:5000/index.html` (e.g. `http://192.168.1.4:5000/index.html`)
3. The instructor opens:  
   👉 `http://<YOUR_IP>:5000/admin.html` (or `http://localhost:5000/admin.html`)
4. All student logins, lessons mastered, and Q&A scores sync directly into the instructor's SQLite database in real time!

### 🌐 Connecting Other PCs Across the Internet (GitHub Pages + Cloud Database)
Because GitHub Pages is a static host, you can connect a **free Google Firebase Realtime Database**:
1. Go to [console.firebase.google.com](https://console.firebase.google.com/) and create a free project (`arc-drone`).
2. In the sidebar under **Build**, click **Realtime Database** &rarr; **Create Database** &rarr; select **"Start in test mode"**.
3. Copy your database URL (`https://your-project-default-rtdb.firebaseio.com/`).
4. In the Admin Portal, click **⚙️ Database & Multi-PC** &rarr; paste the URL into **Cloud Database URL** &rarr; click **Save & Test**.
5. All students accessing via GitHub Pages will now sync their progress and appear in your Admin Portal globally!
