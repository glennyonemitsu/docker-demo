import signal
import sys
if sys.version_info[0] == 2:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
else:
    from http.server import HTTPServer, BaseHTTPRequestHandler


signal.signal(signal.SIGINT, lambda x, y: sys.exit(0))


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.end_headers()
        self.wfile.write(b'Hello, World!')


server = HTTPServer(('', 9999), HelloWorldHandler)
server.serve_forever()
