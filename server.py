import http.server
import os

PHOTOES_DIR = r"D:\DATA\000-IT Training\VSCode\website1\photoes"
PORT = 8000

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # If the request starts with /photoes/, serve from the external photoes directory
        if self.path.startswith('/photoes/'):
            # Get the relative path after /photoes/
            relative_path = self.path[len('/photoes/'):]
            # Construct full path to the external photoes directory
            full_path = os.path.join(PHOTOES_DIR, relative_path)
            # Normalize path to prevent directory traversal attacks
            full_path = os.path.normpath(full_path)
            # Ensure the resolved path is within the photoes directory
            if not full_path.startswith(os.path.normpath(PHOTOES_DIR)):
                self.send_response(403)
                self.end_headers()
                self.wfile.write(b"Forbidden")
                return
            # Check if file exists
            if os.path.isfile(full_path):
                # Determine content type
                ext = os.path.splitext(full_path)[1].lower()
                content_type = {
                    '.jpg': 'image/jpeg',
                    '.jpeg': 'image/jpeg',
                    '.png': 'image/png',
                    '.gif': 'image/gif',
                    '.webp': 'image/webp',
                    '.jfif': 'image/jpeg',
                }.get(ext, 'application/octet-stream')
                with open(full_path, 'rb') as f:
                    data = f.read()
                self.send_response(200)
                self.send_header('Content-Type', content_type)
                self.send_header('Content-Length', str(len(data)))
                self.end_headers()
                self.wfile.write(data)
                return
            else:
                self.send_response(404)
                self.end_headers()
                self.wfile.write(b"File not found")
                return
        # Otherwise, serve files normally from current directory
        return super().do_GET()

if __name__ == '__main__':
    server_address = ('', PORT)
    httpd = http.server.HTTPServer(server_address, CustomHandler)
    print(f"Server running at http://localhost:{PORT}")
    httpd.serve_forever()
