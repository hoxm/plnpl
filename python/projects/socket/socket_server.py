import sys
import traceback  
#import signal
from SocketServer import ThreadingTCPServer, StreamRequestHandler  

#def sig_handler(signo, frame):
#    print "Got signal ", signo
#    sys.exit(0)

class NwkHandler(StreamRequestHandler):
    def handle(self):
        print "Got connection from", self.request.getpeername()
        while True:
            try:
                data = self.rfile.readline().strip()
                if data:
                    print "Receive[%r]: %s" %(self.client_address, data)
                    self.wfile.write(data.upper())
                if data == 'exit':
                    break
            except:
                traceback.print_exc()
                break

#signal.signal(signal.SIGINT, sig_handler)
#signal.signal(signal.SIGTERM, sig_handler)

try:
    server = ThreadingTCPServer(('', 1234), NwkHandler)
    server.serve_forever()
except KeyboardInterrupt:
    sys.exit(0)
