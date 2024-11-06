import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import webview
import tkinter as tk

web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/shutdown':
            if webview_window:
                webview_window.destroy()
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Exiting Processes")
            os._exit(0)

def start_http_server():
    global httpd
    httpd = HTTPServer(("127.0.0.1", 5000), CustomHandler)
    httpd.serve_forever()

def stop_server():
    if httpd:
        httpd.shutdown()

def get_screen_size():
    # Use tkinter to get screen dimensions
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

def create_window():
    global webview_window

    # Get the screen resolution
    screen_width, screen_height = get_screen_size()

    # Create a bordered window that simulates maximization
    webview_window = webview.create_window(
        "Standalone HTTP Server Application",
        "http://127.0.0.1:5000/index.html",
        width=screen_width,
        height=screen_height,
        frameless=False  # Border is enabled for better rendering
    )

    # Start the webview window
    webview.start()

if __name__ == "__main__":
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    create_window()
