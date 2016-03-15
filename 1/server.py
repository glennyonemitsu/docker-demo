import os
import sys

if sys.version_info[0] == 2:
    from __future__ import print_function
    from SocketServer import BaseRequestHandler, TCPServer
else:
    from socketserver import BaseRequestHandler, TCPServer


class HelloHandler(BaseRequestHandler):

    def handle(self):
        print('New connection')
        self.request.send(b'Hello!\n')


print('Starting server')
server = TCPServer(('', 9999), HelloHandler)
server.serve_forever()
