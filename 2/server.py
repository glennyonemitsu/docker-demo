from __future__ import print_function
import os
import sys
if sys.version_info[0] == 2:
    from SocketServer import BaseRequestHandler, TCPServer
else:
    from socketserver import BaseRequestHandler, TCPServer


class HelloHandler(BaseRequestHandler):

    def handle(self):
        self.request.send(b'Hello!\n')


port = int(os.environ.get('SERVER_PORT'))
server = TCPServer(('', port), HelloHandler)
server.serve_forever()
