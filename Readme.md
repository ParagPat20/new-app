# Standalone HTTP Server Application

This project is a simple standalone HTTP server application that serves static files and provides a GUI using the `pywebview` library. It runs a local HTTP server and displays a web interface, allowing interaction with the server through a browser-like window.

## Features

- Serves static HTML files from a specified directory.
- GUI created using `pywebview`  for a seamless user experience.
- Supports shutting down the server through a POST request.
- Runs in a separate thread to keep the GUI responsive.

## Requirements

- Python 3.x
- `pywebview` 
You can install the required library using pip:

```
pip install pywebview
```
Project Structure
```
.
├── static
│   └── index.html  
│   └── styles.css
│   └── script.js
└── app.py       # Main server script
```
Usage
Clone the repository:

```
git clone https://github.com/ParagPat20/new-app.git
cd new-app
```
Install the required libraries:

```
pip install -r requirements.txt
```
Place your HTML files in the static directory.

`Run the server:`

```
python app.py
```
The application will open a window displaying the contents of index.html.

