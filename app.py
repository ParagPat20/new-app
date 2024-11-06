import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import webview

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

def create_window():
    global webview_window
    webview_window = webview.create_window(
        "Standalone HTTP Server Application",
        "http://127.0.0.1:5000/index.html",
        width=1600,
        height=900,
        frameless=True,
        fullscreen=True  # Start in fullscreen mode
    )

    # Start the webview window
    webview.start()

if __name__ == "__main__":
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    create_window()
