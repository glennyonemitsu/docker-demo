import socketserver


class HelloHandler(socketserver.BaseRequestHandler):

    def handle(self):
        print('New connection')
        self.request.send(b'Hello!\n')


print('Starting server')
server = socketserver.TCPServer(('', 9999), HelloHandler)
server.serve_forever()
