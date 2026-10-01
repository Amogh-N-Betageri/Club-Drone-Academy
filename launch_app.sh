#!/bin/bash
# Club Drone Academy - Student Application Launcher
APP_DIR="/home/amogh/projects/Club/Drone"
HTML_FILE="/home/amogh/Desktop/DroneAcademy.html"

# If Desktop HTML doesn't exist, fallback
if [ ! -f "$HTML_FILE" ]; then
    HTML_FILE="$APP_DIR/index.html"
fi

# Ensure SQLite API backend server is running on port 5000
if ! ss -tuln | grep -q ":5000 "; then
    cd "$APP_DIR" && nohup python3 "$APP_DIR/server.py" > "$APP_DIR/server.log" 2>&1 & disown
    sleep 0.8
fi

TARGET_URL="http://localhost:5000/index.html"
if ! curl -s --head --request GET http://localhost:5000 > /dev/null 2>&1; then
    TARGET_URL="$HTML_FILE"
fi

if command -v xdg-open > /dev/null; then
    xdg-open "$TARGET_URL"
elif command -v firefox > /dev/null; then
    firefox "$TARGET_URL"
else
    python3 -m webbrowser "$TARGET_URL"
fi
