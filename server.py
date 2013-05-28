import SocketServer

HOST = '127.0.0.1'
PORT = 40020

class ThreadedServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass

class BluntHandler(SocketServer.StreamRequestHandler):
    def handle(self):
        print 'Connected ', self.request.getpeername()
        self.wfile.write('Hello %r' % self.request.getpeername()[1])

server = ThreadedServer((HOST, PORT), BluntHandler)
print 'Server on'
server.serve_forever(.5)
