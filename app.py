import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess
import time

# Define the directory for the static files
web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/shutdown':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Shutting down the server...")
            os._exit(0)

def start_http_server():
    global httpd
    httpd = HTTPServer(("127.0.0.1", 5000), CustomHandler)
    httpd.serve_forever()

def start_electron_app():
    # Wait a few seconds for the HTTP server to be ready
    time.sleep(2)
    
    # Launch Electron app (assuming 'electron' is installed globally)
    electron_process = subprocess.Popen(['electron', 'main.js'])
    
    # Wait until Electron app is closed
    electron_process.communicate()

if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    # Start the Electron app after a slight delay to ensure the server is up
    start_electron_app()
