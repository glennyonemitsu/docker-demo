import socketserver
import os


class HelloHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('New connection')
        self.request.send(b'Hello!\n')


port = int(os.environ.get('SERVER_PORT'))
print('Starting server on port', port)
server = socketserver.TCPServer(('', port), HelloHandler)
server.serve_forever()
