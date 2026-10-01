#!/usr/bin/env python3
"""
Complete Builder for Club Drone Academy Interactive Web Application
Generates index.html and desktop standalone version with 12 comprehensive chapters,
deep technical spec explanations, multi-page client-side router, and 12+ interactive widgets.
"""

import os
import shutil

OUTPUT_PATHS = [
    "/home/amogh/projects/Club/Drone/index.html",
    "/home/amogh/Desktop/DroneAcademy.html"
]

def get_full_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<title>ARC Drone | Master FPV Drone Engineering & Flight</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&display=swap');
  
  :root {
    --bg-deep: #080C14;
    --bg-surface: #111827;
    --bg-card: #182234;
    --bg-hover: #223048;
    --border: rgba(255, 255, 255, 0.08);
    --border-accent: rgba(99, 102, 241, 0.35);
    --text-primary: #F8FAFC;
    --text-secondary: #94A3B8;
    --text-muted: #64748B;
    --accent-blue: #3B82F6;
    --accent-indigo: #6366F1;
    --accent-cyan: #06B6D4;
    --accent-emerald: #10B981;
    --accent-amber: #F59E0B;
    --accent-rose: #F43F5E;
    --accent-violet: #8B5CF6;
  }
  
  * { box-sizing: border-box; margin: 0; padding: 0; }
  
  body {
    font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
    background: var(--bg-deep);
    color: var(--text-primary);
    line-height: 1.7;
    font-size: 16px;
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
  }
  
  .mono { font-family: 'JetBrains Mono', monospace; }
  .content-width { max-width: 820px; margin: 0 auto; padding: 0 1.25rem; }
  
  .page { display: none; }
  .page.active { display: block; }
  
  /* Top App Header */
  .app-header {
    position: sticky; top: 0; z-index: 50;
    background: rgba(8, 12, 20, 0.9);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    padding: 0.75rem 1.25rem;
  }
  
  .progress-track {
    background: rgba(255, 255, 255, 0.08);
    border-radius: 9999px;
    height: 8px;
    overflow: hidden;
  }
  .progress-fill {
    background: linear-gradient(90deg, #3B82F6, #6366F1, #8B5CF6);
    height: 100%;
    border-radius: 9999px;
    transition: width 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }
  
  /* Chapter Cards on Home Page */
  .chapter-card {
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 1.35rem 1.5rem;
    cursor: pointer;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    display: flex; align-items: center; gap: 1.25rem;
  }
  .chapter-card:hover {
    background: var(--bg-card);
    border-color: var(--border-accent);
    transform: translateY(-2px);
    box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3), 0 0 15px rgba(99, 102, 241, 0.15);
  }
  .chapter-card.completed {
    border-left: 4px solid var(--accent-emerald);
  }
  
  .chapter-icon {
    width: 50px; height: 50px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 24px; flex-shrink: 0;
  }
  
  /* Callout Boxes */
  .tip-box {
    border-left: 4px solid var(--accent-blue);
    background: rgba(59, 130, 246, 0.09);
    border-radius: 0 14px 14px 0;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }
  .warn-box {
    border-left: 4px solid var(--accent-amber);
    background: rgba(245, 158, 11, 0.09);
    border-radius: 0 14px 14px 0;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }
  .danger-box {
    border-left: 4px solid var(--accent-rose);
    background: rgba(244, 63, 94, 0.09);
    border-radius: 0 14px 14px 0;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }
  .spec-box {
    border-left: 4px solid var(--accent-indigo);
    background: rgba(99, 102, 241, 0.09);
    border-radius: 0 14px 14px 0;
    padding: 1rem 1.25rem;
    margin: 1.5rem 0;
  }
  
  .box-label {
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    margin-bottom: 0.35rem;
    display: flex;
    align-items: center;
    gap: 0.4rem;
  }
  
  /* Interactive Widgets */
  .widget-card {
    background: #0D1424;
    border: 1px solid rgba(99, 102, 241, 0.25);
    border-radius: 18px;
    padding: 1.75rem;
    margin: 2rem 0;
    box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
  }
  .widget-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.25rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.06);
    padding-bottom: 0.75rem;
  }
  .widget-title {
    color: var(--accent-indigo);
    font-size: 18px;
    font-weight: 700;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  
  /* Sliders & Inputs */
  input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 8px;
    background: rgba(255, 255, 255, 0.12);
    border-radius: 9999px;
    outline: none;
    cursor: pointer;
  }
  input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 22px;
    height: 22px;
    background: var(--accent-blue);
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 0 12px rgba(59, 130, 246, 0.6);
    transition: transform 0.15s ease, background 0.15s ease;
  }
  input[type="range"]::-webkit-slider-thumb:hover {
    transform: scale(1.15);
    background: #60A5FA;
  }
  input[type="range"]::-moz-range-thumb {
    width: 22px;
    height: 22px;
    background: var(--accent-blue);
    border-radius: 50%;
    cursor: pointer;
    border: none;
    box-shadow: 0 0 12px rgba(59, 130, 246, 0.6);
  }
  
  /* Buttons */
  .btn-primary {
    background: linear-gradient(135deg, #2563EB, #6366F1);
    color: white;
    padding: 0.75rem 1.75rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    border: none;
    transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(37, 99, 235, 0.4);
  }
  
  .btn-secondary {
    background: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border);
    padding: 0.75rem 1.5rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  .btn-secondary:hover {
    background: var(--bg-hover);
    border-color: rgba(255, 255, 255, 0.2);
  }
  
  .btn-emerald {
    background: linear-gradient(135deg, #059669, #10B981);
    color: white;
    padding: 0.75rem 1.75rem;
    border-radius: 12px;
    font-weight: 600;
    font-size: 15px;
    cursor: pointer;
    border: none;
    transition: all 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }
  .btn-emerald:hover {
    box-shadow: 0 6px 20px rgba(16, 185, 129, 0.35);
    transform: translateY(-2px);
  }

  /* Data Tables */
  .data-table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.25rem 0;
    font-size: 14px;
    border-radius: 12px;
    overflow: hidden;
    border: 1px solid var(--border);
  }
  .data-table th {
    background: rgba(99, 102, 241, 0.12);
    color: #A5B4FC;
    font-weight: 600;
    text-align: left;
    padding: 0.75rem 1rem;
    border-bottom: 1px solid rgba(99, 102, 241, 0.25);
  }
  .data-table td {
    padding: 0.75rem 1rem;
    border-bottom: 1px solid var(--border);
    color: var(--text-secondary);
  }
  .data-table tr:hover td {
    background: rgba(255, 255, 255, 0.03);
  }
  .data-table tr:last-child td {
    border-bottom: none;
  }

  /* Section Styling */
  .ch-section { margin-bottom: 2.75rem; }
  .ch-section h2 {
    font-size: 22px;
    font-weight: 700;
    margin-bottom: 0.85rem;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .ch-section h3 {
    font-size: 17px;
    font-weight: 600;
    margin: 1.25rem 0 0.5rem;
    color: #E2E8F0;
  }
  .ch-section p {
    color: var(--text-secondary);
    margin-bottom: 1rem;
  }
  .ch-section ul, .ch-section ol {
    color: var(--text-secondary);
    padding-left: 1.5rem;
    margin-bottom: 1.25rem;
  }
  .ch-section li { margin-bottom: 0.5rem; }

  /* Formula display */
  .formula-card {
    background: #0B111D;
    border: 1px solid rgba(99, 102, 241, 0.2);
    border-radius: 12px;
    padding: 1rem 1.25rem;
    margin: 1rem 0;
    font-family: 'JetBrains Mono', monospace;
    font-size: 15px;
    color: #818CF8;
    text-align: center;
  }

  /* Calculation Outputs */
  .calc-metric-box {
    background: rgba(30, 41, 59, 0.6);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
    flex: 1;
    min-width: 140px;
  }
  .calc-metric-val {
    font-size: 26px;
    font-weight: 800;
    color: var(--accent-blue);
    line-height: 1.2;
    margin: 0.25rem 0;
  }
  .calc-metric-lbl {
    font-size: 12px;
    text-transform: uppercase;
    color: var(--text-muted);
    font-weight: 600;
    letter-spacing: 0.05em;
  }

  /* Segmented Toggle Pills */
  .seg-tabs {
    display: flex;
    border-radius: 12px;
    border: 1px solid var(--border);
    background: var(--bg-surface);
    overflow: hidden;
    margin: 1rem 0;
  }
  .seg-tab {
    flex: 1;
    padding: 0.65rem 0.85rem;
    text-align: center;
    font-size: 14px;
    font-weight: 500;
    color: var(--text-secondary);
    cursor: pointer;
    transition: all 0.2s;
    border: none;
    background: transparent;
  }
  .seg-tab.active {
    background: var(--accent-blue);
    color: white;
    font-weight: 600;
  }

  /* Interactive Checklist */
  .check-row {
    display: flex;
    align-items: center;
    gap: 0.85rem;
    padding: 0.85rem 1.15rem;
    background: var(--bg-surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    margin-bottom: 0.65rem;
    cursor: pointer;
    transition: all 0.2s ease;
  }
  .check-row:hover {
    background: var(--bg-card);
    border-color: rgba(255, 255, 255, 0.15);
  }
  .check-row.done {
    background: rgba(16, 185, 129, 0.08);
    border-color: rgba(16, 185, 129, 0.3);
  }
  .check-circle {
    width: 24px;
    height: 24px;
    border-radius: 50%;
    border: 2px solid var(--text-muted);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 12px;
    font-weight: bold;
    flex-shrink: 0;
    transition: all 0.2s;
  }
  .check-row.done .check-circle {
    background: var(--accent-emerald);
    border-color: var(--accent-emerald);
    color: white;
  }

  /* Mobile Drawer */
  .mobile-drawer {
    position: fixed; top: 0; left: -320px; width: 300px; height: 100vh;
    background: var(--bg-surface);
    z-index: 100;
    transition: left 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    overflow-y: auto;
    border-right: 1px solid var(--border);
    padding: 1.25rem;
  }
  .mobile-drawer.open { left: 0; }
  .drawer-overlay {
    position: fixed; inset: 0;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(4px);
    z-index: 99;
    display: none;
  }
  .drawer-overlay.show { display: block; }

  /* Selection Dropdowns */
  .spec-select {
    width: 100%;
    background: var(--bg-surface);
    color: var(--text-primary);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 0.65rem 0.85rem;
    font-size: 14px;
    outline: none;
    transition: border-color 0.2s;
  }
  .spec-select:focus { border-color: var(--accent-blue); }

  /* Interactive Virtual Stick */
  .stick-gimbal {
    width: 140px; height: 140px;
    background: #090D16;
    border: 2px solid rgba(255, 255, 255, 0.12);
    border-radius: 50%;
    position: relative;
    cursor: crosshair;
    touch-action: none;
    user-select: none;
  }
  .stick-pointer {
    width: 28px; height: 28px;
    background: radial-gradient(circle at 35% 35%, #60A5FA, #2563EB);
    border-radius: 50%;
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    box-shadow: 0 0 10px rgba(59, 130, 246, 0.8);
    pointer-events: none;
    transition: transform 0.05s ease-out;
  }

  
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

  /* Animation */
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(12px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .fade-in { animation: fadeIn 0.35s ease-out; }
  
  /* Scrollbar */
  ::-webkit-scrollbar { width: 8px; }
  ::-webkit-scrollbar-track { background: transparent; }
  ::-webkit-scrollbar-thumb { background: rgba(255, 255, 255, 0.15); border-radius: 999px; }
  ::-webkit-scrollbar-thumb:hover { background: rgba(255, 255, 255, 0.25); }
</style>
</head>
<body>

<!-- Mobile Drawer & Overlay -->
<div class="drawer-overlay" id="mobileOverlay" onclick="closeDrawer()"></div>
<div class="mobile-drawer" id="mobileDrawer">
  <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:1.5rem">
    <div style="font-weight:700;font-size:17px;color:#F8FAFC">📋 Lesson Syllabus</div>
    <button onclick="closeDrawer()" style="background:none;border:none;color:var(--text-secondary);font-size:24px;cursor:pointer">&times;</button>
  </div>
  <div id="drawerList" style="display:flex;flex-direction:column;gap:0.4rem"></div>
</div>


<!-- Student Login Modal -->
<div class="modal-overlay" id="loginModal">
  <div class="modal-box" style="text-align:center">
    <div style="font-size:38px;margin-bottom:0.5rem">🚁</div>
    <h2 style="font-size:22px;font-weight:800;color:#F8FAFC;margin-bottom:0.25rem">Welcome to ARC Drone</h2>
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
    <div style="margin-top:1.25rem;padding-top:1rem;border-top:1px solid var(--border);text-align:center;font-size:12px">
      <button onclick="guestContinue()" style="background:none;border:none;color:var(--text-muted);cursor:pointer">Continue as Guest</button>
    </div>
  </div>
</div>

<!-- Persistent Header -->
<header class="app-header">
  <div style="max-width:820px;margin:0 auto;display:flex;align-items:center;gap:1rem">
    <button id="menuBtn" onclick="openDrawer()" style="background:none;border:none;color:var(--text-primary);font-size:22px;cursor:pointer;display:none" title="Open Syllabus">☰</button>
    <button id="backBtn" onclick="navigate('home')" style="background:none;border:none;color:var(--text-secondary);font-size:15px;font-weight:600;cursor:pointer;display:none">← Syllabus</button>
    <a href="#home" style="text-decoration:none;color:var(--text-primary);font-weight:700;font-size:17px;white-space:nowrap;display:flex;align-items:center;gap:0.4rem" onclick="navigate('home')">
      <span>🚁</span> <span class="hidden sm:inline">ARC Drone</span>
      <span style="font-size:10px;font-weight:700;padding:2px 7px;border-radius:6px;background:rgba(16,185,129,0.15);border:1px solid rgba(16,185,129,0.35);color:#34D399;margin-left:4px">v2.5 Live</span>
    </a>
    <div style="flex:1;display:flex;align-items:center;gap:0.75rem;min-width:0;justify-content:flex-end">
      
    <div id="userProfileBadge" style="display:flex;align-items:center;gap:0.4rem;background:var(--bg-surface);border:1px solid var(--border);border-radius:999px;padding:0.25rem 0.65rem;cursor:pointer" onclick="promptSwitchUser()" title="Click to switch student profile">
      <div style="width:22px;height:22px;border-radius:50%;background:var(--accent-blue);color:white;display:flex;align-items:center;justify-content:center;font-size:10px;font-weight:700" id="userAvatarChar">S</div>
      <span style="font-size:12px;font-weight:600;color:#F8FAFC;max-width:85px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap" id="userNameLabel">Student</span>
    </div>

      <div class="progress-track" style="flex:1;max-width:180px"><div class="progress-fill" id="headerProgress" style="width:0%"></div></div>
      <span style="font-size:12px;color:var(--text-secondary);font-weight:600;white-space:nowrap" id="headerProgressText">0/12</span>
    </div>
  </div>
</header>

<!-- ===== HOME / SYLLABUS PAGE ===== -->
<div class="page active" id="page-home">
  <div class="content-width" style="padding-top:2.5rem;padding-bottom:3.5rem">
    <div class="fade-in" style="text-align:center;margin-bottom:2.75rem">
      <div style="display:inline-flex;align-items:center;gap:0.5rem;background:rgba(99,102,241,0.12);border:1px solid rgba(99,102,241,0.25);border-radius:999px;padding:0.35rem 1rem;font-size:13px;font-weight:600;color:#A5B4FC;margin-bottom:1rem">
        <span>⚡</span> Interactive FPV Robotics & Flight Engineering
      </div>
      <h1 style="font-size:36px;font-weight:800;margin-bottom:0.75rem;letter-spacing:-0.02em;background:linear-gradient(135deg,#60A5FA,#818CF8,#C084FC);-webkit-background-clip:text;-webkit-text-fill-color:transparent">
        ARC Drone
      </h1>
      <p style="color:var(--text-secondary);font-size:17px;max-width:580px;margin:0 auto">
        Master every aspect of FPV quadcopters: aerodynamics, electronics selection, Newtonian physics, Betaflight logic, step-by-step soldering, and race strategy.
      </p>
    </div>

    <!-- Overall Progress Card -->
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:18px;padding:1.5rem;margin-bottom:2rem">
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.75rem">
        <div>
          <span style="font-size:12px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.08em">YOUR FLIGHT TRAINING PROGRESS</span>
          <div style="font-size:18px;font-weight:700;color:var(--text-primary);margin-top:0.15rem" id="homeProgressTitle">0 of 12 Chapters Mastered</div>
        </div>
        <span style="font-size:22px;font-weight:800;color:var(--accent-blue)" id="homeProgressPercent">0%</span>
      </div>
      <div class="progress-track" style="height:10px"><div class="progress-fill" id="homeProgressBar" style="width:0%"></div></div>
    </div>

    <!-- Chapters List -->
    <div style="margin-bottom:1rem;display:flex;align-items:center;justify-content:space-between">
      <span style="font-size:14px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em">COURSE CURRICULUM</span>
      <span style="font-size:13px;color:var(--text-secondary)">12 Interactive Lessons</span>
    </div>
    <div id="chapterList" style="display:flex;flex-direction:column;gap:0.85rem"></div>

    <!-- Quick Reference Card -->
    <div style="margin-top:2.5rem;background:#0A1220;border:1px solid rgba(59,130,246,0.2);border-radius:18px;padding:1.5rem">
      <div style="display:flex;align-items:center;gap:0.6rem;margin-bottom:0.75rem">
        <span style="font-size:20px">🛠️</span>
        <h3 style="font-size:16px;font-weight:700;color:#93C5FD;margin:0">Gold Standard 5-Inch 6S Reference Formula</h3>
      </div>
      <p style="font-size:14px;color:var(--text-secondary);margin-bottom:1rem">
        The universal benchmark setup trusted by world champion pilots for freestyle and racing:
      </p>
      <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:0.75rem;font-size:13px">
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">AIRFRAME</span>
          <strong>5-Inch True-X / DC (5mm arms)</strong>
        </div>
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">MOTORS</span>
          <strong>2207 / 2306 (1850–1950 KV)</strong>
        </div>
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">PROPELLERS</span>
          <strong>5.1" × 4.3" × 3 Tri-Blade</strong>
        </div>
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">ESC</span>
          <strong>50A–60A AM32 4-in-1 (6S)</strong>
        </div>
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">BATTERY</span>
          <strong>6S 1100–1300 mAh (100C+)</strong>
        </div>
        <div style="background:var(--bg-surface);padding:0.75rem;border-radius:10px;border:1px solid var(--border)">
          <span style="color:var(--text-muted);display:block;font-size:11px;font-weight:600">RADIO LINK</span>
          <strong>ExpressLRS 2.4GHz (500Hz)</strong>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ===== DYNAMIC CHAPTER VIEW PAGE ===== -->
<div class="page" id="page-chapter">
  <div class="content-width" style="padding-top:2rem;padding-bottom:4rem">
    <div class="fade-in">
      <!-- Breadcrumb & Position -->
      <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:0.5rem">
        <div style="display:flex;align-items:center;gap:0.5rem">
          <a href="#home" onclick="navigate('home')" style="font-size:13px;color:var(--text-muted);text-decoration:none">Syllabus</a>
          <span style="font-size:12px;color:var(--text-muted)">/</span>
          <span style="font-size:12px;text-transform:uppercase;font-weight:700;letter-spacing:0.08em;color:var(--accent-blue)" id="chapterLabel">CHAPTER 1</span>
        </div>
        <span style="font-size:12px;font-weight:600;color:var(--text-muted)" id="chapterPosition">Lesson 1 of 12</span>
      </div>

      <!-- Chapter Title & Subtitle -->
      <h1 style="font-size:30px;font-weight:800;letter-spacing:-0.02em;margin-bottom:0.25rem;color:var(--text-primary)" id="chapterTitle"></h1>
      <p style="font-size:16px;color:var(--text-secondary);margin-bottom:2rem" id="chapterSubtitle"></p>

      <!-- Chapter Dynamic Body -->
      <div id="chapterContent"></div>

      <!-- Bottom Step-by-Step Navigation Bar -->
      <div style="display:flex;align-items:center;justify-content:space-between;gap:1rem;margin-top:3.5rem;padding-top:1.5rem;border-top:1px solid var(--border);flex-wrap:wrap">
        <button class="btn-secondary" id="prevChapterBtn" onclick="prevChapter()">← Previous Lesson</button>
        <div style="display:flex;gap:0.75rem;flex-wrap:wrap">
          <button class="btn-emerald" id="markCompleteBtn" onclick="toggleCompleteCurrent()">✓ Mark Complete</button>
          <button class="btn-primary" id="nextChapterBtn" onclick="nextChapter()">Next Lesson →</button>
        </div>
      </div>
    </div>
  </div>
</div>

<script>
// ==========================================
// COURSE CHAPTER METADATA (12 CHAPTERS)
// ==========================================
const CHAPTERS = [
  { id: 'ch1', icon: '🎯', title: 'FPV Piloting & Flight Dynamics', subtitle: 'Stick controls, flight modes, and camera tilt physics', time: '10 min', color: '#3B82F6' },
  { id: 'ch2', icon: '🏗️', title: 'Types of Drones & Airframe Geometry', subtitle: 'Size classes, carbon fiber, and arm geometries', time: '12 min', color: '#6366F1' },
  { id: 'ch3', icon: '📐', title: 'Physics of Drone Flight & Calculations', subtitle: "Newton's laws, TWR, hover throttle %, and power", time: '14 min', color: '#06B6D4' },
  { id: 'ch4', icon: '🎯', title: 'Master Spec Selection (Why Each Spec is Chosen)', subtitle: 'The formula for matching all parts in harmony', time: '15 min', color: '#10B981' },
  { id: 'ch5', icon: '⚡', title: 'Motors: The Electromechanical Powerplant', subtitle: 'Stator volume, KV constant, and screw safety', time: '12 min', color: '#8B5CF6' },
  { id: 'ch6', icon: '🌀', title: 'Propellers: Aerodynamics & Thrust', subtitle: 'Pitch speed, blade counts, and rotation logic', time: '10 min', color: '#EC4899' },
  { id: 'ch7', icon: '🔌', title: 'ESC & Power Electronics', subtitle: 'MOSFETs, DShot, AM32, and the capacitor', time: '12 min', color: '#F59E0B' },
  { id: 'ch8', icon: '🧠', title: 'Flight Controller: Architecture & Logic', subtitle: 'MCUs, gyros, soft-mounting, and UART routing', time: '12 min', color: '#14B8A6' },
  { id: 'ch9', icon: '🔋', title: 'Battery Power Systems & Chemistry', subtitle: 'LiPo cells, 4S vs 6S physics, and C-ratings', time: '11 min', color: '#EF4444' },
  { id: 'ch10', icon: '📡', title: 'FPV Video & Radio Link Systems', subtitle: 'Video systems, antenna polarization, and ELRS', time: '13 min', color: '#F97316' },
  { id: 'ch11', icon: '🔧', title: 'Assembling the Drone & Software Setup', subtitle: 'Step-by-step soldering, Betaflight, and PID loop', time: '16 min', color: '#A855F7' },
  { id: 'ch12', icon: '🏁', title: 'Competition Prep, Execution & Conclusion', subtitle: 'RaceBand, pit mode, pre-flight checks, and rules', time: '12 min', color: '#3B82F6' }
];


// ==========================================
// VIDEO TUTORIALS & INTERACTIVE Q&A DATABASE
// ==========================================
const CHAPTER_VIDEOS = {
  "ch1": {
    "id": "SpuXqNakP2A",
    "title": "Learn to Fly an FPV Drone TODAY (Beginner Guide)",
    "author": "Joshua Bardwell"
  },
  "ch2": {
    "id": "rzpizzr3SH0",
    "title": "FPV Drone Frame Geometry: True-X vs Deadcat Explained",
    "author": "Joshua Bardwell"
  },
  "ch3": {
    "id": "E6nsJpuaTQc",
    "title": "Multirotor Flight Physics & Motor Thrust Dynamics",
    "author": "Joshua Bardwell"
  },
  "ch4": {
    "id": "SC556vEMoYs",
    "title": "Component Selection Guide: 5-Inch Drone Kit Architecture",
    "author": "Joshua Bardwell"
  },
  "ch5": {
    "id": "E6nsJpuaTQc",
    "title": "How to Choose Motor KV and Stator Size for Your Build",
    "author": "Joshua Bardwell"
  },
  "ch6": {
    "id": "p09s3f9K6s0",
    "title": "How to Choose Propellers: Diameter, Pitch and Blade Count",
    "author": "Joshua Bardwell"
  },
  "ch7": {
    "id": "kdPfiZ37nKs",
    "title": "Why You MUST Put a Low-ESR Capacitor on Your ESC",
    "author": "Joshua Bardwell"
  },
  "ch8": {
    "id": "gryW-L_U9S8",
    "title": "Flight Controller Selection: Benefits of F7 over F4",
    "author": "Joshua Bardwell"
  },
  "ch9": {
    "id": "n8epgP7jlrk",
    "title": "4S vs 6S LiPo Batteries: Which Should You Choose?",
    "author": "Joshua Bardwell"
  },
  "ch10": {
    "id": "TMOeIQ4VRX4",
    "title": "FPV Goggles & Video Systems: DJI vs Walksnail vs HDZero vs Analog",
    "author": "Joshua Bardwell"
  },
  "ch11": {
    "id": "tNwHNYgWnp8",
    "title": "Build an FPV Drone: Final Betaflight Setup & PID Tuning",
    "author": "Joshua Bardwell"
  },
  "ch12": {
    "id": "DwcE68FmFrE",
    "title": "What are the Best Frequencies for FPV? RaceBand & Pit Mode",
    "author": "Joshua Bardwell"
  }
};
const CHAPTER_QNA = {
  "ch1": [
    {
      "q": "In Mode 2 transmitter configuration, which stick controls the drone's Throttle and Yaw?",
      "options": [
        "Right stick",
        "Left stick",
        "Top slider dials",
        "Both sticks simultaneously"
      ],
      "answer": 1,
      "explanation": "In Mode 2, the Left stick controls Throttle (vertical) and Yaw (horizontal), while the Right stick controls Pitch and Roll."
    },
    {
      "q": "Why do FPV racing pilots tilt their onboard camera upward at 30\u00b0 to 50\u00b0?",
      "options": [
        "To look at the sky",
        "To keep the horizon visible when the quadcopter pitches forward at high speed",
        "To reduce propeller drag",
        "To improve antenna range"
      ],
      "answer": 1,
      "explanation": "Multirotors must pitch their nose down to generate forward thrust. An upward-tilted camera keeps the flight path ahead visible."
    }
  ],
  "ch2": [
    {
      "q": "What critical electrical safety hazard does raw carbon fiber pose to drone electronics?",
      "options": [
        "It is magnetic and repels motors",
        "It is electrically conductive and will short-circuit bare solder pads or wires",
        "It blocks all radio waves completely",
        "It melts at room temperature"
      ],
      "answer": 1,
      "explanation": "Carbon fiber is an electrical conductor. If bare solder joints touch the frame, it creates an immediate chassis short-circuit."
    },
    {
      "q": "What is the primary benefit of a Deadcat (DC) frame geometry?",
      "options": [
        "It flies upside down automatically",
        "It clears propellers out of the wide-angle camera field of view (FOV)",
        "It cuts current draw in half",
        "It increases top speed by 50%"
      ],
      "answer": 1,
      "explanation": "Deadcat arms sweep front motors outward and back so spinning propellers do not appear in wide-angle HD camera footage."
    }
  ],
  "ch3": [
    {
      "q": "If a 5-inch drone has an All-Up Weight (AUW) of 600g and each motor produces 1500g of thrust, what is its Thrust-to-Weight Ratio (TWR)?",
      "options": [
        "2.5 : 1",
        "6.0 : 1",
        "10.0 : 1",
        "15.0 : 1"
      ],
      "answer": 2,
      "explanation": "Total thrust = 4 \u00d7 1500g = 6000g. TWR = 6000g / 600g = 10.0 : 1 (Elite competition grade)."
    },
    {
      "q": "How does a quadcopter execute a Yaw rotation to the left without tilting its frame?",
      "options": [
        "By moving physical rudder flaps on the arms",
        "By speeding up the two CW motors and slowing down the two CCW motors",
        "By reversing all four motors",
        "By shifting the battery"
      ],
      "answer": 1,
      "explanation": "Unbalancing reactive torque between clockwise and counter-clockwise motor pairs rotates the aircraft along its Z-axis."
    }
  ],
  "ch4": [
    {
      "q": "Why has the 5-inch FPV community transitioned almost universally to 6S (22.2V) batteries over 4S (14.8V)?",
      "options": [
        "6S batteries are half the weight",
        "Higher voltage requires ~33% less current for the same power, reducing Joule heat losses (I\u00b2R) by over 50% and eliminating voltage sag",
        "6S batteries charge in 5 seconds",
        "4S motors are no longer made"
      ],
      "answer": 1,
      "explanation": "Power = V \u00d7 I. Higher voltage means lower current, which dramatically reduces resistive heating and preserves punchout power."
    },
    {
      "q": "When pairing motors with an ESC, why is it recommended to choose an ESC with at least a 25% current safety margin?",
      "options": [
        "The extra amps make the camera sharper",
        "Motor peak burst current during aggressive punchouts can exceed continuous ratings, causing MOSFET thermal burnout",
        "To make props spin backwards",
        "It is legally required"
      ],
      "answer": 1,
      "explanation": "High G punchouts push motor current draw to its limits; 25%+ headroom prevents blown MOSFETs."
    }
  ],
  "ch5": [
    {
      "q": "In motor nomenclature, what does the designation '2207' signify?",
      "options": [
        "2200 KV and 7 Volts",
        "22mm stator diameter and 7mm stator height",
        "22 turns of copper wire and 0.7mm magnet thickness",
        "220 grams of thrust on 7-inch props"
      ],
      "answer": 1,
      "explanation": "The first two digits specify stator diameter (mm) and the last two digits specify stator height (mm)."
    },
    {
      "q": "What catastrophe occurs if motor mounting screws are too long and penetrate the stator base?",
      "options": [
        "The motor spins too slowly",
        "Screws puncture the enameled copper stator windings, creating an instant dead short that destroys motor and ESC",
        "The prop locknut cannot be tightened",
        "The gyro gets reversed"
      ],
      "answer": 1,
      "explanation": "Motor screw length must never exceed the arm thickness plus motor base plate (~7-8mm total)."
    }
  ],
  "ch6": [
    {
      "q": "What theoretical distance would a '5146' propeller advance in one complete revolution?",
      "options": [
        "5.1 inches",
        "4.6 inches",
        "51.46 millimeters",
        "46 centimeters"
      ],
      "answer": 1,
      "explanation": "In the 5146 code, '46' represents the pitch: 4.6 inches of linear forward travel per revolution."
    },
    {
      "q": "Why do most modern pilots configure their Betaflight rotation to 'Props Out' (Reversed Rotation)?",
      "options": [
        "It doubles the top speed",
        "Front blades spin outward, deflecting dirt, moisture, and gate clips away from the camera lens and airframe",
        "Motors consume zero current",
        "It eliminates the flight controller"
      ],
      "answer": 1,
      "explanation": "Props Out throws grass and debris away from the FPV camera and pushes the drone off obstacles in gate collisions."
    }
  ],
  "ch7": [
    {
      "q": "Why is it strictly mandatory to solder a Low-ESR electrolytic capacitor across the ESC battery pads?",
      "options": [
        "To make the battery charge faster",
        "To absorb massive inductive voltage spikes (45V\u201355V on 6S) created by active motor braking that would otherwise fry electronics",
        "To provide 5 minutes of emergency power",
        "To filter microphone audio noise"
      ],
      "answer": 1,
      "explanation": "Active motor braking dumps inductive back-EMF energy back onto the power rail; the Low-ESR capacitor clamps these destructive spikes."
    },
    {
      "q": "What is the primary benefit of Bidirectional DShot telemetry between ESC and FC?",
      "options": [
        "It allows you to play music on motors",
        "The ESC streams exact motor RPM back to the FC, enabling dynamic RPM notch filtering of motor vibrations",
        "It charges the radio transmitter while flying",
        "It replaces the radio receiver"
      ],
      "answer": 1,
      "explanation": "Bidirectional DShot enables Betaflight to position dynamic notch filters exactly on motor frequencies, creating ultra-clean gyro signals."
    }
  ],
  "ch8": [
    {
      "q": "Why should a Flight Controller always be soft-mounted on silicone grommets rather than bolted rigidly to carbon fiber?",
      "options": [
        "To prevent the board from falling out",
        "To mechanically isolate the sensitive gyroscope from motor vibration harmonics that cause filter saturation and hot motors",
        "To increase electrical grounding conductivity",
        "To allow the USB port to bend"
      ],
      "answer": 1,
      "explanation": "High-frequency motor vibrations will saturate the gyro sensor without silicone dampeners, causing the D-term to overheat motors."
    },
    {
      "q": "What is the golden rule when soldering a serial receiver (UART) to a flight controller?",
      "options": [
        "Connect TX to TX, and RX to RX",
        "Connect TX to RX, and RX to TX (crossover)",
        "Connect both wires to battery positive",
        "Only connect the ground wire"
      ],
      "answer": 1,
      "explanation": "Serial communications cross over: Transmitter Transmit (TX) line feeds into Receiver Receive (RX) line."
    }
  ],
  "ch9": [
    {
      "q": "At what voltage per cell should a LiPo battery pack be stored when not flying for more than 24 hours?",
      "options": [
        "4.20V per cell (Fully charged)",
        "3.80V \u2013 3.85V per cell (Storage voltage)",
        "3.00V per cell (Fully empty)",
        "0.00V per cell"
      ],
      "answer": 1,
      "explanation": "Storing LiPos at 3.80V\u20133.85V maintains chemical equilibrium, preventing metallic lithium plating and cell degradation."
    },
    {
      "q": "What physical metric provides the most honest indicator of a LiPo battery pack's real health and performance?",
      "options": [
        "The color of the plastic shrink wrap",
        "Internal Resistance (IR) measured in milliohms (m\u03a9) per cell",
        "The printed manufacturer C-rating sticker",
        "How hot the pack gets during charging"
      ],
      "answer": 1,
      "explanation": "Advertised C-ratings are often inflated; low internal resistance (1.5\u20133m\u03a9) is the true mark of a healthy high-discharge pack."
    }
  ],
  "ch10": [
    {
      "q": "What catastrophic signal loss occurs if you use an RHCP antenna on your drone and an LHCP antenna on your goggles?",
      "options": [
        "Video colors become inverted",
        "An immediate 20dB to 30dB cross-polarization penalty occurs, destroying over 90% of your operational video range",
        "The VTX will explode instantly",
        "The goggles turn off"
      ],
      "answer": 1,
      "explanation": "Mismatching circular polarization causes the receiving antenna to actively reject the signal, drastically cutting range."
    },
    {
      "q": "Why is ExpressLRS (ELRS) 2.4GHz preferred over legacy 50Hz radio protocols for competitive FPV?",
      "options": [
        "It requires no antennas",
        "It offers sub-3ms latency, packet rates up to 1000Hz, and extreme long range using open-source LoRa technology",
        "It is manufactured exclusively by DJI",
        "It works without a battery"
      ],
      "answer": 1,
      "explanation": "ELRS combines ultra-high packet rates (up to 1000Hz) with sub-3ms stick-to-motor latency and immense penetration range."
    }
  ],
  "ch11": [
    {
      "q": "What should you ALWAYS do before connecting a drone to the computer and configuring motors in Betaflight?",
      "options": [
        "Charge the battery to 100%",
        "REMOVE ALL PROPELLERS from the motors",
        "Turn off your radio transmitter",
        "Solder the antenna directly to the carbon frame"
      ],
      "answer": 1,
      "explanation": "Accidental motor spin-up on the workbench with propellers on causes severe lacerations and physical injury. Always remove props!"
    },
    {
      "q": "In Betaflight PID tuning, what is the role of the 'D' (Derivative) gain?",
      "options": [
        "To increase raw top speed",
        "To act as a shock absorber that dampens P-term overshoot and prevents oscillations after quick flips",
        "To correct for steady wind drift over several seconds",
        "To make the beeper louder"
      ],
      "answer": 1,
      "explanation": "The D-term measures the rate of error change, acting like a dynamic shock absorber to prevent P-term overshoot."
    }
  ],
  "ch12": [
    {
      "q": "Why does the international FPV racing community use the 8 RaceBand frequencies with a strict 37MHz minimum channel separation?",
      "options": [
        "To comply with FM radio music stations",
        "To prevent third-order Intermodulation Distortion (IMD) products from video transmitters jamming neighboring pilots",
        "Because only 8 drones can fit in the air physically",
        "To lower battery consumption"
      ],
      "answer": 1,
      "explanation": "Non-linear RF mixing generates IMD interference spikes; 37MHz minimum spacing ensures 8 pilots can fly simultaneously with clear video."
    },
    {
      "q": "What is the maximum legal recreational altitude for drone flight under DGCA (India) and FAA (USA) aviation regulations?",
      "options": [
        "30 meters (100 feet) AGL",
        "120 meters (400 feet) AGL",
        "500 meters (1640 feet) AGL",
        "Unlimited in all airspace"
      ],
      "answer": 1,
      "explanation": "Recreational drones must stay below 120m (400ft) Above Ground Level to remain well clear of manned civil aviation."
    }
  ]
};

let currentUser = JSON.parse(localStorage.getItem('droneAcademy_activeUser') || 'null');
let userQnaScores = JSON.parse(localStorage.getItem('clubDroneAcademy_qna') || '{}');


function getQnaSectionHtml(id) {
  const questions = CHAPTER_QNA[id];
  if (!questions || questions.length === 0) return '';

  const saved = userQnaScores[id] || { answers: {} };

  return `
    <div class="ch-section">
      <h2>📝 Lesson Knowledge Check & Q&A</h2>
      <p style="font-size:14px;color:var(--text-secondary);margin-bottom:1rem">
        Answer the following technical questions to verify your comprehension. Your answers are automatically saved to your profile:
      </p>

      <div class="widget-card" style="margin-top:0.5rem">
        <div class="widget-header">
          <span class="widget-title">🧠 Examination & Mastery Check</span>
          <span style="font-size:12px;color:var(--text-muted)" id="qnaScoreBadge_${id}">
            ${saved.score !== undefined ? `Score: ${saved.score} / ${questions.length}` : `2 Questions`}
          </span>
        </div>

        <div style="display:flex;flex-direction:column;gap:1.5rem">
          ${questions.map((q, qIdx) => {
            const selectedOpt = saved.answers ? saved.answers[qIdx] : undefined;
            return `
              <div>
                <div style="font-size:14px;font-weight:700;color:#F8FAFC;margin-bottom:0.75rem">
                  ${qIdx + 1}. ${q.q}
                </div>
                <div id="qnaOptions_${id}_${qIdx}">
                  ${q.options.map((opt, optIdx) => {
                    let optClass = 'qna-opt';
                    if (selectedOpt !== undefined) {
                      if (optIdx === q.answer) optClass += ' correct';
                      else if (selectedOpt === optIdx) optClass += ' wrong';
                    }
                    return `
                      <div class="${optClass}" onclick="selectQnaOption('${id}', ${qIdx}, ${optIdx})">
                        <span style="font-weight:600;margin-right:0.4rem">${String.fromCharCode(65 + optIdx)}.</span> ${opt}
                      </div>
                    `;
                  }).join('')}
                </div>
                <div id="qnaFeedback_${id}_${qIdx}" style="font-size:12px;margin-top:0.4rem;${selectedOpt !== undefined ? 'display:block' : 'display:none'}">
                  <div style="padding:0.6rem 0.85rem;border-radius:8px;background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.2);color:var(--text-secondary)">
                    <strong>💡 Explanation:</strong> ${q.explanation}
                  </div>
                </div>
              </div>
            `;
          }).join('')}
        </div>
      </div>
    </div>
  `;
}

function selectQnaOption(chId, qIdx, optIdx) {
  const questions = CHAPTER_QNA[chId];
  if (!questions) return;
  const q = questions[qIdx];

  if (!userQnaScores[chId]) {
    userQnaScores[chId] = { answers: {}, score: 0, total: questions.length };
  }

  userQnaScores[chId].answers[qIdx] = optIdx;

  // Recalculate chapter score
  let correctCount = 0;
  questions.forEach((question, idx) => {
    if (userQnaScores[chId].answers[idx] === question.answer) {
      correctCount++;
    }
  });
  userQnaScores[chId].score = correctCount;
  userQnaScores[chId].total = questions.length;

  localStorage.setItem('clubDroneAcademy_qna', JSON.stringify(userQnaScores));

  // Update UI options
  const optContainer = document.getElementById(`qnaOptions_${chId}_${qIdx}`);
  if (optContainer) {
    const options = optContainer.querySelectorAll('.qna-opt');
    options.forEach((el, i) => {
      el.classList.remove('correct', 'wrong');
      if (i === q.answer) el.classList.add('correct');
      else if (i === optIdx) el.classList.add('wrong');
    });
  }

  // Show feedback
  const feedbackEl = document.getElementById(`qnaFeedback_${chId}_${qIdx}`);
  if (feedbackEl) feedbackEl.style.display = 'block';

  // Update score badge
  const badge = document.getElementById(`qnaScoreBadge_${chId}`);
  if (badge) badge.textContent = `Score: ${correctCount} / ${questions.length}`;

  syncWithDatabase();
}

function checkLogin() {
  if (!currentUser) {
    document.getElementById('loginModal').classList.add('open');
  } else {
    updateHeaderProfile();
    syncWithDatabase();
  }
}

async function submitLogin() {
  const name = document.getElementById('loginName').value.trim();
  const email = document.getElementById('loginEmail').value.trim();

  if (!name || !email) {
    alert('Please enter both your name and email to proceed.');
    return;
  }

  currentUser = { name, email, loggedInAt: new Date().toISOString() };
  localStorage.setItem('droneAcademy_activeUser', JSON.stringify(currentUser));
  document.getElementById('loginModal').classList.remove('open');
  updateHeaderProfile();

  // Attempt sync with server
  try {
    const res = await fetch('/api/login', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name, email })
    });
    if (res.ok) {
      const data = await res.json();
      if (data.student) {
        // Merge progress from server if exists
        if (data.student.completed_chapters && data.student.completed_chapters.length > 0) {
          data.student.completed_chapters.forEach(ch => progress[ch] = true);
          localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  syncWithDatabase();
        }
        if (data.student.qna_scores && Object.keys(data.student.qna_scores).length > 0) {
          userQnaScores = Object.assign(userQnaScores, data.student.qna_scores);
          localStorage.setItem('clubDroneAcademy_qna', JSON.stringify(userQnaScores));
        }
        updateCourseProgress();
      }
    }
  } catch (e) {
    console.log('Server offline; using local database storage');
  }

  syncWithDatabase();
}

function guestContinue() {
  currentUser = { name: 'Guest Student', email: 'guest@droneacademy.local', loggedInAt: new Date().toISOString() };
  localStorage.setItem('droneAcademy_activeUser', JSON.stringify(currentUser));
  document.getElementById('loginModal').classList.remove('open');
  updateHeaderProfile();
}

function promptSwitchUser() {
  const name = currentUser ? currentUser.name : '';
  const email = currentUser ? currentUser.email : '';
  if (confirm(`Currently signed in as: ${name} (${email})\n\nDo you want to switch student profile or sign in as someone else?`)) {
    document.getElementById('loginName').value = '';
    document.getElementById('loginEmail').value = '';
    document.getElementById('loginModal').classList.add('open');
  }
}

function updateHeaderProfile() {
  const avatar = document.getElementById('userAvatarChar');
  const label = document.getElementById('userNameLabel');
  if (currentUser && currentUser.name) {
    avatar.textContent = currentUser.name.charAt(0).toUpperCase();
    label.textContent = currentUser.name.split(' ')[0];
  } else {
    avatar.textContent = 'S';
    label.textContent = 'Student';
  }
}

async function syncWithDatabase() {
  if (!currentUser || !currentUser.email) return;

  const completedList = Object.keys(progress).filter(k => progress[k]);
  const overallPct = Math.round((completedList.length / CHAPTERS.length) * 100);

  // 1. Sync to local database storage (all students)
  const localDb = JSON.parse(localStorage.getItem('droneAcademy_allStudents') || '[]');
  const idx = localDb.findIndex(s => s.email.toLowerCase() === currentUser.email.toLowerCase());
  const record = {
    id: idx >= 0 ? localDb[idx].id : Date.now(),
    name: currentUser.name,
    email: currentUser.email,
    created_at: idx >= 0 ? localDb[idx].created_at : new Date().toISOString(),
    last_active: new Date().toISOString(),
    overall_progress: overallPct,
    completed_chapters: completedList,
    qna_scores: userQnaScores
  };

  if (idx >= 0) localDb[idx] = record;
  else localDb.unshift(record);

  localStorage.setItem('droneAcademy_allStudents', JSON.stringify(localDb));

  // 2. Sync to Python SQLite server API if accessible
  try {
    await fetch('/api/progress', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        email: currentUser.email,
        completed_chapters: completedList,
        qna_scores: userQnaScores,
        overall_progress: overallPct
      })
    });
  } catch (e) {
    // Server offline, silent fallback
  }
}

// Persistent State
const STORAGE_KEY = 'clubDroneAcademy_progress';
let progress = JSON.parse(localStorage.getItem(STORAGE_KEY) || '{}');
let activeChapterId = null;

// ==========================================
// CHAPTER 1 CONTENT: FPV PILOTING
// ==========================================
function getCh1Content() {
  return `
<div class="ch-section">
  <h2>What is FPV Piloting?</h2>
  <p><strong>First Person View (FPV)</strong> piloting places you directly in the virtual cockpit of a high-performance aircraft. Wearing ultra-low-latency video goggles, you see what the drone sees in real-time, operating in true 6-Degrees-of-Freedom (6-DoF) space at speeds exceeding 160 km/h (100 mph).</p>
  <p>Unlike commercial DJI camera drones, which rely on GPS positioning, sonar, optical flow, and automatic altitude hold to fly autonomously, an FPV freestyle or racing drone is <strong>100% manually controlled</strong>. When you release the radio sticks, the drone does not stop or hover—it continues moving in whatever orientation and trajectory momentum dictates.</p>
</div>

<div class="ch-section">
  <h2>Transmitter Stick Anatomy (Mode 2)</h2>
  <p>Over 95% of international FPV pilots use <strong>Mode 2</strong> radio configuration. Understanding what each stick axis commands is the foundation of muscle memory:</p>

  <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(260px, 1fr));gap:1rem;margin:1.25rem 0">
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:14px;padding:1.25rem">
      <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem">
        <span style="font-size:22px">🕹️</span>
        <h3 style="margin:0;font-size:16px;color:var(--accent-blue)">LEFT STICK (Throttle & Yaw)</h3>
      </div>
      <ul style="padding-left:1.2rem;font-size:14px;color:var(--text-secondary);margin-bottom:0">
        <li><strong>Vertical (Throttle):</strong> Controls total motor RPM. Does NOT self-center! Down = zero throttle; Up = 100% full motor thrust.</li>
        <li><strong>Horizontal (Yaw):</strong> Rotates the drone along its vertical Z-axis (turning like a compass needle) via counter-rotating motor torque.</li>
      </ul>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:14px;padding:1.25rem">
      <div style="display:flex;align-items:center;gap:0.5rem;margin-bottom:0.75rem">
        <span style="font-size:22px">🕹️</span>
        <h3 style="margin:0;font-size:16px;color:var(--accent-emerald)">RIGHT STICK (Pitch & Roll)</h3>
      </div>
      <ul style="padding-left:1.2rem;font-size:14px;color:var(--text-secondary);margin-bottom:0">
        <li><strong>Vertical (Pitch):</strong> Tilts the nose of the drone down (forward acceleration) or up (backward braking / reverse). Spring-loaded self-centering.</li>
        <li><strong>Horizontal (Roll):</strong> Tilts the quad laterally to bank left or right for turning and acrobatic barrel rolls. Spring-loaded self-centering.</li>
      </ul>
    </div>
  </div>

  <!-- Interactive Stick Visualizer -->
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🎮 Interactive Mode 2 Stick Visualizer</span>
      <span style="font-size:12px;color:var(--text-muted)">Drag or Click Gimbal to Test</span>
    </div>
    <p style="font-size:14px;color:var(--text-secondary);margin-bottom:1.25rem">
      Drag inside either gimbal to simulate stick inputs and observe how the drone interprets your commands in real time:
    </p>

    <div style="display:flex;gap:2rem;justify-content:center;align-items:center;flex-wrap:wrap;margin-bottom:1.5rem">
      <!-- Left Stick -->
      <div style="text-align:center">
        <div style="font-size:13px;font-weight:700;color:var(--accent-blue);margin-bottom:0.5rem">LEFT GIMBAL (Throttle / Yaw)</div>
        <div class="stick-gimbal" id="leftGimbal" onpointerdown="startStickDrag(event, 'left')">
          <div class="stick-pointer" id="leftPointer" style="top:50%;left:50%"></div>
        </div>
        <div style="font-size:12px;color:var(--text-muted);margin-top:0.4rem" id="leftGimbalVal">Throttle: 50% | Yaw: 0°/s</div>
      </div>

      <!-- Right Stick -->
      <div style="text-align:center">
        <div style="font-size:13px;font-weight:700;color:var(--accent-emerald);margin-bottom:0.5rem">RIGHT GIMBAL (Pitch / Roll)</div>
        <div class="stick-gimbal" id="rightGimbal" onpointerdown="startStickDrag(event, 'right')">
          <div class="stick-pointer" id="rightPointer" style="top:50%;left:50%"></div>
        </div>
        <div style="font-size:12px;color:var(--text-muted);margin-top:0.4rem" id="rightGimbalVal">Pitch: 0° | Roll: 0°</div>
      </div>
    </div>

    <div class="calc-metric-box" style="text-align:left;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem">
      <div>
        <span class="calc-metric-lbl">SIMULATED DRONE REACTION</span>
        <div style="font-size:16px;font-weight:700;color:#F8FAFC" id="stickReactionText">Level Hover State (50% Throttle)</div>
      </div>
      <button class="btn-secondary" style="padding:0.4rem 1rem;font-size:13px" onclick="resetSticks()">Center Sticks</button>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Flight Stabilization Modes: Angle vs Acro</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/fiUSJgQOkOA" 
              title="Should I Learn Acro or Angle First As A New FPV Pilot?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Should I Learn Acro or Angle First As A New FPV Pilot?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=fiUSJgQOkOA" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Betaflight supports three fundamental flight stabilization algorithms:</p>
  <table class="data-table">
    <thead>
      <tr>
        <th>Mode</th>
        <th>Sensors Used</th>
        <th>Stick Behavior</th>
        <th>Use Case</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Angle Mode</strong></td>
        <td>Gyroscope + Accelerometer</td>
        <td>Self-levels immediately when sticks are released. Maximum tilt angle is capped (typically 45°–55°). You cannot perform flips or rolls.</td>
        <td>Beginners on their first 2–3 battery packs; emergency panic recovery switch.</td>
      </tr>
      <tr>
        <td><strong>Horizon Mode</strong></td>
        <td>Gyroscope + Accelerometer</td>
        <td>Self-levels at low stick deflections, but permits continuous 360° flips when sticks are pushed to the outer stops.</td>
        <td>Transition training; rarely used by experienced pilots due to unpredictable midpoint behavior.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-blue)">Acro Mode (Rate Mode) ⭐</strong></td>
        <td>Gyroscope Only</td>
        <td><strong>Pure rotational rate control.</strong> Stick deflection dictates rotational velocity (degrees per second). Releasing the stick holds the current angle indefinitely.</td>
        <td><strong>The universal standard for 100% of freestyle and competitive drone racing.</strong></td>
      </tr>
    </tbody>
  </table>

  <div class="tip-box">
    <div class="box-label" style="color:var(--accent-blue)">💡 The Golden Acro Rule</div>
    <p style="margin:0;font-size:14px;color:var(--text-secondary)">
      Do not spend weeks flying in Angle mode. Acro mode requires training your brain to make continuous micro-corrections. Fly in a simulator in <strong>Acro mode from day one</strong>. Once you build Acro muscle memory, flying becomes as natural as riding a bicycle.
    </p>
  </div>
</div>

<div class="ch-section">
  <h2>The Physics of Camera Tilt Angle</h2>
  <p>Because a quadcopter generates vertical thrust perpendicular to its frame, <strong>to move forward it must tilt its nose down</strong>. If your FPV camera were mounted flat (0° tilt), when flying forward you would only see the grass!</p>
  <p>By angling the camera upward relative to the top plate, you maintain a level view of the horizon while the quadcopter is pitched forward at high speed:</p>
  <div class="formula-card">Forward Thrust Vector = Total Thrust × sin(Pitch Angle)</div>
  <ul>
    <li><strong>15° – 25° (Beginner / Tight Proximity):</strong> Low forward drift speed, easy to hover and navigate tight gaps slowly.</li>
    <li><strong>30° – 40° (Freestyle Sweet Spot):</strong> Balances explosive high-speed lines with smooth inverted float maneuvers.</li>
    <li><strong>50° – 65°+ (Competitive Racing):</strong> Forces extreme forward pitch for sustained 160+ km/h straightaway speeds. (Hovering requires looking straight up into the sky!)</li>
  </ul>
</div>

<div class="ch-section">
  <h2>FPV Racing Quads vs DJI Camera Drones</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🔄 Side-by-Side System Comparison</span>
      <span style="font-size:12px;color:var(--text-muted)">Click Tab to Toggle</span>
    </div>
    <div class="seg-tabs">
      <button class="seg-tab active" onclick="setCompTab('fpv', this)">FPV Racing Quadcopter</button>
      <button class="seg-tab" onclick="setCompTab('dji', this)">DJI Camera Drone (Mavic/Mini)</button>
    </div>
    <div id="compDisplay">
      <table class="data-table" style="margin:0">
        <tbody>
          <tr><td><strong>Top Airspeed</strong></td><td style="color:var(--accent-emerald);font-weight:700">140 – 210 km/h (85 – 130 mph)</td></tr>
          <tr><td><strong>Thrust-to-Weight Ratio</strong></td><td style="color:var(--accent-emerald);font-weight:700">5:1 (Freestyle) to 12:1+ (Racing)</td></tr>
          <tr><td><strong>Flight Stabilization</strong></td><td>Pure manual gyroscopic rate control (Acro)</td></tr>
          <tr><td><strong>Video Latency</strong></td><td style="color:var(--accent-emerald);font-weight:700">10ms – 28ms (Zero/Near-Zero latency)</td></tr>
          <tr><td><strong>Crash Resilience</strong></td><td style="color:var(--accent-emerald);font-weight:700">Carbon fiber frame survives concrete impacts at 100 km/h</td></tr>
          <tr><td><strong>Repairability</strong></td><td style="color:var(--accent-emerald);font-weight:700">100% modular DIY; every component replaceable with a soldering iron</td></tr>
          <tr><td><strong>Flight Duration</strong></td><td>3.5 – 6.5 minutes per battery pack</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>The Simulator Mastery Roadmap</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/SpuXqNakP2A" 
              title="Learn to Fly an FPV Drone TODAY (Beginner Simulator Guide)" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Learn to Fly an FPV Drone TODAY (Beginner Simulator Guide)</div>
      </div>
      <a href="https://www.youtube.com/watch?v=SpuXqNakP2A" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The smartest and cheapest way to enter FPV is to purchase your radio transmitter first (e.g., RadioMaster Pocket or Boxer) and plug it directly into your PC via USB as a joystick controller. Fly in a realistic simulator before spending a single rupee on drone hardware:</p>
  <ul>
    <li><strong>Hours 0 – 3:</strong> Throttle management. Practice hovering smoothly in Acro mode without bouncing off the ground or shooting into the sky.</li>
    <li><strong>Hours 3 – 8:</strong> Coordinated turns. Combining Roll and Yaw together with minor throttle adjustments to carve clean smooth corners.</li>
    <li><strong>Hours 8 – 15:</strong> Gate proximity and air braking (pitching nose up to kill forward momentum).</li>
    <li><strong>Hours 15+:</strong> Inverted yaw spins, split-S, and power loops.</li>
  </ul>
</div>
`;
}

// ==========================================
// CHAPTER 2 CONTENT: TYPES OF DRONES
// ==========================================
function getCh2Content() {
  return `
<div class="ch-section">
  <h2>FPV Drone Size Classes</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/SC556vEMoYs" 
              title="Sub-250g or 5 Inch FPV Drone Kit? Which To Get?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Sub-250g or 5 Inch FPV Drone Kit? Which To Get?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=SC556vEMoYs" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Multirotor drones are classified by the maximum diameter propeller their arms can physically swing without collision:</p>

  <table class="data-table">
    <thead>
      <tr><th>Class</th><th>Prop Size</th><th>Battery</th><th>All-Up Weight</th><th>Discipline & Characteristics</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Tiny Whoop</strong></td>
        <td>31mm – 40mm</td>
        <td>1S (300–450mAh)</td>
        <td>24g – 35g</td>
        <td>Indoor winter practice. Duct-guarded props bounce harmlessly off walls, pets, and humans.</td>
      </tr>
      <tr>
        <td><strong>Micro / Toothpick</strong></td>
        <td>2.5" – 3.5"</td>
        <td>2S – 4S</td>
        <td>65g – 180g</td>
        <td>Neighborhood park flying. Low acoustic footprint; quiet and non-threatening.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-blue)">5-Inch Standard ⭐</strong></td>
        <td>5.0" – 5.2"</td>
        <td>6S (1100–1400mAh)</td>
        <td>550g – 700g</td>
        <td><strong>The Universal Benchmark.</strong> 90% of freestyle competitions and MultiGP professional races use this class. Ideal balance of inertia, power, and durability.</td>
      </tr>
      <tr>
        <td><strong>7-Inch Long Range</strong></td>
        <td>7.0" – 7.5"</td>
        <td>6S Li-Ion / LiPo</td>
        <td>850g – 1400g</td>
        <td>Mountain surfing and exploration. Aerodynamic bi-blade props deliver 20–30+ minute flight times with GPS return-to-home.</td>
      </tr>
      <tr>
        <td><strong>Cinewhoop</strong></td>
        <td>3.0" – 3.5" ducted</td>
        <td>4S – 6S</td>
        <td>350g – 550g</td>
        <td>Slow, smooth cinematic fly-throughs inside factories, real estate, and around moving actors.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Airframe Geometry & Dynamics</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/rzpizzr3SH0" 
              title="What Downsides Do Deadcat Frames Actually Have? Frame Geometry" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">What Downsides Do Deadcat Frames Actually Have? Frame Geometry</div>
      </div>
      <a href="https://www.youtube.com/watch?v=rzpizzr3SH0" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The spatial geometry of the frame arms determines moment of inertia across the roll and pitch axes and dictates whether propellers appear in your HD camera video:</p>

  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">📐 Interactive Airframe Geometry Explorer</span>
      <span style="font-size:12px;color:var(--text-muted)">Select Geometry</span>
    </div>
    <div class="seg-tabs">
      <button class="seg-tab active" onclick="setGeoTab('truex', this)">True-X</button>
      <button class="seg-tab" onclick="setGeoTab('stretchx', this)">Stretch-X</button>
      <button class="seg-tab" onclick="setGeoTab('deadcat', this)">Deadcat (DC)</button>
      <button class="seg-tab" onclick="setGeoTab('ducted', this)">Ducted Cinewhoop</button>
    </div>
    <div id="geoDisplay" style="display:flex;gap:1.5rem;align-items:center;flex-wrap:wrap">
      <!-- Dynamic SVG Canvas -->
      <div style="background:#060A12;border:1px solid var(--border);border-radius:14px;padding:1rem;flex:1;min-width:240px;display:flex;justify-content:center">
        <svg id="geoSvg" viewBox="0 0 240 240" width="220" height="220"></svg>
      </div>
      <div style="flex:1.2;min-width:250px" id="geoDescription"></div>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Carbon Fiber Material Science</h2>
  <p>Modern FPV frames are cut from quasi-isotropic 3K twill high-tensile <strong>Toray T700 carbon fiber</strong>. Understanding carbon fiber properties is essential for electrical safety and flight tuning:</p>
  <ul>
    <li><strong>Electrical Conductivity Hazard:</strong> Carbon fiber is an electrical conductor ($\rho \approx 1.5 \times 10^{-5} \ \Omega\cdot\text{m}$). If an uninsulated battery lead, motor wire solder joint, or FC pin contacts the carbon plate, it creates an immediate chassis short-circuit that can vaporize copper traces and ignite LiPos!</li>
    <li><strong>Arm Thickness vs Weight:</strong>
      <ul>
        <li><strong>4.0mm:</strong> Weight-optimized racing frames (~60g–85g). Susceptible to arm flex under heavy prop loads.</li>
        <li><strong>5.0mm – 6.0mm:</strong> Standard freestyle frames (~110g–145g). High rigidity prevents low-frequency mechanical arm flutter from confusing gyro filters.</li>
      </ul>
    </li>
    <li><strong>Chamfered Edges:</strong> Quality frames feature CNC-chamfered plate edges. Sharp 90° raw carbon edges will slice through silicone battery wires and nylon battery straps in a high-speed crash.</li>
  </ul>

  <div class="danger-box">
    <div class="box-label" style="color:var(--accent-rose)">⚡ Short Circuit Isolation Rule</div>
    <p style="margin:0;font-size:14px;color:var(--text-secondary)">
      Never allow bare PCB solder pads or exposed wire conductors to contact raw carbon fiber. Always place silicone insulation, Mylar tape, or non-conductive O-rings between the electronics and the frame chassis.
    </p>
  </div>
</div>

<div class="ch-section">
  <h2>Benchmark 5-Inch Frames</h2>
  <table class="data-table">
    <thead>
      <tr><th>Frame</th><th>Weight</th><th>Arm Thickness</th><th>Mounting Stacks</th><th>Distinguishing Advantage</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>TBS Source One V5</strong></td>
        <td>115g</td>
        <td>5.0mm</td>
        <td>30.5×30.5 & 20×20</td>
        <td>Open-source community standard. Replacement arms cost under ₹350; virtually indestructible.</td>
      </tr>
      <tr>
        <td><strong>AOS 5 V5 (Chris Rosser)</strong></td>
        <td>110g</td>
        <td>5.0mm</td>
        <td>30.5×30.5 & 20×20</td>
        <td>Finite Element Analysis (FEA) optimized. Pushes resonant vibration frequencies above 320Hz for razor-sharp PID response.</td>
      </tr>
      <tr>
        <td><strong>ImpulseRC Apex EVO</strong></td>
        <td>138g</td>
        <td>5.5mm</td>
        <td>30.5×30.5 & 20×20</td>
        <td>Premium freestyle baseline with interlocking key-stone arm lock and vibration-isolated camera cage.</td>
      </tr>
    </tbody>
  </table>
</div>
`;
}

// ==========================================
// CHAPTER 3 CONTENT: PHYSICS & CALCULATIONS
// ==========================================
function getCh3Content() {
  return `
<div class="ch-section">
  <h2>Newton's Laws Applied to Multirotors</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/SpuXqNakP2A" 
              title="How Quadcopters Fly & Momentum Dynamics" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How Quadcopters Fly & Momentum Dynamics</div>
      </div>
      <a href="https://www.youtube.com/watch?v=SpuXqNakP2A" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Every maneuver performed by an FPV drone is governed by classical Newtonian mechanics and momentum conservation:</p>
  
  <div style="display:grid;gap:1rem;margin:1.25rem 0">
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:12px;padding:1.25rem">
      <h3 style="margin:0 0 0.5rem;color:var(--accent-blue)">1. First Law: Law of Inertia (Acro Mode Physics)</h3>
      <p style="margin:0;font-size:14px;color:var(--text-secondary)">
        An object maintains its state of uniform motion unless acted upon by a net external force. In Acro mode, when you pitch the drone 45° forward and center the right stick, the drone preserves that 45° orientation and continues hurtling forward. The flight controller only applies motor torque when you command a rate change!
      </p>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:12px;padding:1.25rem">
      <h3 style="margin:0 0 0.5rem;color:var(--accent-emerald)">2. Second Law: Force, Mass & Vertical Acceleration</h3>
      <div class="formula-card">F_net = m · a &nbsp;⟹&nbsp; a_z = (T_total - m · g) / m</div>
      <p style="margin:0;font-size:14px;color:var(--text-secondary)">
        To accelerate vertically upward at $1.0\text{G}$ ($9.81\text{ m/s}^2$), your total motor thrust must equal exactly twice the quadcopter's gravitational weight ($2.0\text{G}$ total thrust). A racing drone with a 10:1 Thrust-to-Weight ratio produces an instantaneous vertical acceleration of $9\text{Gs}$ ($88.3\text{ m/s}^2$)!
      </p>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:12px;padding:1.25rem">
      <h3 style="margin:0 0 0.5rem;color:var(--accent-amber)">3. Third Law: Counter-Rotating Props & Yaw Generation</h3>
      <p style="margin:0;font-size:14px;color:var(--text-secondary)">
        Every action has an equal and opposite reaction. As motor 1 spins its propeller clockwise (CW), aerodynamic drag exerts an equal counter-clockwise (CCW) reactive torque on the drone body. 
        <br><br>
        To prevent the drone from spinning uncontrollably in circles, <strong>two motors spin Clockwise (CW) and two spin Counter-Clockwise (CCW)</strong>. At level hover, reactive torques cancel out perfectly to zero. 
        <br><br>
        <strong>How Yaw Works:</strong> When you yaw left, the flight controller speeds up the two CW motors and slows down the two CCW motors. Total lift remains unchanged, but the net unbalanced torque rotates the drone around its Z-axis without tilting!
      </p>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Thrust-to-Weight Ratio (TWR) Formula</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/6t4gS-HfqT0" 
              title="Thrust to Weight Ratio for FPV Drones - How Much Power Do You Need?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Thrust to Weight Ratio for FPV Drones - How Much Power Do You Need?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=6t4gS-HfqT0" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <div class="formula-card">TWR = Total Maximum Thrust (g) / All-Up Weight (g)</div>
  <p>Where All-Up Weight (AUW) includes the frame, four motors, ESC, FC, VTX, antennas, FPV camera, battery, and optional HD recording camera (GoPro):</p>
  <ul>
    <li><strong>TWR &lt; 2:1:</strong> Sluggish, barely flyable. Cannot arrest descent from freefall; winds will blow it away.</li>
    <li><strong>TWR 4:1 to 6:1 (Freestyle Benchmark):</strong> Smooth, predictable throttle resolution. Crisp float at zero-throttle with explosive punchouts.</li>
    <li><strong>TWR 8:1 to 14:1+ (Competition Racing):</strong> Extreme acceleration. 0 to 100 km/h in under 1.2 seconds. Hover occurs at 10%–15% stick position.</li>
  </ul>

  <div class="formula-card">Hover Throttle % ≈ (1 / TWR) × 100%</div>
</div>

<div class="ch-section">
  <h2>Master Flight Physics & TWR Calculator</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">📐 Multirotor Dynamics & Acceleration Calculator</span>
      <span style="font-size:12px;color:var(--text-muted)">Live Newtonian Solver</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:1.25rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          All-Up Weight (AUW): <strong id="twrAuwVal" style="color:var(--accent-blue)">650</strong> grams
        </label>
        <input type="range" min="200" max="1400" value="650" step="10" id="twrAuwInput" oninput="updatePhysicsCalc()">
      </div>
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Peak Thrust per Motor: <strong id="twrThrustVal" style="color:var(--accent-blue)">1650</strong> grams
        </label>
        <input type="range" min="400" max="2500" value="1650" step="25" id="twrThrustInput" oninput="updatePhysicsCalc()">
      </div>
    </div>

    <!-- Output Metrics Grid -->
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1.25rem">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">TOTAL THRUST</span>
        <div class="calc-metric-val" id="physTotalThrust">6,600g</div>
        <span style="font-size:11px;color:var(--text-muted)">4 × Motor Thrust</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">THRUST-TO-WEIGHT</span>
        <div class="calc-metric-val" id="physTwr" style="color:var(--accent-emerald)">10.15 : 1</div>
        <span style="font-size:11px;color:var(--text-muted)" id="physTwrClass">Competition Class</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">HOVER THROTTLE</span>
        <div class="calc-metric-val" id="physHoverThrottle" style="color:#A78BFA">9.8%</div>
        <span style="font-size:11px;color:var(--text-muted)">Stick Position</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">MAX VERTICAL G-FORCE</span>
        <div class="calc-metric-val" id="physGForce" style="color:var(--accent-amber)">9.15 G</div>
        <span style="font-size:11px;color:var(--text-muted)">89.8 m/s² accel</span>
      </div>
    </div>

    <div style="background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:10px;padding:0.85rem 1rem;font-size:13px;color:var(--text-secondary)" id="physVerdictText">
      ✓ <strong>Elite Competition Racing Setup:</strong> Enormous power-to-weight ratio. Instantaneous punch-out acceleration with negligible throttle lag.
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Electrical Power & Joule Heating Laws</h2>
  <div class="formula-card">P = V × I &nbsp;&nbsp;|&nbsp;&nbsp; P_loss = I² × R_internal</div>
  <p>Electrical power transferred to the mechanical motors equals Voltage multiplied by Current. When high current passes through the battery chemistry, ESC MOSFET switches, and copper wiring, resistive loss ($I^2 R$) generates pure wasted heat.</p>
  <p>By switching from a 4S system (14.8V) to a 6S system (22.2V) to deliver 500 Watts of power:</p>
  <ul>
    <li>Current drops from $33.8\text{ Amps}$ to $22.5\text{ Amps}$ (a 33.4% reduction).</li>
    <li>Joule heat dissipation ($I^2 R$) drops by <strong>55.6%</strong>! This explains why 6S components run dramatically cooler and suffer significantly less battery voltage sag.</li>
  </ul>
</div>
`;
}

// ==========================================
// CHAPTER 4 CONTENT: MASTER SPEC SELECTION
// ==========================================
function getCh4Content() {
  return `
<div class="ch-section">
  <h2>The Component Harmony Principle</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/SC556vEMoYs" 
              title="How to Choose Parts for a 5-Inch FPV Drone Kit" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How to Choose Parts for a 5-Inch FPV Drone Kit</div>
      </div>
      <a href="https://www.youtube.com/watch?v=SC556vEMoYs" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The single greatest mistake made by first-time drone builders is purchasing parts in isolation based on random sales or YouTube clips. An FPV quadcopter is an interconnected electromechanical system:</p>
  <div class="spec-box">
    <div class="box-label" style="color:var(--accent-indigo)">Master Engineering Sequence</div>
    <div style="font-size:14px;color:var(--text-secondary);line-height:1.8">
      <strong>Mission Profile</strong> ⟹ Determines <strong>Frame Geometry & Propeller Diameter</strong><br>
      <strong>Propeller Load</strong> ⟹ Determines <strong>Motor Stator Diameter & Height</strong><br>
      <strong>Battery Voltage (4S vs 6S)</strong> ⟹ Determines <strong>Motor KV Rating</strong><br>
      <strong>Peak Motor Current</strong> ⟹ Determines <strong>ESC Continuous Amperage (+25% Headroom)</strong><br>
      <strong>Total Current Draw</strong> ⟹ Determines <strong>Battery Capacity (mAh) & C-Rating</strong><br>
      <strong>Peripherals (VTX, GPS, RX)</strong> ⟹ Determines <strong>Flight Controller MCU & UART Count</strong>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Why Each Specification is Chosen</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/n8epgP7jlrk" 
              title="4S vs 6S LiPo Batteries - Which Do I Buy as a New Pilot?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">4S vs 6S LiPo Batteries - Which Do I Buy as a New Pilot?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=n8epgP7jlrk" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <table class="data-table">
    <thead>
      <tr><th>Component</th><th>Recommended 5" 6S Spec</th><th>Why This Exact Spec is Chosen</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Frame Size</strong></td>
        <td>210mm – 230mm (5" Props)</td>
        <td>Optimal balance of agility, inertia, and aerodynamic authority. Parts are globally available and standardized.</td>
      </tr>
      <tr>
        <td><strong>Arm Thickness</strong></td>
        <td>5.0mm – 6.0mm Carbon</td>
        <td>Resists flex under high G-loads. Keeps mechanical vibration resonance frequencies high (&gt;300Hz) for clean gyro filtering.</td>
      </tr>
      <tr>
        <td><strong>Motor Stator</strong></td>
        <td>2207 or 2306</td>
        <td>Large stator volume (~2,660 mm³) generates sufficient magnetic torque to spin steep 5.1" props without bogging down.</td>
      </tr>
      <tr>
        <td><strong>Motor KV</strong></td>
        <td>1850 – 1960 KV</td>
        <td>Multiplied by 22.2V nominal 6S voltage yields ~42,000 RPM, the sweet spot for 5-inch freestyle propeller aerodynamics.</td>
      </tr>
      <tr>
        <td><strong>Propeller</strong></td>
        <td>5.1" × 4.3" Tri-Blade</td>
        <td>Tri-blade design provides corner grip and active braking authority. 4.3" pitch gives linear throttle feel without high amp draw.</td>
      </tr>
      <tr>
        <td><strong>ESC Rating</strong></td>
        <td>50A – 60A Continuous</td>
        <td>Modern 2207 motors spike to 40A–45A during full-throttle punchouts. A 55A ESC provides mandatory 25%+ safety thermal headroom.</td>
      </tr>
      <tr>
        <td><strong>ESC Firmware</strong></td>
        <td>AM32 or Bluejay (32-bit)</td>
        <td>Enables Bidirectional DShot to stream real-time motor RPM to the flight controller for dynamic notch filtering.</td>
      </tr>
      <tr>
        <td><strong>Battery</strong></td>
        <td>6S 1100–1300 mAh (100C+)</td>
        <td>Optimal energy-to-weight ratio (~210g). Anything over 1500mAh adds dead weight that degrades acrobatics.</td>
      </tr>
      <tr>
        <td><strong>Flight Controller</strong></td>
        <td>STM32F722 or H743</td>
        <td>Runs 8kHz PID loops with bidirectional DShot with plenty of flash memory and 5+ hardware UARTs.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Interactive 5-Inch Spec Builder & Compatibility Validator</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🛠️ Complete 5" Drone Spec Configurator</span>
      <span style="font-size:12px;color:var(--text-muted)">Live Engineering Validator</span>
    </div>

    <!-- Dropdown Selector Form -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(230px, 1fr));gap:1rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">FRAME TYPE</label>
        <select class="spec-select" id="specFrame" onchange="updateSpecBuilder()">
          <option value="freestyle_5">5" Freestyle True-X (5mm arms, 125g)</option>
          <option value="race_5">5" Ultralight Racing (4mm arms, 70g)</option>
          <option value="deadcat_5">5" Deadcat Cinematic (5mm arms, 140g)</option>
        </select>
      </div>

      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">MOTORS (STATOR & KV)</label>
        <select class="spec-select" id="specMotor" onchange="updateSpecBuilder()">
          <option value="2207_1950">2207 1950KV (6S Freestyle Standard)</option>
          <option value="2207_2100">2207 2100KV (6S Extreme Racing)</option>
          <option value="2207_2450">2207 2450KV (4S Classic Build)</option>
          <option value="2306_1850">2306 1850KV (6S High Torque / Smooth)</option>
        </select>
      </div>

      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">PROPELLER PITCH</label>
        <select class="spec-select" id="specProp" onchange="updateSpecBuilder()">
          <option value="5143">5.1" × 4.3" Tri-Blade (Balanced Freestyle)</option>
          <option value="5146">5.1" × 4.6" Tri-Blade (Aggressive Racing)</option>
          <option value="5030">5.0" × 3.0" Bi-Blade (Smooth Efficiency)</option>
        </select>
      </div>

      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">ESC RATING</label>
        <select class="spec-select" id="specEsc" onchange="updateSpecBuilder()">
          <option value="35">35A 4-in-1 (Ultralight / Risky)</option>
          <option value="45">45A 4-in-1 (Standard Budget)</option>
          <option value="55" selected>55A 4-in-1 (Recommended Gold Standard)</option>
          <option value="65">65A 4-in-1 (Heavy Duty Racing)</option>
        </select>
      </div>

      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">BATTERY SYSTEM</label>
        <select class="spec-select" id="specBatt" onchange="updateSpecBuilder()">
          <option value="6s_1100">6S 1100mAh 120C (190g - Racing Agility)</option>
          <option value="6s_1300" selected>6S 1300mAh 100C (215g - Freestyle Sweet Spot)</option>
          <option value="6s_1800">6S 1800mAh 80C (290g - Long Cruising)</option>
          <option value="4s_1500">4S 1500mAh 100C (180g - Legacy 4S)</option>
        </select>
      </div>

      <div>
        <label style="font-size:12px;font-weight:700;color:var(--text-muted);display:block;margin-bottom:0.35rem">VIDEO SYSTEM</label>
        <select class="spec-select" id="specVtx" onchange="updateSpecBuilder()">
          <option value="analog">Analog 5.8GHz (Rush Tank + Ratel, 25g)</option>
          <option value="dji">DJI O3 Air Unit HD (42g)</option>
          <option value="walksnail">Walksnail Avatar HD Pro (35g)</option>
          <option value="hdzero">HDZero Freestyle V2 (32g)</option>
        </select>
      </div>
    </div>

    <!-- Calculated Spec Summary Box -->
    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1.25rem">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">ESTIMATED ALL-UP WEIGHT</span>
        <div class="calc-metric-val" id="specAuw">625g</div>
        <span style="font-size:11px;color:var(--text-muted)">Ready to Fly</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">PEAK CURRENT / MOTOR</span>
        <div class="calc-metric-val" id="specPeakAmp">41.5A</div>
        <span style="font-size:11px;color:var(--text-muted)">Full Punchout</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">ESC SAFETY MARGIN</span>
        <div class="calc-metric-val" id="specEscMargin" style="color:var(--accent-emerald)">+32.5%</div>
        <span style="font-size:11px;color:var(--text-muted)">Thermal Headroom</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">ESTIMATED TWR</span>
        <div class="calc-metric-val" id="specTwr" style="color:var(--accent-blue)">10.8 : 1</div>
        <span style="font-size:11px;color:var(--text-muted)">Thrust to Weight</span>
      </div>
    </div>

    <!-- Architectural Rational Breakdown -->
    <div id="specRationaleBox" style="background:#080E1A;border:1px solid var(--border);border-radius:12px;padding:1.15rem;font-size:13px;line-height:1.7"></div>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 5 CONTENT: MOTORS
// ==========================================
function getCh5Content() {
  return `
<div class="ch-section">
  <h2>Brushless DC Outrunner Physics</h2>
  <p>FPV drones use three-phase <strong>Brushless DC (BLDC) outrunner motors</strong>. In an outrunner motor, the copper wire stator coils are stationary at the center, while the outer bell housing containing permanent neodymium magnets spins around it:</p>
  <ul>
    <li><strong>12N14P Standard Architecture:</strong> 12 stator electromagnets and 14 permanent curved rotor magnets. This configuration balances smooth torque generation with minimal rotational cogging.</li>
    <li><strong>N52H & N52SH Neodymium Magnets:</strong> The "N52" denotes maximum magnetic energy product (MGOe). The "H" and "SH" suffixes indicate high Curie temperature ratings (150°C–180°C), preventing the magnets from losing strength when running hot during aggressive flights.</li>
  </ul>
</div>

<div class="ch-section">
  <h2>Stator Size Geometry (XXYY Naming)</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/Wxpa-1FrbYM" 
              title="2306 vs 2207 Motor Size Comparison for FPV Mini Quad" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">2306 vs 2207 Motor Size Comparison for FPV Mini Quad</div>
      </div>
      <a href="https://www.youtube.com/watch?v=Wxpa-1FrbYM" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Motor sizing is expressed as a 4-digit number: <strong>2207</strong> = 22mm Stator Diameter × 7mm Stator Height:</p>
  <div class="formula-card">Stator Volume = π × (Diameter / 2)² × Height</div>
  <table class="data-table">
    <thead>
      <tr><th>Stator</th><th>Diameter</th><th>Height</th><th>Volume</th><th>Electromechanical Characteristics</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>2207 ⭐</strong></td>
        <td>22 mm</td>
        <td>7 mm</td>
        <td>2,661 mm³</td>
        <td>Taller magnetic field contact area. Higher top-end power and sustained high-RPM torque for steep props. Modern freestyle standard.</td>
      </tr>
      <tr>
        <td><strong>2306</strong></td>
        <td>23 mm</td>
        <td>6 mm</td>
        <td>2,493 mm³</td>
        <td>Wider magnetic lever arm. Generates instantaneous low-RPM torque for snappier direction reversals and runs slightly cooler.</td>
      </tr>
      <tr>
        <td><strong>2208</strong></td>
        <td>22 mm</td>
        <td>8 mm</td>
        <td>3,041 mm³</td>
        <td>Massive power for heavy racing props, but draws significant current and adds ~36g per motor.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Motor KV & Stator Explorer</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/E6nsJpuaTQc" 
              title="How Do You Choose Motor KV for a Build?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How Do You Choose Motor KV for a Build?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=E6nsJpuaTQc" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">⚡ Interactive Motor KV & RPM Solver</span>
      <span style="font-size:12px;color:var(--text-muted)">RPM & Torque Calculator</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:1.25rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Battery Cell Count: <strong id="motorCellVal" style="color:var(--accent-blue)">6S (22.2V - 25.2V)</strong>
        </label>
        <input type="range" min="3" max="6" value="6" id="motorCellInput" oninput="updateMotorExplorer()">
      </div>
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Motor KV Rating: <strong id="motorKvVal" style="color:var(--accent-blue)">1950 KV</strong>
        </label>
        <input type="range" min="1400" max="2800" value="1950" step="25" id="motorKvInput" oninput="updateMotorExplorer()">
      </div>
    </div>

    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1.25rem">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">UNLOADED MAX RPM</span>
        <div class="calc-metric-val" id="motorMaxRpm">49,140</div>
        <span style="font-size:11px;color:var(--text-muted)">At 25.2V Full Charge</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">LOADED WORKING RPM</span>
        <div class="calc-metric-val" id="motorWorkRpm" style="color:var(--accent-emerald)">39,310</div>
        <span style="font-size:11px;color:var(--text-muted)">~80% with 5.1" Prop</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">RPM OPERATING ZONE</span>
        <div class="calc-metric-val" id="motorZoneText" style="color:var(--accent-emerald);font-size:18px;margin:0.5rem 0">✓ Optimal 5"</div>
        <span style="font-size:11px;color:var(--text-muted)">Freestyle Target: 38k–43k</span>
      </div>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>The Dangerous Motor Screw Depth Trap</h2>
  <div class="danger-box">
    <div class="box-label" style="color:var(--accent-rose)">🔥 The #1 Beginner Killer: Screws Touching Stator Windings</div>
    <p style="margin:0;font-size:14px;color:var(--text-secondary)">
      When bolting motors to the carbon fiber arms, <strong>always verify screw thread penetration depth</strong>. If a screw is even 1mm too long, it will thread into the base and puncture the enamel coating of the copper stator windings.
      <br><br>
      The moment you plug in your battery, a dead short from the battery through the carbon frame to the ESC will vaporize the motor windings and instantly blow the ESC MOSFETs!
      <br><br>
      <strong>Golden Formula:</strong> Screw Length = Arm Thickness (5mm) + Motor Base Thickness (2mm) = <strong>7mm to 8mm max screw length</strong>.
    </p>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 6 CONTENT: PROPELLERS
// ==========================================
function getCh6Content() {
  return `
<div class="ch-section">
  <h2>Propeller Aerodynamics: How Thrust is Created</h2>
  <p>A propeller blade is a rotating aerodynamic airfoil. Its curved upper camber and flatter lower camber create a pressure differential as it slices through the air ($L = \frac{1}{2}\rho v^2 S C_L$), accelerating an air mass downward according to momentum theory:</p>
  <div class="formula-card">Thrust = Mass Airflow Rate × Velocity Change &nbsp;⟹&nbsp; T = ṁ · Δv</div>
</div>

<div class="ch-section">
  <h2>Decoding Propeller Naming Formats</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/p09s3f9K6s0" 
              title="How to Choose FPV Drone Propellers: Pitch and Diameter" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How to Choose FPV Drone Propellers: Pitch and Diameter</div>
      </div>
      <a href="https://www.youtube.com/watch?v=p09s3f9K6s0" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Modern props use a 5-digit shorthand code, such as <strong>51466</strong>:</p>
  <ul>
    <li><strong>First Two Digits (51):</strong> Propeller diameter in inches (5.1 inches). Larger diameter sweeps a wider disk area, generating more thrust at lower RPM.</li>
    <li><strong>Middle Two Digits (46):</strong> Pitch in inches (4.6 inches). The theoretical linear distance the propeller would advance in one revolution through a solid medium.</li>
    <li><strong>Last Digit (6):</strong> Aerodynamic blade profile / design revision.</li>
  </ul>
</div>

<div class="ch-section">
  <h2>Pitch Dynamics & Airspeed Calculator</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🌀 Propeller Pitch Speed & Airflow Calculator</span>
      <span style="font-size:12px;color:var(--text-muted)">Aerodynamic Speed Solver</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:1.25rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Propeller Pitch: <strong id="propPitchVal" style="color:var(--accent-blue)">4.3 inches</strong>
        </label>
        <input type="range" min="3.0" max="5.0" value="4.3" step="0.1" id="propPitchInput" oninput="updatePropSpeedCalc()">
      </div>
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Motor Working RPM: <strong id="propRpmVal" style="color:var(--accent-blue)">38,000 RPM</strong>
        </label>
        <input type="range" min="20000" max="48000" value="38000" step="1000" id="propRpmInput" oninput="updatePropSpeedCalc()">
      </div>
    </div>

    <div style="display:flex;gap:1rem;flex-wrap:wrap;margin-bottom:1.25rem">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">THEORETICAL PITCH SPEED</span>
        <div class="calc-metric-val" id="propPitchSpeedMph">154.7 mph</div>
        <span style="font-size:11px;color:var(--text-muted)" id="propPitchSpeedKmh">249.0 km/h</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">ESTIMATED REAL AIRSPEED</span>
        <div class="calc-metric-val" id="propRealSpeedKmh" style="color:var(--accent-emerald)">161.8 km/h</div>
        <span style="font-size:11px;color:var(--text-muted)">~65% Real Dynamic Efficiency</span>
      </div>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>"Props In" vs "Props Out" (Reversed Rotation)</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/bZL-BBl9JnE" 
              title="Props-In (Standard) vs. Props-Out (Reversed) - Which Is Better?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Props-In (Standard) vs. Props-Out (Reversed) - Which Is Better?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=bZL-BBl9JnE" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Traditionally, quadcopters were configured with propellers rotating inwards toward the front camera ("Props In"). Modern FPV setups universally run <strong>"Props Out" (Reversed Rotation)</strong>:</p>
  <ul>
    <li><strong>Camera Lens Protection:</strong> In "Props Out", the front propellers spin outward away from the center cage, throwing dirt, moisture, and shredded grass away from your FPV camera lens.</li>
    <li><strong>Gate Clip Survival:</strong> When clipping an obstacle or race gate with a front arm, an outwardly spinning prop tends to deflect and push the drone off the gate, rather than sucking the airframe into the obstacle.</li>
  </ul>
</div>
`;
}

// ==========================================
// CHAPTER 7 CONTENT: ESC & ELECTRONICS
// ==========================================
function getCh7Content() {
  return `
<div class="ch-section">
  <h2>Electronic Speed Controller (ESC) Architecture</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/NoiqODFwU68" 
              title="How Do I Pick An ESC For My Flight Controller?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How Do I Pick An ESC For My Flight Controller?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=NoiqODFwU68" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The 4-in-1 Electronic Speed Controller is the heavy-power bridge between your DC battery pack and the three-phase AC motors. For each of the 4 motor channels, the ESC uses 6 high-power N-channel MOSFET transistors arranged into 3 half-bridges:</p>
  <div class="formula-card">Joule Conduction Losses = I² × R_DS(on)</div>
  <p>Premium ESCs utilize MOSFETs with ultra-low drain-to-source on-resistance ($R_{DS(on)} \le 0.8\text{ m}\Omega$). Lower internal resistance means cooler temperatures and reduced risk of thermal runaway.</p>
</div>

<div class="ch-section">
  <h2>ESC Firmware: AM32 & Bidirectional DShot</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/2tvWimtmgd4" 
              title="How Does Betaflight RPM Filtering Work?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How Does Betaflight RPM Filtering Work?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=2tvWimtmgd4" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <table class="data-table">
    <thead>
      <tr><th>Firmware</th><th>Architecture</th><th>Capabilities</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong style="color:var(--accent-blue)">AM32 (AlkaMotors) ⭐</strong></td>
        <td>32-bit (STM32/AT32/GD32)</td>
        <td><strong>Open-source community standard.</strong> Native Bidirectional DShot, variable PWM frequencies (24kHz–96kHz), telemetry, sinusoidal startup. Replaces BLHeli_32.</td>
      </tr>
      <tr>
        <td><strong>Bluejay</strong></td>
        <td>8-bit (BusyBee / BLHeli_S)</td>
        <td>Open-source firmware that brings Bidirectional DShot and RPM filtering to budget 8-bit ESCs.</td>
      </tr>
    </tbody>
  </table>

  <h3>Why Bidirectional DShot is Essential</h3>
  <p>With Bidirectional DShot600, on every single control packet the ESC sends back a 16-bit telemetry packet containing the exact motor electrical period (eRPM). Betaflight calculates precise motor rotational frequencies in real time and positions narrow <strong>RPM dynamic notch filters</strong> right on top of motor harmonics, eliminating vibrations without adding filter phase delay!</p>
</div>

<div class="ch-section">
  <h2>The Mandatory Low-ESR Capacitor</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/kdPfiZ37nKs" 
              title="Best Way to Mount Your Capacitor on ESC or XT60" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Best Way to Mount Your Capacitor on ESC or XT60</div>
      </div>
      <a href="https://www.youtube.com/watch?v=kdPfiZ37nKs" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <div class="danger-box">
    <div class="box-label" style="color:var(--accent-rose)">⚡ Inductive Voltage Spikes Destroy Electronics</div>
    <p style="margin:0;font-size:14px;color:var(--text-secondary)">
      When motors brake actively (Damped Light mode), the motor coils act as inductors. Collapsing magnetic fields generate massive inductive voltage spikes that shoot back into the main battery rail.
      <br><br>
      On a 6S battery (25.2V), these voltage spikes frequently exceed <strong>45V to 55V</strong>! Without an electrolytic capacitor, these spikes instantly fry the 5V/9V voltage regulators on your flight controller and video transmitter.
      <br><br>
      <strong>Requirement:</strong> Always solder a <strong>35V–50V 1000µF Low-ESR Rubycon ZLH or Panasonic FR capacitor</strong> directly across the main ESC XT60 battery solder pads with the shortest possible leads.
    </p>
  </div>
</div>

<div class="ch-section">
  <h2>ESC Safety Headroom Calculator</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🔌 ESC Safety Margin & Thermal Headroom</span>
      <span style="font-size:12px;color:var(--text-muted)">Amperage Safety Checker</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:1.25rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Motor Peak Burst Current: <strong id="escMotorVal" style="color:var(--accent-blue)">42A</strong>
        </label>
        <input type="range" min="20" max="65" value="42" id="escMotorInput" oninput="updateEscSafetyCalc()">
      </div>
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          ESC Continuous Rating: <strong id="escRatingVal" style="color:var(--accent-blue)">55A</strong>
        </label>
        <input type="range" min="30" max="75" value="55" step="5" id="escRatingInput" oninput="updateEscSafetyCalc()">
      </div>
    </div>

    <div style="display:flex;gap:1rem;flex-wrap:wrap">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">SAFETY HEADROOM</span>
        <div class="calc-metric-val" id="escMarginVal" style="color:var(--accent-emerald)">+31.0%</div>
        <span style="font-size:11px;color:var(--text-muted)">Target: &gt; 25%</span>
      </div>
      <div class="calc-metric-box" style="flex:2">
        <span class="calc-metric-lbl">STATUS & RECOMMENDATION</span>
        <div style="font-size:15px;font-weight:700;color:var(--text-primary);margin-top:0.4rem" id="escVerdict">
          ✓ Safe Margin: Adequate headroom to absorb current spikes in hot weather.
        </div>
      </div>
    </div>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 8 CONTENT: FLIGHT CONTROLLER
// ==========================================
function getCh8Content() {
  return `
<div class="ch-section">
  <h2>Compute Architecture: MCUs & Gyros</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/gryW-L_U9S8" 
              title="What Are The Benefits Of An F7 Flight Controller Over An F4?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">What Are The Benefits Of An F7 Flight Controller Over An F4?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=gryW-L_U9S8" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The Flight Controller (FC) samples its onboard 6-axis Inertial Measurement Unit (IMU) at 3.2kHz to 8kHz, calculates error terms from pilot radio setpoints, runs the PID loop, and outputs motor commands via DShot600:</p>

  <table class="data-table">
    <thead>
      <tr><th>Processor (MCU)</th><th>Clock Speed</th><th>Flash Memory</th><th>UART Serial Ports</th><th>Engineering Assessment</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>STM32F405</strong></td>
        <td>168 MHz</td>
        <td>1 MB</td>
        <td>3 – 4 Ports</td>
        <td>Budget baseline. Lacks hardware inverters on all ports; requires software hacks for legacy receivers.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-blue)">STM32F722 ⭐</strong></td>
        <td>216 MHz</td>
        <td>512 KB</td>
        <td>5 – 6 Ports</td>
        <td><strong>The Modern Sweet Spot.</strong> Universal hardware inverters on all UARTs. Handles 8kHz PID loops with bidirectional DShot.</td>
      </tr>
      <tr>
        <td><strong>STM32H743</strong></td>
        <td>480 MHz</td>
        <td>2 MB</td>
        <td>7 – 8 Ports</td>
        <td>Powerhouse MCU. Massive memory for autonomous INAV navigation routines and complex dual-gyro filtering.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Gyroscopes & Soft-Mounting Physics</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/QhW-0ddGJ7A" 
              title="How to Wire a Flight Controller and Soft Mount" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How to Wire a Flight Controller and Soft Mount</div>
      </div>
      <a href="https://www.youtube.com/watch?v=QhW-0ddGJ7A" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>The onboard gyroscope measures angular rates of change on roll, pitch, and yaw:</p>
  <ul>
    <li><strong>ICM-42688-P:</strong> The current benchmark sensor. 32kHz native internal sampling rate with an ultra-low noise floor, but sensitive to mechanical frame vibrations.</li>
    <li><strong>BMI270:</strong> Extremely vibration-tolerant Bosch sensor. Limited to 3.2kHz PID loop rates in Betaflight, but very forgiving on noisy frames.</li>
    <li><strong>Silicone Soft-Mounting Grommets:</strong> The FC PCB must <strong>NEVER be bolted rigidly to carbon fiber standoffs</strong>. Silicone anti-vibration grommets isolate the IMU from mechanical motor harmonics. Over-tightening stack nuts crushes the grommets solid, causing gyro saturation, hot motors, and mid-air twitches!</li>
  </ul>
</div>

<div class="ch-section">
  <h2>Interactive UART Bus Planner</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🧠 UART Serial Port Planner & Resource Allocator</span>
      <span style="font-size:12px;color:var(--text-muted)">Hardware Pin Validator</span>
    </div>

    <p style="font-size:14px;color:var(--text-secondary);margin-bottom:1rem">
      Check the hardware peripherals you plan to solder to the flight controller:
    </p>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(240px, 1fr));gap:0.6rem;margin-bottom:1.25rem">
      <label class="check-row done" style="margin:0;cursor:default">
        <span class="check-circle">✓</span>
        <span style="font-size:13px;font-weight:600">CRSF / ELRS Receiver (Required - UART 1)</span>
      </label>
      <label class="check-row" id="uartCheckVtx" onclick="toggleUartCheck(this)" style="margin:0">
        <span class="check-circle" id="uartDotVtx"></span>
        <span style="font-size:13px">Digital VTX / MSP DisplayPort (DJI/Walksnail)</span>
      </label>
      <label class="check-row" id="uartCheckGps" onclick="toggleUartCheck(this)" style="margin:0">
        <span class="check-circle" id="uartDotGps"></span>
        <span style="font-size:13px">GPS Rescue Module + Compass</span>
      </label>
      <label class="check-row" id="uartCheckTelem" onclick="toggleUartCheck(this)" style="margin:0">
        <span class="check-circle" id="uartDotTelem"></span>
        <span style="font-size:13px">ESC Current/RPM Telemetry Wire</span>
      </label>
      <label class="check-row" id="uartCheckAudio" onclick="toggleUartCheck(this)" style="margin:0">
        <span class="check-circle" id="uartDotAudio"></span>
        <span style="font-size:13px">Analog VTX SmartAudio / Tramp Wire</span>
      </label>
    </div>

    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:12px;padding:1rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:1rem">
      <div>
        <span style="font-size:12px;color:var(--text-muted);font-weight:600">PORTS REQUIRED</span>
        <div style="font-size:20px;font-weight:800;color:var(--accent-blue)" id="uartNeededCount">1 Hardware UART</div>
      </div>
      <div style="font-size:13px;color:var(--text-secondary)" id="uartCompatibility">
        Compatible with <strong>F405 (3 ports)</strong>, <strong>F722 (5 ports)</strong>, and <strong>H743 (7 ports)</strong>.
      </div>
    </div>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 9 CONTENT: BATTERIES & CHEMISTRY
// ==========================================
function getCh9Content() {
  return `
<div class="ch-section">
  <h2>LiPo Electrochemistry & Voltage Thresholds</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/lZKoW_ekAu0" 
              title="How to Charge and Handle LiPo Batteries Safely" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">How to Charge and Handle LiPo Batteries Safely</div>
      </div>
      <a href="https://www.youtube.com/watch?v=lZKoW_ekAu0" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Lithium Polymer (LiPo) batteries use lithium cobalt oxide cathodes and graphite anodes. Each cell has strict physical voltage boundaries:</p>

  <table class="data-table">
    <thead>
      <tr><th>Cell State</th><th>Voltage per Cell</th><th>6S Pack Voltage</th><th>Chemical Consequence</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Fully Charged</strong></td>
        <td>4.20V</td>
        <td>25.2V</td>
        <td>Maximum chemical saturation. Never charge above 4.20V (4.35V for LiHV).</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-amber)">Storage Voltage ⭐</strong></td>
        <td>3.80V – 3.85V</td>
        <td>22.8V – 23.1V</td>
        <td><strong>The chemical equilibrium state.</strong> Store batteries here if unused for &gt;24 hours to prevent metallic lithium plating and internal resistance buildup.</td>
      </tr>
      <tr>
        <td><strong>Safe Landing</strong></td>
        <td>3.50V (Resting)</td>
        <td>21.0V</td>
        <td>Land here to maximize battery lifespan (&gt;250 recharge cycles).</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-rose)">Danger Critical</strong></td>
        <td>&lt; 3.20V</td>
        <td>&lt; 19.2V</td>
        <td>Permanent chemical breakdown, dendrite formation, permanent cell puffing, and fire risk on recharge.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>The C-Rating Reality vs Marketing Claims</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/uBPuwOyh3do" 
              title="LiPo Internal Resistance & C-Rating Truth" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">LiPo Internal Resistance & C-Rating Truth</div>
      </div>
      <a href="https://www.youtube.com/watch?v=uBPuwOyh3do" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Manufacturers advertise exaggerated discharge ratings like "150C" ($\text{Max Current} = \text{Capacity (Ah)} \times C$). A 1300mAh pack with a real 150C rating would deliver 195 Amps continuously—melting its own silicone leads within seconds!</p>
  <p><strong>The True Metric of LiPo Health is Internal Resistance (IR):</strong></p>
  <ul>
    <li><strong>1.5mΩ – 3.0mΩ per cell:</strong> Brand new, premium competition battery pack. Zero voltage sag.</li>
    <li><strong>4.0mΩ – 7.0mΩ per cell:</strong> Healthy pack for daily practice and freestyle.</li>
    <li><strong>&gt; 12.0mΩ per cell:</strong> Degraded pack. Suffers severe voltage sag under throttle; discharge to 0V in salt water and recycle.</li>
  </ul>
</div>

<div class="ch-section">
  <h2>Interactive Flight Time & Voltage Sag Simulator</h2>
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">🔋 LiPo Flight Time & Energy Simulator</span>
      <span style="font-size:12px;color:var(--text-muted)">Discharge Estimator</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:1.25rem;margin-bottom:1.5rem">
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Battery Capacity: <strong id="battCapVal" style="color:var(--accent-blue)">1300 mAh</strong>
        </label>
        <input type="range" min="850" max="2200" value="1300" step="50" id="battCapInput" oninput="updateBattSim()">
      </div>
      <div>
        <label style="font-size:13px;color:var(--text-secondary);display:block;margin-bottom:0.35rem">
          Average Throttle Load: <strong id="battLoadVal" style="color:var(--accent-blue)">24A (Freestyle Flow)</strong>
        </label>
        <input type="range" min="12" max="45" value="24" step="1" id="battLoadInput" oninput="updateBattSim()">
      </div>
    </div>

    <div style="display:flex;gap:1rem;flex-wrap:wrap">
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">ESTIMATED FLIGHT DURATION</span>
        <div class="calc-metric-val" id="battTimeVal" style="color:var(--accent-emerald)">4:20</div>
        <span style="font-size:11px;color:var(--text-muted)">Using 80% Safe Capacity</span>
      </div>
      <div class="calc-metric-box">
        <span class="calc-metric-lbl">EFFECTIVE C-RATE DEMAND</span>
        <div class="calc-metric-val" id="battCRateVal" style="color:var(--accent-blue)">18.5 C</div>
        <span style="font-size:11px;color:var(--text-muted)">Continuous Draw</span>
      </div>
    </div>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 10 CONTENT: VIDEO & RADIO SYSTEMS
// ==========================================
function getCh10Content() {
  return `
<div class="ch-section">
  <h2>The FPV Video Ecosystems Compared</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/TMOeIQ4VRX4" 
              title="Best FPV Goggles Buyer Guide: DJI vs HDZero vs Walksnail vs Analog" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Best FPV Goggles Buyer Guide: DJI vs HDZero vs Walksnail vs Analog</div>
      </div>
      <a href="https://www.youtube.com/watch?v=TMOeIQ4VRX4" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>Your video link is your eyes in the sky. Four competing transmission systems dominate the FPV landscape:</p>

  <table class="data-table">
    <thead>
      <tr><th>System</th><th>Resolution</th><th>Latency</th><th>Degradation Behavior</th><th>Ecosystem Cost</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><strong style="color:var(--accent-amber)">Analog 5.8GHz</strong></td>
        <td>Standard Def (~480p)</td>
        <td>10ms – 18ms (Fixed)</td>
        <td><strong>Graceful Snow.</strong> Signal dissolves into static; pilot maintains horizon orientation.</td>
        <td>Lowest cost entry. Universal open cross-brand compatibility.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-blue)">DJI O3 / O4 HD</strong></td>
        <td>1080p 100fps / 4K Rec</td>
        <td>28ms – 40ms (Variable)</td>
        <td>Resolution drops, then video freezes.</td>
        <td>Premium cost. Closed proprietary ecosystem. Best cinematic image quality.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-emerald)">Walksnail Avatar</strong></td>
        <td>1080p 60fps / 720p 100fps</td>
        <td>22ms (Fast mode)</td>
        <td>Pixelation/smearing before frame loss.</td>
        <td>Open HDMI receiver modules available. Outstanding low-light sensors.</td>
      </tr>
      <tr>
        <td><strong style="color:var(--accent-violet)">HDZero</strong></td>
        <td>720p 60fps / 540p 90fps</td>
        <td>14ms (Zero Latency)</td>
        <td>Degrades like analog with rainbow static; never freezes.</td>
        <td>The competitive racer's choice for digital video.</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Antenna Circular Polarization Physics</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/mbHl3DgnN4k" 
              title="Left vs Right Circular Polarization (LHCP vs RHCP)" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Left vs Right Circular Polarization (LHCP vs RHCP)</div>
      </div>
      <a href="https://www.youtube.com/watch?v=mbHl3DgnN4k" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>FPV radio frequencies utilize <strong>Circular Polarization (CP)</strong>—the electromagnetic wave radiates in a corkscrew pattern:</p>
  <ul>
    <li><strong>Multipath Reflection Rejection:</strong> When a circularly polarized wave bounces off concrete, metal, or wet trees, its rotational direction reverses (RHCP becomes LHCP). The receiving antenna rejects the reversed signal, eliminating ghosting interference!</li>
    <li><strong>The 20dB Cross-Polarization Penalty:</strong> The drone VTX antenna and the goggle antennas <strong>MUST match polarization</strong> (both RHCP or both LHCP). Mixing RHCP on the quad with LHCP on your goggles results in an immediate 20dB–30dB signal penalty, destroying over 90% of your transmission range!</li>
  </ul>
</div>

<div class="ch-section">
  <h2>ExpressLRS: The Open-Source RC King</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/oHA2qhABamc" 
              title="Why I Always Bind ELRS - ExpressLRS Setup Guide" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Why I Always Bind ELRS - ExpressLRS Setup Guide</div>
      </div>
      <a href="https://www.youtube.com/watch?v=oHA2qhABamc" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p><strong>ExpressLRS (ELRS)</strong> has rendered legacy proprietary protocols obsolete by combining Semtech LoRa spread-spectrum hardware with open-source firmware:</p>
  <ul>
    <li><strong>Packet Rates up to 1000Hz:</strong> Transmits stick updates every single millisecond.</li>
    <li><strong>Sub-3ms Latency:</strong> From stick deflection to motor response, latency is imperceptible to humans.</li>
    <li><strong>30+ km Range on 2.4GHz:</strong> Easily outranges video systems even on low 100mW power.</li>
    <li><strong>Antenna Carbon Shielding Rule:</strong> Never tape receiver antennas flat against carbon fiber arms. Always mount them out into clean air using 3D-printed TPU mounts.</li>
  </ul>
</div>
`;
}

// ==========================================
// CHAPTER 11 CONTENT: ASSEMBLY & SOFTWARE
// ==========================================
function getCh11Content() {
  return `
<div class="ch-section">
  <h2>The Step-by-Step Bench Assembly Sequence</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/kfhHecJsS3Y" 
              title="Build an FPV Drone Step by Step - Soldering & Assembly" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Build an FPV Drone Step by Step - Soldering & Assembly</div>
      </div>
      <a href="https://www.youtube.com/watch?v=kfhHecJsS3Y" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <ol>
    <li><strong>Frame Preparation & Dry-Fit:</strong> Sand carbon arm edges lightly, test standoffs, and apply blue threadlocker (Loctite 242) to steel bolts.</li>
    <li><strong>Motor Installation:</strong> Bolt motors to arms. <strong style="color:var(--accent-rose)">VERIFY SCREW DEPTH!</strong> Screws must not penetrate stator windings.</li>
    <li><strong>ESC Power Solder:</strong> Solder heavy 12AWG/14AWG silicone battery leads to the ESC. Solder the 35V 1000µF Low-ESR capacitor directly across the battery pads.</li>
    <li><strong>Smoke Stopper Continuity Test #1:</strong> Plug in a battery through a current-limiting Smoke Stopper. If the bulb lights or electronic fuse trips, locate the solder bridge immediately!</li>
    <li><strong>Flight Controller Mounting:</strong> Soft-mount the FC on silicone gummies. Check that the wiring harness between FC and ESC matches pin-for-pin.</li>
    <li><strong>Receiver Wiring:</strong> Solder Receiver TX to FC RX, and Receiver RX to FC TX. Power from clean 5V BEC.</li>
    <li><strong>VTX & Camera Wiring:</strong> Wire camera to FC video input; wire VTX to filtered 9V/10V BEC.</li>
    <li><strong>Smoke Stopper Continuity Test #2:</strong> Full avionics test. Verify receiver binds and video appears in goggles.</li>
    <li><strong>Betaflight Setup:</strong> Configure software with <strong style="color:var(--accent-rose)">PROPELLERS OFF</strong>.</li>
  </ol>
</div>

<div class="ch-section">
  <h2>The PID Control Loop Explained</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/M-6pq1rFtBI" 
              title="Should I Learn to PID Tune or Use Betaflight Presets?" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Should I Learn to PID Tune or Use Betaflight Presets?</div>
      </div>
      <a href="https://www.youtube.com/watch?v=M-6pq1rFtBI" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(180px, 1fr));gap:0.75rem;margin:1.25rem 0">
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:10px;padding:1rem">
      <span style="color:var(--accent-blue);font-weight:700">P (Proportional)</span>
      <p style="font-size:13px;color:var(--text-secondary);margin:0.25rem 0 0">The corrective muscle. Responds to present error. Too high = rapid oscillation; too low = loose feeling.</p>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:10px;padding:1rem">
      <span style="color:var(--accent-emerald);font-weight:700">I (Integral)</span>
      <p style="font-size:13px;color:var(--text-secondary);margin:0.25rem 0 0">The memory. Accumulates past error over time. Fights steady-state wind drift and aerodynamic drag.</p>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:10px;padding:1rem">
      <span style="color:var(--accent-amber);font-weight:700">D (Derivative)</span>
      <p style="font-size:13px;color:var(--text-secondary);margin:0.25rem 0 0">The shock absorber. Predicts future error by calculating rate of change, dampening P-term overshoot.</p>
    </div>
    <div style="background:var(--bg-surface);border:1px solid var(--border);border-radius:10px;padding:1rem">
      <span style="color:var(--accent-violet);font-weight:700">FF (Feedforward)</span>
      <p style="font-size:13px;color:var(--text-secondary);margin:0.25rem 0 0">The predictor. Looks at stick movement speed and pre-applies motor torque before error occurs.</p>
    </div>
  </div>

  <!-- Interactive PID Visualizer -->
  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">📈 Interactive PID Step Response Visualizer</span>
      <span style="font-size:12px;color:var(--text-muted)">Live Control Loop Simulation</span>
    </div>

    <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(160px, 1fr));gap:1rem;margin-bottom:1.25rem">
      <div>
        <label style="font-size:12px;color:var(--text-secondary)">P GAIN: <strong id="pidPVal" style="color:var(--accent-blue)">45</strong></label>
        <input type="range" min="15" max="95" value="45" id="pidPInput" oninput="drawPidCanvas()">
      </div>
      <div>
        <label style="font-size:12px;color:var(--text-secondary)">D GAIN: <strong id="pidDVal" style="color:var(--accent-amber)">35</strong></label>
        <input type="range" min="10" max="75" value="35" id="pidDInput" oninput="drawPidCanvas()">
      </div>
    </div>

    <div style="background:#060A12;border:1px solid var(--border);border-radius:12px;padding:1rem;margin-bottom:1rem">
      <canvas id="pidCanvas" width="700" height="200" style="width:100%;height:180px"></canvas>
    </div>

    <div style="font-size:13px;color:var(--text-secondary)" id="pidResponseStatus">
      ✓ <strong>Critically Damped:</strong> Rapid rise time with negligible overshoot and zero ringing.
    </div>
  </div>
</div>
`;
}

// ==========================================
// CHAPTER 12 CONTENT: COMPETITION & CONCLUSION
// ==========================================
function getCh12Content() {
  return `
<div class="ch-section">
  <h2>Race Event Frequency Management & Pit Etiquette</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/DwcE68FmFrE" 
              title="What Are The Best Frequencies to Use For FPV? RaceBand & Pit Mode" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">What Are The Best Frequencies to Use For FPV? RaceBand & Pit Mode</div>
      </div>
      <a href="https://www.youtube.com/watch?v=DwcE68FmFrE" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <p>At FPV racing events, up to 8 pilots fly simultaneously on 5.8GHz. Proper frequency management is critical:</p>

  <div class="danger-box">
    <div class="box-label" style="color:var(--accent-rose)">🔥 The Golden Pit Rule: Never Power Up Without Clearance</div>
    <p style="margin:0;font-size:14px;color:var(--text-secondary)">
      Never plug in a battery in the pit area without verifying your assigned video channel and ensuring your VTX is set to <strong>Pit Mode (0.1mW)</strong>. Powering up on an active race channel will instantly blind an airborne pilot, causing high-speed crashes and potential injury!
    </p>
  </div>

  <table class="data-table">
    <thead>
      <tr><th>Race Channel</th><th>Frequency</th><th>Spacing Rule</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>RaceBand 1 (R1)</strong></td><td>5658 MHz</td><td rowspan="8" style="vertical-align:middle;color:var(--accent-emerald)"><strong>37MHz Minimum Separation:</strong> Standardized frequency spacing prevents third-order Intermodulation Distortion (IMD) products from blinding neighboring receivers.</td></tr>
      <tr><td><strong>RaceBand 2 (R2)</strong></td><td>5695 MHz</td></tr>
      <tr><td><strong>RaceBand 3 (R3)</strong></td><td>5732 MHz</td></tr>
      <tr><td><strong>RaceBand 4 (R4)</strong></td><td>5769 MHz</td></tr>
      <tr><td><strong>RaceBand 5 (R5)</strong></td><td>5806 MHz</td></tr>
      <tr><td><strong>RaceBand 6 (R6)</strong></td><td>5843 MHz</td></tr>
      <tr><td><strong>RaceBand 7 (R7)</strong></td><td>5880 MHz</td></tr>
      <tr><td><strong>RaceBand 8 (R8)</strong></td><td>5917 MHz</td></tr>
    </tbody>
  </table>
</div>

<div class="ch-section">
  <h2>Interactive Master Pre-Flight Checklist</h2>

  <div style="background:#0B101D;border:1px solid rgba(99,102,241,0.25);border-radius:16px;overflow:hidden;margin:1.5rem 0;box-shadow:0 8px 25px rgba(0,0,0,0.35)">
    <div style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden">
      <iframe src="https://www.youtube-nocookie.com/embed/O5ngG--_pKo" 
              title="Failsafe Setup and Test in Betaflight to Prevent Flyaways" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:0" 
              allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
              allowfullscreen></iframe>
    </div>
    <div style="padding:0.85rem 1.15rem;display:flex;align-items:center;justify-content:space-between;gap:0.75rem;flex-wrap:wrap">
      <div>
        <div style="font-size:11px;font-weight:700;color:var(--accent-indigo);text-transform:uppercase;letter-spacing:0.04em">📺 TUTORIAL SPOTLIGHT • Joshua Bardwell</div>
        <div style="font-size:13px;font-weight:700;color:#F8FAFC;margin-top:0.15rem">Failsafe Setup and Test in Betaflight to Prevent Flyaways</div>
      </div>
      <a href="https://www.youtube.com/watch?v=O5ngG--_pKo" target="_blank" rel="noopener" class="btn-secondary" style="font-size:12px;padding:0.35rem 0.75rem">
        Watch on YouTube ↗
      </a>
    </div>
  </div>

  <div class="widget-card">
    <div class="widget-header">
      <span class="widget-title">✅ Master Flight & Safety Inspection Checklist</span>
      <span style="font-size:12px;color:var(--text-muted)">12-Point Inspection</span>
    </div>

    <div id="checklistItems">
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Propeller locknuts tightened firmly down to nylon ring</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Propellers installed with text facing UP and matching motor rotation</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Battery strapped securely with two rubberized Kevlar straps</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Balance lead tucked away from spinning propeller path</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">VTX antenna screwed on securely (never power without antenna)</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Receiver antennas clear of carbon chassis and propeller blades</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Failsafe tested: turning off radio immediately shuts down motors</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Arming switch and Acro/Angle switches verified in goggles OSD</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Battery cell voltage checked (4.20V per cell full charge)</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Flight field is clear of non-participating people and obstacles</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">Visual spotter is present to maintain continuous Line-of-Sight</span></div>
      <div class="check-row" onclick="toggleFlightCheck(this)"><div class="check-circle">✓</div><span style="font-size:14px">HD recording camera (GoPro/O3) started and locked in</span></div>
    </div>

    <div style="margin-top:1.25rem">
      <div class="progress-track" style="height:10px"><div class="progress-fill" id="flightCheckProgress" style="width:0%"></div></div>
      <div style="display:flex;align-items:center;justify-content:space-between;font-size:13px;color:var(--text-secondary);margin-top:0.5rem">
        <span id="flightCheckCount">0 of 12 items verified</span>
        <span id="flightCheckReadyText" style="font-weight:700;color:var(--text-muted)">Inspection Incomplete</span>
      </div>
    </div>
  </div>
</div>

<div class="ch-section">
  <h2>Aviation Regulations & Ethical Flying</h2>
  <ul>
    <li><strong>Visual Line of Sight (VLOS) with Spotter:</strong> Aviation authorities (DGCA India Digital Sky / FAA Part 107) require that whenever flying with FPV goggles, a visual observer/spotter must stand beside you to maintain unaided line of sight with the airspace.</li>
    <li><strong>Altitude Limits:</strong> Maximum permissible altitude for recreational drone flight is <strong>120 meters (400 feet) Above Ground Level (AGL)</strong>.</li>
    <li><strong>Airspace Restrictions:</strong> Never fly within 5 km of an active airport, military base, government facility, or over crowded public gatherings.</li>
  </ul>
</div>

<div class="ch-section">
  <h2>Conclusion: Your FPV Journey Begins</h2>
  <p>You now possess the complete theoretical and engineering foundation of FPV quadcopter robotics. From aerodynamic airfoil physics and stator electromagnetics to Betaflight PID tuning and high-speed race execution, you are equipped to build, tune, and fly your own custom aircraft.</p>
  <div class="spec-box" style="border-left-color:var(--accent-emerald)">
    <div class="box-label" style="color:var(--accent-emerald)">🎓 Recommended Next Steps</div>
    <div style="font-size:14px;color:var(--text-secondary)">
      1. Log 15+ hours in an FPV simulator (Velocidrone / Liftoff).<br>
      2. Gather your workbench tools: soldering iron, multimeter, smoke stopper, and hex drivers.<br>
      3. Build your reference 5-inch 6S quadcopter following the Chapter 11 assembly sequence.<br>
      4. Connect with your local FPV flying club or university robotics team and take to the skies!
    </div>
  </div>
</div>
`;
}

// ==========================================
// CORE APP ROUTER & LOGIC
// ==========================================
function getChapterContentById(id) {
  let raw = "";
  try {
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
  } catch (err) {
    console.error("Error generating chapter body for " + id + ":", err);
    raw = '<div style="padding:2rem;color:#FDA4AF">Error generating chapter content: ' + err.message + '</div>';
  }

  try {
    if (typeof getQnaSectionHtml === 'function') {
      raw += getQnaSectionHtml(id);
    }
  } catch (qnaErr) {
    console.warn("Error generating QnA section for " + id + ":", qnaErr);
  }

  return raw;
}

function navigate(target) {
  if (target === 'home') {
    document.getElementById('page-home').classList.add('active');
    document.getElementById('page-chapter').classList.remove('active');
    document.getElementById('backBtn').style.display = 'none';
    activeChapterId = null;
    if (window.location.hash !== '#home') {
      window.location.hash = '#home';
    }
  } else {
    const idx = CHAPTERS.findIndex(c => c.id === target);
    if (idx === -1) return;
    activeChapterId = target;
    const ch = CHAPTERS[idx];

    document.getElementById('page-home').classList.remove('active');
    document.getElementById('page-chapter').classList.add('active');
    document.getElementById('backBtn').style.display = 'inline-block';
    
    document.getElementById('chapterLabel').textContent = 'CHAPTER ' + (idx + 1);
    document.getElementById('chapterPosition').textContent = 'Lesson ' + (idx + 1) + ' of ' + CHAPTERS.length;
    document.getElementById('chapterTitle').textContent = ch.title;
    document.getElementById('chapterSubtitle').textContent = ch.subtitle;
    try {
      const content = getChapterContentById(target);
      document.getElementById('chapterContent').innerHTML = content;
    } catch (e) {
      console.error('Render error:', e);
      document.getElementById('chapterContent').innerHTML = '<div style="padding:2rem;color:#FDA4AF">Failed to render chapter content. Error: ' + e.message + '</div>';
    }

    // Prev / Next Buttons
    const prevBtn = document.getElementById('prevChapterBtn');
    if (idx === 0) {
      prevBtn.style.visibility = 'hidden';
    } else {
      prevBtn.style.visibility = 'visible';
    }

    const nextBtn = document.getElementById('nextChapterBtn');
    if (idx === CHAPTERS.length - 1) {
      nextBtn.textContent = '🏠 Return to Syllabus';
    } else {
      nextBtn.textContent = 'Next Lesson →';
    }

    // Complete Button
    updateCompleteBtnState();

    if (window.location.hash !== '#' + target) {
      window.location.hash = '#' + target;
    }
    window.scrollTo(0, 0);

    // Initialize in-chapter widgets
    initChapterWidgets(target);
  }
  updateCourseProgress();
  closeDrawer();
}

function prevChapter() {
  if (!activeChapterId) return;
  const idx = CHAPTERS.findIndex(c => c.id === activeChapterId);
  if (idx > 0) {
    navigate(CHAPTERS[idx - 1].id);
  }
}

function nextChapter() {
  if (!activeChapterId) return;
  const idx = CHAPTERS.findIndex(c => c.id === activeChapterId);
  if (idx < CHAPTERS.length - 1) {
    navigate(CHAPTERS[idx + 1].id);
  } else {
    navigate('home');
  }
}

function toggleCompleteCurrent() {
  if (!activeChapterId) return;
  progress[activeChapterId] = !progress[activeChapterId];
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
  syncWithDatabase();
  updateCompleteBtnState();
  updateCourseProgress();
}

function updateCompleteBtnState() {
  const btn = document.getElementById('markCompleteBtn');
  if (progress[activeChapterId]) {
    btn.innerHTML = '✓ Lesson Mastered';
    btn.style.opacity = '0.7';
  } else {
    btn.innerHTML = '✓ Mark as Complete';
    btn.style.opacity = '1';
  }
}

function updateCourseProgress() {
  const completed = CHAPTERS.filter(c => progress[c.id]).length;
  const total = CHAPTERS.length;
  const pct = Math.round((completed / total) * 100);

  document.getElementById('headerProgress').style.width = pct + '%';
  document.getElementById('headerProgressText').textContent = completed + '/' + total;

  const homeBar = document.getElementById('homeProgressBar');
  if (homeBar) homeBar.style.width = pct + '%';
  const homeTitle = document.getElementById('homeProgressTitle');
  if (homeTitle) homeTitle.textContent = completed + ' of ' + total + ' Chapters Mastered';
  const homePct = document.getElementById('homeProgressPercent');
  if (homePct) homePct.textContent = pct + '%';

  renderHomeChapterList();
  renderDrawerList();
}

function renderHomeChapterList() {
  const list = document.getElementById('chapterList');
  if (!list) return;

  list.innerHTML = CHAPTERS.map((ch, idx) => {
    const isDone = !!progress[ch.id];
    return `
      <div class="chapter-card ${isDone ? 'completed' : ''}" onclick="navigate('${ch.id}')">
        <div class="chapter-icon" style="background:${ch.color}22">
          <span>${isDone ? '✓' : ch.icon}</span>
        </div>
        <div style="flex:1;min-width:0">
          <div style="display:flex;align-items:center;justify-content:space-between;gap:0.5rem">
            <div style="font-size:11px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em">
              CHAPTER ${idx + 1}
            </div>
            <span style="font-size:12px;color:var(--text-muted);white-space:nowrap">${ch.time}</span>
          </div>
          <h3 style="font-size:16px;font-weight:700;color:var(--text-primary);margin:0.15rem 0">${ch.title}</h3>
          <p style="font-size:13px;color:var(--text-secondary);margin:0">${ch.subtitle}</p>
        </div>
        <div style="color:var(--text-muted);font-size:18px">→</div>
      </div>
    `;
  }).join('');
}

function renderDrawerList() {
  const list = document.getElementById('drawerList');
  if (!list) return;

  list.innerHTML = CHAPTERS.map((ch, idx) => {
    const isDone = !!progress[ch.id];
    return `
      <div style="padding:0.75rem 0.85rem;border-radius:10px;cursor:pointer;display:flex;align-items:center;gap:0.75rem;transition:background 0.2s"
           onclick="navigate('${ch.id}')"
           onmouseover="this.style.background='var(--bg-hover)'"
           onmouseout="this.style.background='transparent'">
        <span style="font-size:16px">${isDone ? '✓' : ch.icon}</span>
        <div style="flex:1;min-width:0">
          <div style="font-size:13px;font-weight:600;color:${activeChapterId === ch.id ? 'var(--accent-blue)' : 'var(--text-primary)'}">
            ${idx + 1}. ${ch.title}
          </div>
        </div>
      </div>
    `;
  }).join('');
}

function openDrawer() {
  document.getElementById('mobileDrawer').classList.add('open');
  document.getElementById('mobileOverlay').classList.add('show');
}

function closeDrawer() {
  document.getElementById('mobileDrawer').classList.remove('open');
  document.getElementById('mobileOverlay').classList.remove('show');
}

// ==========================================
// INTERACTIVE WIDGET INITIALIZATION & LOGIC
// ==========================================
function initChapterWidgets(id) {
  try {
    if (id === 'ch1') {
      resetSticks();
    } else if (id === 'ch2') {
      setGeoTab('truex', document.querySelector('#geoDisplay') ? document.querySelector('.seg-tab') : null);
    } else if (id === 'ch3') {
      updatePhysicsCalc();
    } else if (id === 'ch4') {
      updateSpecBuilder();
    } else if (id === 'ch5') {
      updateMotorExplorer();
    } else if (id === 'ch6') {
      updatePropSpeedCalc();
    } else if (id === 'ch7') {
      updateEscSafetyCalc();
    } else if (id === 'ch8') {
      // UART Planner
    } else if (id === 'ch9') {
      updateBattSim();
    } else if (id === 'ch11') {
      setTimeout(drawPidCanvas, 50);
    }
  } catch (err) {
    console.warn("Widget init error:", err);
  }
}

// CH1: Virtual Stick Gimbal
let activeGimbal = null;
function startStickDrag(e, type) {
  activeGimbal = type;
  handleStickMove(e);
  window.addEventListener('pointermove', handleStickMove);
  window.addEventListener('pointerup', stopStickDrag);
}

function handleStickMove(e) {
  if (!activeGimbal) return;
  const gimbal = document.getElementById(activeGimbal === 'left' ? 'leftGimbal' : 'rightGimbal');
  const pointer = document.getElementById(activeGimbal === 'left' ? 'leftPointer' : 'rightPointer');
  const rect = gimbal.getBoundingClientRect();
  const radius = rect.width / 2;

  let x = e.clientX - rect.left - radius;
  let y = e.clientY - rect.top - radius;
  const dist = Math.sqrt(x * x + y * y);
  const maxR = radius - 14;

  if (dist > maxR) {
    x = (x / dist) * maxR;
    y = (y / dist) * maxR;
  }

  pointer.style.transform = `translate(calc(-50% + ${x}px), calc(-50% + ${y}px))`;

  const normX = (x / maxR).toFixed(2);
  const normY = (-y / maxR).toFixed(2);

  if (activeGimbal === 'left') {
    const thr = Math.round(((parseFloat(normY) + 1) / 2) * 100);
    const yawRate = Math.round(parseFloat(normX) * 600);
    document.getElementById('leftGimbalVal').textContent = `Throttle: ${thr}% | Yaw: ${yawRate}°/s`;
    updateStickReactionText(thr, yawRate, null, null);
  } else {
    const pitch = Math.round(parseFloat(normY) * 55);
    const roll = Math.round(parseFloat(normX) * 55);
    document.getElementById('rightGimbalVal').textContent = `Pitch: ${pitch}° | Roll: ${roll}°`;
    updateStickReactionText(null, null, pitch, roll);
  }
}

function stopStickDrag() {
  activeGimbal = null;
  window.removeEventListener('pointermove', handleStickMove);
  window.removeEventListener('pointerup', stopStickDrag);
}

function resetSticks() {
  const lp = document.getElementById('leftPointer');
  const rp = document.getElementById('rightPointer');
  if (lp) lp.style.transform = 'translate(-50%, -50%)';
  if (rp) rp.style.transform = 'translate(-50%, -50%)';
  const lv = document.getElementById('leftGimbalVal');
  if (lv) lv.textContent = 'Throttle: 50% | Yaw: 0°/s';
  const rv = document.getElementById('rightGimbalVal');
  if (rv) rv.textContent = 'Pitch: 0° | Roll: 0°';
  const rx = document.getElementById('stickReactionText');
  if (rx) rx.textContent = 'Level Hover State (50% Throttle)';
}

function updateStickReactionText(thr, yaw, pitch, roll) {
  const el = document.getElementById('stickReactionText');
  if (!el) return;
  if (pitch !== null && (Math.abs(pitch) > 10 || Math.abs(roll) > 10)) {
    el.textContent = `Banking ${roll > 10 ? 'Right' : (roll < -10 ? 'Left' : '')} & Pitching ${pitch > 10 ? 'Forward (Accelerating)' : (pitch < -10 ? 'Back (Braking)' : '')}`;
  } else if (thr !== null) {
    if (thr > 70) el.textContent = 'High-Speed Vertical Climb (Full Power)';
    else if (thr < 30) el.textContent = 'Rapid Inverted Zero-G Float / Descent';
    else el.textContent = 'Level Hover State (50% Throttle)';
  }
}

function setCompTab(type, btn) {
  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.seg-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
  }
  const display = document.getElementById('compDisplay');
  if (!display) return;
  if (type === 'fpv') {
    display.innerHTML = `
      <table class="data-table" style="margin:0">
        <tbody>
          <tr><td><strong>Top Airspeed</strong></td><td style="color:var(--accent-emerald);font-weight:700">140 – 210 km/h (85 – 130 mph)</td></tr>
          <tr><td><strong>Thrust-to-Weight Ratio</strong></td><td style="color:var(--accent-emerald);font-weight:700">5:1 (Freestyle) to 12:1+ (Racing)</td></tr>
          <tr><td><strong>Flight Stabilization</strong></td><td>Pure manual gyroscopic rate control (Acro)</td></tr>
          <tr><td><strong>Video Latency</strong></td><td style="color:var(--accent-emerald);font-weight:700">10ms – 28ms (Zero/Near-Zero latency)</td></tr>
          <tr><td><strong>Crash Resilience</strong></td><td style="color:var(--accent-emerald);font-weight:700">Carbon fiber frame survives concrete impacts at 100 km/h</td></tr>
          <tr><td><strong>Repairability</strong></td><td style="color:var(--accent-emerald);font-weight:700">100% modular DIY; every component replaceable with a soldering iron</td></tr>
          <tr><td><strong>Flight Duration</strong></td><td>3.5 – 6.5 minutes per battery pack</td></tr>
        </tbody>
      </table>
    `;
  } else {
    display.innerHTML = `
      <table class="data-table" style="margin:0">
        <tbody>
          <tr><td><strong>Top Airspeed</strong></td><td>55 – 70 km/h (35 – 45 mph)</td></tr>
          <tr><td><strong>Thrust-to-Weight Ratio</strong></td><td>~2:1 (Gentle climb authority)</td></tr>
          <tr><td><strong>Flight Stabilization</strong></td><td>Dual GPS + Optical Flow + Sonar Auto-Hover</td></tr>
          <tr><td><strong>Video Latency</strong></td><td>120ms – 200ms (Unsuitable for manual acrobatic flight)</td></tr>
          <tr><td><strong>Crash Resilience</strong></td><td style="color:var(--accent-rose)">Plastic unibody shell cracks easily on branch impact</td></tr>
          <tr><td><strong>Repairability</strong></td><td style="color:var(--accent-rose)">Proprietary; requires factory service return</td></tr>
          <tr><td><strong>Flight Duration</strong></td><td style="color:var(--accent-emerald);font-weight:700">25 – 40 minutes (Li-Ion slow cruising)</td></tr>
        </tbody>
      </table>
    `;
  }
}

// CH2: Airframe Geometry SVG
function setGeoTab(type, btn) {
  if (btn && btn.parentElement) {
    btn.parentElement.querySelectorAll('.seg-tab').forEach(t => t.classList.remove('active'));
    btn.classList.add('active');
  }
  const svg = document.getElementById('geoSvg');
  const desc = document.getElementById('geoDescription');
  if (!svg || !desc) return;

  if (type === 'truex') {
    svg.innerHTML = `
      <line x1="40" y1="40" x2="200" y2="200" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <line x1="200" y1="40" x2="40" y2="200" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <rect x="95" y="95" width="50" height="50" rx="8" fill="#1E293B" stroke="#6366F1" stroke-width="2"/>
      <circle cx="40" cy="40" r="18" fill="none" stroke="#3B82F6" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="200" cy="40" r="18" fill="none" stroke="#3B82F6" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="40" cy="200" r="18" fill="none" stroke="#3B82F6" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="200" cy="200" r="18" fill="none" stroke="#3B82F6" stroke-width="2" stroke-dasharray="4"/>
      <text x="120" y="125" text-anchor="middle" fill="#A5B4FC" font-size="11" font-weight="700">90° EQUAL</text>
    `;
    desc.innerHTML = `
      <h3 style="color:var(--accent-blue);font-size:18px;margin-top:0">True-X Airframe Geometry</h3>
      <p style="font-size:14px;color:var(--text-secondary)">
        Arms form a perfectly symmetrical 90° layout. Moments of inertia across the roll and pitch axes are identical ($I_{xx} \approx I_{yy}$), producing balanced, predictable handling during freestyle axial rolls and flips.
      </p>
      <div style="font-size:12px;color:var(--text-muted)"><strong>Best for:</strong> Pure Acrobatic Freestyle & MultiGP Standard Class.</div>
    `;
  } else if (type === 'stretchx') {
    svg.innerHTML = `
      <line x1="60" y1="30" x2="180" y2="210" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <line x1="180" y1="30" x2="60" y2="210" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <rect x="95" y="95" width="50" height="50" rx="8" fill="#1E293B" stroke="#10B981" stroke-width="2"/>
      <circle cx="60" cy="30" r="18" fill="none" stroke="#10B981" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="180" cy="30" r="18" fill="none" stroke="#10B981" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="60" cy="210" r="18" fill="none" stroke="#10B981" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="180" cy="210" r="18" fill="none" stroke="#10B981" stroke-width="2" stroke-dasharray="4"/>
      <text x="120" y="125" text-anchor="middle" fill="#6EE7B7" font-size="11" font-weight="700">STRETCH</text>
    `;
    desc.innerHTML = `
      <h3 style="color:var(--accent-emerald);font-size:18px;margin-top:0">Stretch-X Geometry</h3>
      <p style="font-size:14px;color:var(--text-secondary)">
        Front-to-back distance exceeds side-to-side distance. Rear motors fly in cleaner, undisturbed air (outside the propwash wake of the front blades during forward pitch). Improves high-speed forward pitch stability.
      </p>
      <div style="font-size:12px;color:var(--text-muted)"><strong>Best for:</strong> High-Speed Competition Racing & Drag Punchouts.</div>
    `;
  } else if (type === 'deadcat') {
    svg.innerHTML = `
      <line x1="25" y1="65" x2="105" y2="120" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <line x1="215" y1="65" x2="135" y2="120" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <line x1="45" y1="205" x2="105" y2="120" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <line x1="195" y1="205" x2="135" y2="120" stroke="#475569" stroke-width="8" stroke-linecap="round"/>
      <rect x="90" y="90" width="60" height="55" rx="8" fill="#1E293B" stroke="#F59E0B" stroke-width="2"/>
      <polygon points="120,60 90,85 150,85" fill="#EF4444" opacity="0.3"/>
      <text x="120" y="50" text-anchor="middle" fill="#F59E0B" font-size="10" font-weight="700">NO PROPS IN FOV</text>
      <circle cx="25" cy="65" r="18" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="215" cy="65" r="18" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="45" cy="205" r="18" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="4"/>
      <circle cx="195" cy="205" r="18" fill="none" stroke="#F59E0B" stroke-width="2" stroke-dasharray="4"/>
    `;
    desc.innerHTML = `
      <h3 style="color:var(--accent-amber);font-size:18px;margin-top:0">Deadcat (DC) Geometry</h3>
      <p style="font-size:14px;color:var(--text-secondary)">
        Front arms are pushed out laterally and swept back. This eliminates spinning propellers from the wide-angle field of view (FOV) of onboard DJI O3/O4 or GoPro HD cameras.
      </p>
      <div style="font-size:12px;color:var(--text-muted)"><strong>Best for:</strong> Cinematic Filming & Mountain Surfing (Clean Video).</div>
    `;
  } else {
    svg.innerHTML = `
      <rect x="95" y="95" width="50" height="50" rx="8" fill="#1E293B" stroke="#8B5CF6" stroke-width="2"/>
      <circle cx="50" cy="50" r="32" fill="#8B5CF6" opacity="0.15" stroke="#8B5CF6" stroke-width="3"/>
      <circle cx="190" cy="50" r="32" fill="#8B5CF6" opacity="0.15" stroke="#8B5CF6" stroke-width="3"/>
      <circle cx="50" cy="190" r="32" fill="#8B5CF6" opacity="0.15" stroke="#8B5CF6" stroke-width="3"/>
      <circle cx="190" cy="190" r="32" fill="#8B5CF6" opacity="0.15" stroke="#8B5CF6" stroke-width="3"/>
      <text x="120" y="125" text-anchor="middle" fill="#C084FC" font-size="11" font-weight="700">DUCTED</text>
    `;
    desc.innerHTML = `
      <h3 style="color:var(--accent-violet);font-size:18px;margin-top:0">Ducted Cinewhoop</h3>
      <p style="font-size:14px;color:var(--text-secondary)">
        Propellers are completely enclosed in high-impact plastic or foam ducts. Protects people, walls, and delicate indoor items from spinning blades, allowing close-proximity filming.
      </p>
      <div style="font-size:12px;color:var(--text-muted)"><strong>Best for:</strong> Indoor Commercials, Real Estate & People Proximity.</div>
    `;
  }
}

// CH3: Physics Calculator
function updatePhysicsCalc() {
  const auw = parseFloat(document.getElementById('twrAuwInput').value);
  const motorThrust = parseFloat(document.getElementById('twrThrustInput').value);
  document.getElementById('twrAuwVal').textContent = auw;
  document.getElementById('twrThrustVal').textContent = motorThrust;

  const totalThrust = motorThrust * 4;
  const twr = (totalThrust / auw).toFixed(2);
  const hoverThrottle = Math.min(100, Math.round((1 / twr) * 100));
  const gForce = (twr - 1).toFixed(2);
  const accel = ((twr - 1) * 9.81).toFixed(1);

  document.getElementById('physTotalThrust').textContent = totalThrust.toLocaleString() + 'g';
  document.getElementById('physTwr').textContent = twr + ' : 1';
  document.getElementById('physHoverThrottle').textContent = hoverThrottle + '%';
  document.getElementById('physGForce').textContent = gForce + ' G';

  let twrClass = 'Casual Cruiser';
  let color = 'var(--accent-blue)';
  let verdict = '';

  if (twr < 3) {
    twrClass = 'Sluggish Cruiser';
    color = 'var(--accent-amber)';
    verdict = '⚠ Marginal Thrust-to-Weight Ratio: Sluggish flight dynamics. Heavy descent recovery lag.';
  } else if (twr <= 6.5) {
    twrClass = 'Ideal Freestyle';
    color = 'var(--accent-emerald)';
    verdict = '✓ Perfect Freestyle Setup: Balanced throttle control with crisp zero-throttle float and plenty of power.';
  } else {
    twrClass = 'Competition Class';
    color = 'var(--accent-violet)';
    verdict = '✓ Elite Competition Racing Setup: Explosive acceleration. Blistering straightaway top speeds.';
  }

  document.getElementById('physTwrClass').textContent = twrClass;
  document.getElementById('physTwr').style.color = color;
  document.getElementById('physVerdictText').innerHTML = verdict;
}

// CH4: Master Spec Builder
function updateSpecBuilder() {
  const frameEl = document.getElementById('specFrame');
  const motorEl = document.getElementById('specMotor');
  const propEl = document.getElementById('specProp');
  const escEl = document.getElementById('specEsc');
  const battEl = document.getElementById('specBatt');
  const vtxEl = document.getElementById('specVtx');
  if (!frameEl || !motorEl || !propEl || !escEl || !battEl || !vtxEl) return;

  const frame = frameEl.value;
  const motor = motorEl.value;
  const prop = propEl.value;
  const esc = parseInt(escEl.value) || 50;
  const batt = battEl.value || '6s_1100';
  const vtx = vtxEl.value || 'analog';

  let baseWeight = 0;
  if (frame === 'freestyle_5') baseWeight += 125;
  else if (frame === 'race_5') baseWeight += 70;
  else baseWeight += 140;

  // Motors (4x)
  baseWeight += 32 * 4; // ~128g
  // Props (4x)
  baseWeight += 4.5 * 4; // 18g
  // ESC + FC Stack
  baseWeight += 28;
  // Battery
  if (batt === '6s_1100') baseWeight += 190;
  else if (batt === '6s_1300') baseWeight += 215;
  else if (batt === '6s_1800') baseWeight += 290;
  else baseWeight += 180;

  // VTX
  if (vtx === 'analog') baseWeight += 25;
  else if (vtx === 'dji') baseWeight += 42;
  else if (vtx === 'walksnail') baseWeight += 35;
  else baseWeight += 32;

  // Misc hardware & wiring
  baseWeight += 25;

  let peakAmp = 38;
  if (motor === '2207_2100') peakAmp = 46;
  if (prop === '5146') peakAmp += 5;
  if (prop === '5030') peakAmp -= 7;

  const escMargin = (((esc - peakAmp) / peakAmp) * 100).toFixed(1);
  const totalThrust = (motor === '2207_2100' ? 1850 : 1650) * 4;
  const twr = (totalThrust / baseWeight).toFixed(1);

  const auwEl = document.getElementById('specAuw');
  if (auwEl) auwEl.textContent = baseWeight + 'g';
  const ampEl = document.getElementById('specPeakAmp');
  if (ampEl) ampEl.textContent = peakAmp.toFixed(1) + 'A';
  const escMarginEl = document.getElementById('specEscMargin');
  if (escMarginEl) {
    escMarginEl.textContent = (escMargin > 0 ? '+' : '') + escMargin + '%';
    if (escMargin < 15) escMarginEl.style.color = 'var(--accent-rose)';
    else if (escMargin < 25) escMarginEl.style.color = 'var(--accent-amber)';
    else escMarginEl.style.color = 'var(--accent-emerald)';
  }
  const twrEl = document.getElementById('specTwr');
  if (twrEl) twrEl.textContent = twr + ' : 1';

  // Rationale text
  const is6S = batt && batt.startsWith('6s');
  let rationale = `
    <strong>Architecture Analysis & Compatibility Report:</strong><br>
    • <strong>Motor/Prop Harmony:</strong> Selected motor stator volume reliably drives the selected propeller load without thermal saturation.<br>
    • <strong>Voltage System:</strong> ${is6S ? '6S Voltage reduces resistive heat dissipation ($I^2R$) by over 50% compared to legacy 4S systems.' : 'Legacy 4S configuration draws higher current; ensure heavy battery leads.'}<br>
    • <strong>ESC Headroom:</strong> ${escMargin >= 25 ? 'Outstanding +25% safety margin protects MOSFET gates against heat failure.' : '<span style="color:var(--accent-rose)">Warning: Low ESC headroom. Upgrade to 55A+ rating for high throttle safety.</span>'}<br>
    • <strong>Weight-to-Power Balance:</strong> ${twr >= 8 ? 'Competition-grade punchout power with razor-sharp acrobatic agility.' : 'Predictable, smooth freestyle cruise profile.'}
  `;
  const rationaleBox = document.getElementById('specRationaleBox');
  if (rationaleBox) rationaleBox.innerHTML = rationale;
}

// CH5: Motor Explorer
function updateMotorExplorer() {
  const cells = parseInt(document.getElementById('motorCellInput').value);
  const kv = parseInt(document.getElementById('motorKvInput').value);
  document.getElementById('motorCellVal').textContent = `${cells}S (${(cells * 3.7).toFixed(1)}V - ${(cells * 4.2).toFixed(1)}V)`;
  document.getElementById('motorKvVal').textContent = kv + ' KV';

  const maxV = cells * 4.2;
  const maxRpm = Math.round(kv * maxV);
  const workRpm = Math.round(maxRpm * 0.8);

  document.getElementById('motorMaxRpm').textContent = maxRpm.toLocaleString();
  document.getElementById('motorWorkRpm').textContent = workRpm.toLocaleString();

  const zoneEl = document.getElementById('motorZoneText');
  if (workRpm < 32000) {
    zoneEl.textContent = '⚠ Low RPM (Slow/Cruiser)';
    zoneEl.style.color = 'var(--accent-amber)';
  } else if (workRpm <= 44000) {
    zoneEl.textContent = '✓ Optimal 5" Freestyle';
    zoneEl.style.color = 'var(--accent-emerald)';
  } else {
    zoneEl.textContent = '⚡ Extreme Racing / Hot';
    zoneEl.style.color = 'var(--accent-rose)';
  }
}

// CH6: Prop Speed Calculator
function updatePropSpeedCalc() {
  const pitch = parseFloat(document.getElementById('propPitchInput').value);
  const rpm = parseInt(document.getElementById('propRpmInput').value);
  document.getElementById('propPitchVal').textContent = pitch.toFixed(1) + ' inches';
  document.getElementById('propRpmVal').textContent = rpm.toLocaleString() + ' RPM';

  const mph = (pitch * rpm) / 1056;
  const kmh = mph * 1.60934;
  const realKmh = kmh * 0.65;

  document.getElementById('propPitchSpeedMph').textContent = mph.toFixed(1) + ' mph';
  document.getElementById('propPitchSpeedKmh').textContent = kmh.toFixed(1) + ' km/h';
  document.getElementById('propRealSpeedKmh').textContent = realKmh.toFixed(1) + ' km/h';
}

// CH7: ESC Safety Calculator
function updateEscSafetyCalc() {
  const motor = parseInt(document.getElementById('escMotorInput').value);
  const esc = parseInt(document.getElementById('escRatingInput').value);
  document.getElementById('escMotorVal').textContent = motor + 'A';
  document.getElementById('escRatingVal').textContent = esc + 'A';

  const margin = (((esc - motor) / motor) * 100).toFixed(1);
  const valEl = document.getElementById('escMarginVal');
  const verdictEl = document.getElementById('escVerdict');
  valEl.textContent = (margin > 0 ? '+' : '') + margin + '%';

  if (margin < 15) {
    valEl.style.color = 'var(--accent-rose)';
    verdictEl.innerHTML = '<span style="color:var(--accent-rose)">✗ Dangerous: ESC is under-rated. Thermal saturation during full punchouts will blow MOSFETs.</span>';
  } else if (margin < 25) {
    valEl.style.color = 'var(--accent-amber)';
    verdictEl.innerHTML = '<span style="color:var(--accent-amber)">⚠ Risky: Minimal safety headroom. ESC will run hot in summer temperatures.</span>';
  } else {
    valEl.style.color = 'var(--accent-emerald)';
    verdictEl.innerHTML = '<span style="color:var(--accent-emerald)">✓ Safe Margin: Adequate headroom to absorb current spikes in hot weather.</span>';
  }
}

// CH8: UART Planner
let uartChecks = { vtx: false, gps: false, telem: false, audio: false };
function toggleUartCheck(el) {
  const id = el.id.replace('uartCheck', '').toLowerCase();
  uartChecks[id] = !uartChecks[id];
  el.classList.toggle('done');
  document.getElementById('uartDot' + el.id.replace('uartCheck', '')).textContent = uartChecks[id] ? '✓' : '';

  let count = 1; // Receiver always counted
  if (uartChecks.vtx) count++;
  if (uartChecks.gps) count++;
  if (uartChecks.telem) count++;
  if (uartChecks.audio) count++;

  document.getElementById('uartNeededCount').textContent = count + ' Hardware UART' + (count > 1 ? 's' : '');
  const compEl = document.getElementById('uartCompatibility');

  if (count <= 3) {
    compEl.innerHTML = 'Compatible with <strong>F405 (3 ports)</strong>, <strong>F722 (5 ports)</strong>, and <strong>H743 (7 ports)</strong>.';
  } else if (count <= 5) {
    compEl.innerHTML = 'Requires <strong style="color:var(--accent-blue)">F722 (5 ports)</strong> or <strong>H743 (7 ports)</strong>. (F405 will run out of pins).';
  } else {
    compEl.innerHTML = '<strong style="color:var(--accent-violet)">Requires STM32H743</strong>. High peripheral demand exceeds standard F722 capacity.';
  }
}

// CH9: Battery Simulator
function updateBattSim() {
  const cap = parseInt(document.getElementById('battCapInput').value);
  const load = parseInt(document.getElementById('battLoadInput').value);
  document.getElementById('battCapVal').textContent = cap + ' mAh';
  document.getElementById('battLoadVal').textContent = load + 'A';

  const usableAh = (cap * 0.8) / 1000;
  const hours = usableAh / load;
  const totalSecs = Math.round(hours * 3600);
  const mins = Math.floor(totalSecs / 60);
  const secs = totalSecs % 60;

  const cRate = (load / (cap / 1000)).toFixed(1);

  document.getElementById('battTimeVal').textContent = `${mins}:${secs < 10 ? '0' : ''}${secs}`;
  document.getElementById('battCRateVal').textContent = cRate + ' C';
}

// CH11: PID Step Response Canvas
function drawPidCanvas() {
  const canvas = document.getElementById('pidCanvas');
  const pInput = document.getElementById('pidPInput');
  const dInput = document.getElementById('pidDInput');
  if (!canvas || !canvas.getContext || !pInput || !dInput) return;
  const ctx = canvas.getContext('2d');
  if (!ctx) return;
  const w = canvas.width;
  const h = canvas.height;

  const p = parseFloat(pInput.value) || 45;
  const d = parseFloat(dInput.value) || 35;
  const pVal = document.getElementById('pidPVal');
  if (pVal) pVal.textContent = p;
  const dVal = document.getElementById('pidDVal');
  if (dVal) dVal.textContent = d;

  ctx.clearRect(0, 0, w, h);

  // Background Grid
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
  ctx.lineWidth = 1;
  for (let x = 0; x < w; x += 50) {
    ctx.beginPath(); ctx.moveTo(x, 0); ctx.lineTo(x, h); ctx.stroke();
  }
  for (let y = 0; y < h; y += 40) {
    ctx.beginPath(); ctx.moveTo(0, y); ctx.lineTo(w, y); ctx.stroke();
  }

  // Target Setpoint Line (dashed yellow)
  const targetY = h * 0.35;
  ctx.strokeStyle = '#F59E0B';
  ctx.setLineDash([6, 4]);
  ctx.lineWidth = 2;
  ctx.beginPath();
  ctx.moveTo(40, targetY);
  ctx.lineTo(w - 20, targetY);
  ctx.stroke();
  ctx.setLineDash([]);

  // Target Label
  ctx.fillStyle = '#F59E0B';
  ctx.font = '11px JetBrains Mono';
  ctx.fillText('TARGET SETPOINT (Stick Command)', 50, targetY - 8);

  // Simulate 2nd-order dynamic system
  const omega = Math.sqrt(p * 0.8);
  const zeta = (d * 0.12) / (2 * Math.sqrt(p * 0.08) + 0.001);

  ctx.strokeStyle = '#3B82F6';
  ctx.lineWidth = 3;
  ctx.beginPath();
  ctx.moveTo(40, h * 0.85);

  const startX = 40;
  const baselineY = h * 0.85;
  const stepHeight = baselineY - targetY;

  for (let px = 0; px < (w - 60); px++) {
    const t = px * 0.04;
    let resp = 0;
    if (zeta < 1.0) {
      // Underdamped
      const wd = omega * Math.sqrt(1 - zeta * zeta);
      resp = 1 - Math.exp(-zeta * omega * t) * (Math.cos(wd * t) + (zeta / Math.sqrt(1 - zeta * zeta)) * Math.sin(wd * t));
    } else {
      // Overdamped
      resp = 1 - Math.exp(-omega * t * 0.6);
    }
    const curY = baselineY - (resp * stepHeight);
    ctx.lineTo(startX + px, curY);
  }
  ctx.stroke();

  // Status message
  const statusEl = document.getElementById('pidResponseStatus');
  if (statusEl) {
    if (zeta < 0.5) {
      statusEl.innerHTML = '<span style="color:var(--accent-rose)">⚠ Underdamped (Oscillatory): P is too high relative to D. Severe overshoot and ringing will create motor vibration.</span>';
    } else if (zeta > 1.2) {
      statusEl.innerHTML = '<span style="color:var(--accent-amber)">⚠ Overdamped (Sluggish): D is too high. Control feels mushy and motors will run hot.</span>';
    } else {
      statusEl.innerHTML = '<span style="color:var(--accent-emerald)">✓ Critically Damped: Optimal tuning. Instantaneous rise time with negligible overshoot.</span>';
    }
  }
}

// CH12: Flight Checklist
function toggleFlightCheck(el) {
  el.classList.toggle('done');
  const items = document.querySelectorAll('#checklistItems .check-row');
  const done = document.querySelectorAll('#checklistItems .check-row.done').length;
  const total = items.length;

  document.getElementById('flightCheckProgress').style.width = ((done / total) * 100) + '%';
  document.getElementById('flightCheckCount').textContent = `${done} of ${total} items verified`;

  const statusEl = document.getElementById('flightCheckReadyText');
  if (done === total) {
    statusEl.textContent = '🚀 Ready for Takeoff!';
    statusEl.style.color = 'var(--accent-emerald)';
  } else {
    statusEl.textContent = 'Inspection Incomplete';
    statusEl.style.color = 'var(--text-muted)';
  }
}

// Router Event Listeners
function handleHashRoute() {
  const hash = window.location.hash.replace('#', '') || 'home';
  if (hash === 'home') {
    navigate('home');
  } else if (CHAPTERS.find(c => c.id === hash)) {
    navigate(hash);
  } else {
    navigate('home');
  }
}

function handleResize() {
  const isMobile = window.innerWidth < 640;
  document.getElementById('menuBtn').style.display = isMobile ? 'inline-block' : 'none';
}

window.addEventListener('hashchange', handleHashRoute);
window.addEventListener('resize', handleResize);
window.addEventListener('DOMContentLoaded', () => {
  handleResize();
  handleHashRoute();
  updateCourseProgress();
  checkLogin();
});

// Immediate execution fallback
if (document.readyState === 'complete' || document.readyState === 'interactive') {
  handleResize();
  handleHashRoute();
  updateCourseProgress();
  checkLogin();
}
</script>
</body>
</html>
'''

def build_academy():
    print("[*] Generating Club Drone Academy application HTML...")
    html_content = get_full_html()

    for path in OUTPUT_PATHS:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        print(f"[*] Writing to: {path}")
        with open(path, "w", encoding="utf-8") as f:
            f.write(html_content)
        size_kb = os.path.getsize(path) / 1024
        print(f"[✓] Successfully generated {path} ({size_kb:.1f} KB)")

if __name__ == "__main__":
    build_academy()
