#!/usr/bin/python
# SimpleSyslogServer
# Ramesh Natarajan (nram), Solace PSG
# Reference: https://yuks.me/blog/python-syslog-server

__author__ = 'Ramesh Natarajan, Solace PSG'
 
import argparse
#import SocketServer as SS
import socketserver as SS

from threading import Thread
 
PORT = 514
HOST = ""
 
class MySocketServerHandler(SS.BaseRequestHandler):
 
    def handle(self):
        #print  self.request
        #print  self.request[0].strip()
        self.data = self.request.recv(1024).strip()
        print ("--- event received from {0} :\n {}".format(self.client_address[0], self.data))
     
 
def start_udp():
    print("Starting UDP Server at port %s " % PORT)
    server_s = SS.UDPServer((HOST, PORT), MySocketServerHandler)
    server_s.serve_forever()
 
 
def start_tcp():
    print("Starting TCP Server at port %s " % PORT)
    server_s = SS.TCPServer((HOST, PORT), MySocketServerHandler)
    server_s.serve_forever()
 
 
if __name__ == "__main__":
 
    parser = argparse.ArgumentParser(description='Bugtower rsyslog server')
    parser.add_argument('--tcp', help='Start TCP server', action='store_true', default=False, required=False)
    parser.add_argument('--udp', help='Start UDP server', action='store_true', default=True, required=False)
    parser.add_argument('--port', help='Port for servers', default=514, required=False)
    args = parser.parse_args()
 
    PORT = int(args.port)

    if args.udp:
        t = Thread(target=start_udp)
        t.start()
    if args.tcp:
        t2 = Thread(target=start_tcp)
        t2.start()