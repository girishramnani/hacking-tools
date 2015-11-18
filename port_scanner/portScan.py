__author__ = 'girish'

import argparse
import socket
from socket import *

def conn(tgthost,tgtprt):
    try:
        connectSkt = socket()
        connectSkt.connect((tgthost,tgtprt))
        connectSkt.send(b'heyo man \r\n')
        result = connectSkt.recv(10)
        print("{} /tcp open".format(tgtprt))
        connectSkt.close()
    except:
        pass

def portScan(tgtHost,tgtPorts):
    try:
        tgtIP=gethostbyname(tgtHost)
    except:
        print("achi tarah se likh")
    else:
        setdefaulttimeout(0.2)
        for tgtport in tgtPorts:
            print("Scanning port {}".format(tgtport))
            conn(tgtIP,int(tgtport))

arg =argparse.ArgumentParser("port scanner")
arg.add_argument('--host',help="the host name you want to scan",required=True)
arg.add_argument('--port',help="ports with : for range",required=True)
w = arg.parse_args()
tgtports = w.port.split(":")
portScan(w.host,range(int(tgtports[0]),int(tgtports[1])))






