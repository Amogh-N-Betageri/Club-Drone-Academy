#!/bin/bash
# Club Drone Academy - Admin & Instructor Dashboard Launcher
APP_DIR="/home/amogh/projects/Club/Drone"
HTML_FILE="$APP_DIR/admin.html"

# If Desktop HTML exists, fallback
if [ -f "/home/amogh/Desktop/DroneAcademyAdmin.html" ]; then
    HTML_FILE="/home/amogh/Desktop/DroneAcademyAdmin.html"
fi

if command -v xdg-open > /dev/null; then
    xdg-open "$HTML_FILE"
elif command -v firefox > /dev/null; then
    firefox "$HTML_FILE"
else
    python3 -m webbrowser "$HTML_FILE"
fi
