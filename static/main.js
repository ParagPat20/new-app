const { app, BrowserWindow } = require('electron');
const path = require('path');

let mainWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1920,  // You can leave the width and height properties if you want to control the size too
    height: 1080,
    fullscreen: false,  // This makes the window fullscreen
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')  // If you're using a preload.js file
    }
  });

  // Load your HTML file into the window
  mainWindow.loadURL('http://127.0.0.1:5000/index.html');

  // Open the DevTools (optional)
  // mainWindow.webContents.openDevTools();

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
