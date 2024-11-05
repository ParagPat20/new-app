# app.py
import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import webview

# Define the directory where HTML and static files are located
web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)  # Set working directory to /static

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/shutdown':
            # Shutdown WebView and HTTP server
            if webview_window:
                webview_window.destroy()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Exiting Processes")
            os._exit(0)  # Terminate the entire Python process

# Start HTTP server in a separate thread
def start_http_server():
    global httpd
    httpd = HTTPServer(("127.0.0.1", 5000), CustomHandler)
    httpd.serve_forever()

# Function to stop the server
def stop_server():
    if httpd:
        httpd.shutdown()

# Function to create a web view window
def create_window():
    global webview_window
    webview_window = webview.create_window(
        "Standalone HTTP Server Application",
        "http://127.0.0.1:5000/index.html",  # Point directly to index.html in /static
        width=1600,
        height=900,
        frameless=True
    )
    webview.start()

if __name__ == "__main__":
    # Start HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    # Create and run the web view window
    create_window()
