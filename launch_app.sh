#!/bin/bash
# Club Drone Academy Desktop Launcher
APP_DIR="/home/amogh/projects/Club/Drone"
HTML_FILE="/home/amogh/Desktop/DroneAcademy.html"

# If Desktop HTML doesn't exist, fallback to project index.html
if [ ! -f "$HTML_FILE" ]; then
    HTML_FILE="$APP_DIR/index.html"
fi

if command -v xdg-open > /dev/null; then
    xdg-open "$HTML_FILE"
elif command -v firefox > /dev/null; then
    firefox "$HTML_FILE"
else
    python3 -m webbrowser "$HTML_FILE"
fi
