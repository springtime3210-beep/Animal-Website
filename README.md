## Local Photo Asset Server
A lightweight Python development server built on top of http.server. It serves standard project files from the root directory while mapping any request starting with /photoes/ to a dedicated external media folder. It also includes path normalisation to prevent directory traversal security risks. [1, 2, 3] 
## Features

* Dual-Root Serving: Serves local website files alongside external image folders simultaneously.
* Security Middleware: Validates paths to block directory traversal attacks (../).
* Image Format Support: Automatically detects and maps MIME types for JPG, JPEG, PNG, GIF, WEBP, and JFIF.
* Zero Dependencies: Runs entirely on Python's built-in standard libraries. [4, 5] 

## Prerequisites

* Python 3.x installed on your system.

## Configuration
Before running the server, update the configuration constants at the top of the script if necessary:

* PHOTOES_DIR: The absolute path to your external image assets (currently configured to D:\DATA\000-IT Training\VSCode\website1\photoes).
* PORT: The network port the server listens on (default is 8000).

## How to Run

   1. Open your terminal or command prompt.
   2. Navigate to the directory containing the script.
   3. Execute the script using Python:

python server.py


   1. The terminal will display: Server running at http://localhost:8000 [6, 7] 

## URL Routing Behaviour

* Standard Requests: http://localhost:8000/index.html → Serves index.html from the script's current working directory.
* External Photo Requests: http://localhost:8000/photoes/vacation.jpg → Serves vacation.jpg directly from your configured PHOTOES_DIR. [8] 

------------------------------
If you would like to expand this setup, let me know if you want to add support for more file extensions, enable CORS headers for cross-origin frontend requests, or make the directory path configurable via command-line arguments.
