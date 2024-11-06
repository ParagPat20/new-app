import os
import sys
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile
from PyQt5.QtCore import QUrl

# Set up the web directory
web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

# Define global variable for the webview window
webview_window = None

# HTTP Server Class
class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/shutdown':
            global webview_window
            if webview_window:
                webview_window.close()  # Close the webview window
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Exiting Processes")
            os._exit(0)

# Start HTTP server in a separate thread
def start_http_server():
    global httpd
    httpd = HTTPServer(("127.0.0.1", 5000), CustomHandler)
    httpd.serve_forever()

# PyQt Window Class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        global webview_window
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://127.0.0.1:5000/index.html"))
        self.setCentralWidget(self.browser)
        self.setWindowTitle("Webview Window")
        self.showMaximized()  # Maximize the window on startup
        webview_window = self  # Assign the current window to the global variable

# Create and display the main window
def create_window():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    # Create and display the PyQt window
    create_window()
