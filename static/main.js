const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1920,  // Initial width, you can leave it as is or omit it since you're maximizing
    height: 1080,  // Initial height, you can leave it as is or omit it since you're maximizing
    fullscreen: false,  // This ensures the window is not in fullscreen mode
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')  // If you're using a preload.js file
    }
  });

  // Maximize the window
  mainWindow.maximize();

  // Load your HTML file into the window
  mainWindow.loadURL('http://127.0.0.1:5000/index.html');

  mainWindow.on('closed', () => {
    mainWindow = null;
  });
}


app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});
