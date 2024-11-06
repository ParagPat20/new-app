import os
import threading
from http.server import SimpleHTTPRequestHandler, HTTPServer
import subprocess
import time
import platform

# Define the directory for the static files
web_dir = os.path.join(os.path.dirname(__file__), 'static')
os.chdir(web_dir)

class CustomHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        # Handling focus-in and focus-out events
        if self.path == '/focus-in':
            self.execute_shell_script('keyboardstart.sh')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Focus-in event received, running keyboardstart.sh")
        elif self.path == '/focus-out':
            self.execute_shell_script('keyboardstop.sh')
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Focus-out event received, running keyboardstop.sh")
        elif self.path == '/shutdown':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Server shutting down...")
            print("Shutting down the server...")
            httpd.shutdown()  # Graceful shutdown of the server
            os._exit(0)
        else:
            self.send_response(404)
            self.end_headers()

    def execute_shell_script(self, script_name):
        # Ensure the script is executable
        script_path = os.path.join(os.path.dirname(__file__), script_name)
        if platform.system() == "Windows":
            # On Windows, use subprocess to execute batch script or shell commands
            subprocess.Popen(['cmd', '/c', script_path])
        elif platform.system() == "Linux":
            # On Linux, execute the shell script
            subprocess.Popen(['sh', script_path])
        else:
            print(f"Unsupported operating system for script execution.")

def start_http_server():
    global httpd
    httpd = HTTPServer(("127.0.0.1", 5000), CustomHandler)
    print("HTTP server running on http://127.0.0.1:5000")
    httpd.serve_forever()

def start_electron_app():
    # Wait a few seconds for the HTTP server to be ready
    time.sleep(1)

    # Check the operating system
    if platform.system() == "Windows":
        # For Windows, use the full path to the Electron executable
        electron_executable = r'C:\Users\LOQ\AppData\Roaming\npm\node_modules\electron\dist\electron.exe'
    elif platform.system() == "Linux":
        # For Linux, use just 'electron' (assuming it's installed globally)
        electron_executable = 'electron'
    else:
        raise EnvironmentError("Unsupported operating system")

    # Launch Electron app with the disable-gpu flag and other relevant flags
    electron_process = subprocess.Popen([electron_executable, '--disable-gpu', '--no-sandbox', '--use-gl=swiftshader', 'main.js'])

    # Wait until Electron app is closed
    electron_process.communicate()

if __name__ == "__main__":
    # Start the HTTP server in a separate thread
    http_thread = threading.Thread(target=start_http_server)
    http_thread.start()

    # Start the Electron app after a slight delay to ensure the server is up
    start_electron_app()
