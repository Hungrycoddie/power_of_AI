import socket
import time

class PLC_TCP:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.ip, self.port))
        self.sock.settimeout(1)
        self.sock.send(b'\x01\x03\x00\x00\x00\x01\x84\x00')
        self.sock.recv(1024)
