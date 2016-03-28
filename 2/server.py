import os
import sys
if sys.version_info[0] == 2:
    from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
else:
    from http.server import HTTPServer, BaseHTTPRequestHandler


port = int(os.environ.get('SERVER_PORT'))


class HelloWorldHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, 'OK')
        self.end_headers()
        self.wfile.write(b'Hello, World, from port {}'.format(port))


server = HTTPServer(('', port), HelloWorldHandler)
server.serve_forever()
