const { app, BrowserWindow } = require('electron');
const path = require('path');
const { exec } = require('child_process');  // Required for executing shell scripts

let mainWindow;
let keyboardWindow;

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 800,  // You can leave the width and height properties if you want to control the size too
    height: 600,
    fullscreen: true,  // This makes the window fullscreen
    webPreferences: {
      nodeIntegration: true,
      preload: path.join(__dirname, 'preload.js')  // If you're using a preload.js file
    }
  });

  // Load your HTML file into the window
  mainWindow.loadURL('http://127.0.0.1:5000/index.html');

  mainWindow.on('closed', () => {
    mainWindow = null;
    if (keyboardWindow) {
      keyboardWindow.close();  // Close the keyboard window when the main window is closed
    }
  });

  // Execute keyboardstart.sh to launch the keyboard window
  executeShellScript('keyboardstart.sh');

  // Create the keyboard window after the main window is created
  createKeyboardWindow();
}

function createKeyboardWindow() {
  keyboardWindow = new BrowserWindow({
    width: 800,
    height: 200,  // Adjust the height as needed
    alwaysOnTop: true,  // Keeps the keyboard on top of the main window
    frame: false,       // Optional: removes the window frame for a floating effect
    transparent: true,  // Optional: Makes the window background transparent
    x: 0,               // Position the keyboard window
    y: 0
  });

  // Load your keyboard HTML or JS here
  keyboardWindow.loadFile('keyboard.html');  // Assuming your keyboard is in a file named 'keyboard.html'

  keyboardWindow.on('closed', () => {
    keyboardWindow = null;
  });
}

function executeShellScript(scriptName) {
  // Executes the shell script using the child_process module
  exec(`sh ${path.join(__dirname, scriptName)}`, (error, stdout, stderr) => {
    if (error) {
      console.error(`exec error: ${error}`);
      return;
    }
    console.log(`stdout: ${stdout}`);
    console.error(`stderr: ${stderr}`);
  });
}

app.whenReady().then(() => {
  createWindow();

  // Optionally, you can handle other events such as focus-in and focus-out
  app.on('focus', () => {
    executeShellScript('keyboardstart.sh');  // Execute the keyboardstart.sh script when app gains focus
  });

  app.on('blur', () => {
    executeShellScript('keyboardstop.sh');  // Execute the keyboardstop.sh script when app loses focus
  });
});

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
