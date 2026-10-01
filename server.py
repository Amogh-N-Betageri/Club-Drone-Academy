#!/usr/bin/env python3
"""
Club Drone Academy - Backend API & Static Server
Provides SQLite database persistence for student logins, progress tracking,
lesson completion, and Q&A exam scores, plus serves the web apps.
"""

import http.server
import socketserver
import json
import sqlite3
import os
import urllib.parse
from datetime import datetime

PORT = 5000
DB_FILE = "/home/amogh/projects/Club/Drone/drone_academy.db"
STATIC_DIR = "/home/amogh/projects/Club/Drone"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            last_active TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            overall_progress INTEGER DEFAULT 0,
            completed_chapters TEXT DEFAULT '[]',
            qna_scores TEXT DEFAULT '{}'
        )
    ''')
    conn.commit()
    conn.close()
    print(f"[✓] SQLite database initialized at: {DB_FILE}")

class DroneAcademyHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=STATIC_DIR, **kwargs)

    def _send_cors_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')

    def do_OPTIONS(self):
        self.send_response(200)
        self._send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == '/api/students':
            self.handle_get_students()
        elif parsed.path == '/api/stats':
            self.handle_get_stats()
        elif parsed.path == '/api/student':
            query = urllib.parse.parse_qs(parsed.query)
            email = query.get('email', [''])[0]
            self.handle_get_student_by_email(email)
        else:
            # Fallback to serving static files (index.html, admin.html, etc.)
            super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        content_len = int(self.headers.get('Content-Length', 0))
        post_body = self.rfile.read(content_len).decode('utf-8')
        
        try:
            data = json.loads(post_body) if post_body else {}
        except json.JSONDecodeError:
            data = {}

        if parsed.path == '/api/login':
            self.handle_login(data)
        elif parsed.path == '/api/progress':
            self.handle_update_progress(data)
        elif parsed.path == '/api/reset':
            self.handle_reset_student(data)
        else:
            self.send_response(404)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Endpoint not found'}).encode('utf-8'))

    def handle_login(self, data):
        name = data.get('name', '').strip()
        email = data.get('email', '').strip().lower()

        if not name or not email:
            self.send_response(400)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Name and Email are required'}).encode('utf-8'))
            return

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, email, created_at, last_active, overall_progress, completed_chapters, qna_scores FROM students WHERE email = ?', (email,))
        row = cursor.fetchone()

        now = datetime.now().isoformat()

        if row:
            # Existing student
            cursor.execute('UPDATE students SET name = ?, last_active = ? WHERE email = ?', (name, now, email))
            conn.commit()
            student = {
                'id': row[0],
                'name': name,
                'email': row[2],
                'created_at': row[3],
                'last_active': now,
                'overall_progress': row[5],
                'completed_chapters': json.loads(row[6]),
                'qna_scores': json.loads(row[7])
            }
        else:
            # New student registration
            cursor.execute('''
                INSERT INTO students (name, email, created_at, last_active, overall_progress, completed_chapters, qna_scores)
                VALUES (?, ?, ?, ?, 0, '[]', '{}')
            ''', (name, email, now, now))
            conn.commit()
            student_id = cursor.lastrowid
            student = {
                'id': student_id,
                'name': name,
                'email': email,
                'created_at': now,
                'last_active': now,
                'overall_progress': 0,
                'completed_chapters': [],
                'qna_scores': {}
            }

        conn.close()

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'student': student}).encode('utf-8'))

    def handle_update_progress(self, data):
        email = data.get('email', '').strip().lower()
        if not email:
            self.send_response(400)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Email required'}).encode('utf-8'))
            return

        completed_chapters = data.get('completed_chapters', [])
        qna_scores = data.get('qna_scores', {})
        overall_progress = data.get('overall_progress', 0)
        now = datetime.now().isoformat()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students 
            SET completed_chapters = ?, qna_scores = ?, overall_progress = ?, last_active = ?
            WHERE email = ?
        ''', (json.dumps(completed_chapters), json.dumps(qna_scores), overall_progress, now, email))
        conn.commit()
        conn.close()

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True, 'updated_at': now}).encode('utf-8'))

    def handle_get_students(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, email, created_at, last_active, overall_progress, completed_chapters, qna_scores FROM students ORDER BY last_active DESC')
        rows = cursor.fetchall()
        conn.close()

        students = []
        for r in rows:
            students.append({
                'id': r[0],
                'name': r[1],
                'email': r[2],
                'created_at': r[3],
                'last_active': r[4],
                'overall_progress': r[5],
                'completed_chapters': json.loads(r[6]),
                'qna_scores': json.loads(r[7])
            })

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'students': students}).encode('utf-8'))

    def handle_get_stats(self):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*), AVG(overall_progress) FROM students')
        row = cursor.fetchone()
        count = row[0] or 0
        avg_progress = round(row[1] or 0, 1)

        cursor.execute('SELECT completed_chapters FROM students')
        all_completed = cursor.fetchall()
        total_lessons_done = 0
        for r in all_completed:
            try:
                ch_list = json.loads(r[0])
                total_lessons_done += len(ch_list)
            except:
                pass

        conn.close()

        stats = {
            'total_students': count,
            'avg_progress': avg_progress,
            'total_lessons_completed': total_lessons_done
        }

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(stats).encode('utf-8'))

    def handle_reset_student(self, data):
        email = data.get('email', '').strip().lower()
        if not email:
            self.send_response(400)
            self._send_cors_headers()
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'error': 'Email required'}).encode('utf-8'))
            return

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE students 
            SET completed_chapters = '[]', qna_scores = '{}', overall_progress = 0, last_active = ?
            WHERE email = ?
        ''', (datetime.now().isoformat(), email))
        conn.commit()
        conn.close()

        self.send_response(200)
        self._send_cors_headers()
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True

def run_server():
    init_db()
    with ReusableTCPServer(("", PORT), DroneAcademyHandler) as httpd:
        print(f"[🚀] Club Drone Academy server running at: http://localhost:{PORT}")
        print(f"[📖] Student App: http://localhost:{PORT}/index.html")
        print(f"[📊] Admin Dashboard: http://localhost:{PORT}/admin.html")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[!] Server shutting down.")
            httpd.server_close()

if __name__ == '__main__':
    run_server()
