"""
Once an open port is found write to the PLCs
"""

import socket
import sys
import time
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.10', 502)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Send data
# message = 'This is the message.  It will be repeated.'
# print >>sys.stderr, 'sending "%s"' % message
# sock.sendall(message)

# Look for the response
# amount_received = 0
# amount_expected = len(message)

# while amount_received < amount_expected:
#     data = sock.recv(16)
#     amount_received += len(data)
#     print >>sys.stderr, 'received "%s"' % data

import socket
import sys
import time
import struct

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.1.10', 502)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

# Send data
# The number of registers to read
message = struct.pack('>HH', 0, 1)

# The starting address to read from
message += struct.pack('>HH', 0, 0)

# The number of registers to write
message += struct.pack('>HH', 0, 1)

# The starting address to write to
message += struct.pack('>HH', 0, 0)

# The value to write
message += struct.pack('>HH', 0, 1)

print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print >>sys.stderr, 'received "%s"' % data

# Send data
# The number of registers to read
message = struct.pack('>HH', 0, 1)

# The starting address to read from
message += struct.pack('>HH', 0, 0)

# The number of registers to write
message += struct.pack('>HH', 0, 1)

# The starting address to write to
message += struct.pack('>HH', 0, 0)

# The value to write
message += struct.pack('>HH', 0, 0)

print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print >>sys.stderr, 'received "%s"' % data

# Send data
# The number of registers to read
message = struct.pack('>HH', 0, 1)

# The starting address to read from
message += struct.pack('>HH', 0, 0)

# The number of registers to write
message += struct.pack('>HH', 0, 1)

# The starting address to write to
message += struct.pack('>HH', 0, 0)

# The value to write
message += struct.pack('>HH', 0, 1)

print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)

# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print >>sys.stderr, 'received "%s"' % data

# Send data
# The number of registers to read
message = struct.pack('>HH', 0, 1)

# The starting address to read from
message += struct.pack('>HH', 0, 0)

# The number of registers to write
message += struct.pack('>HH', 0, 1)

# The starting address to write to
message += struct.pack('>HH', 0, 0)

# The value to write
message += struct.pack('>HH', 0, 0)

print >>sys.stderr, 'sending "%s"' % message
sock.sendall(message)


# Look for the response
amount_received = 0
amount_expected = len(message)

while amount_received < amount_expected:
    data = sock.recv(16)
    amount_received += len(data)
    print >>sys.stderr, 'received "%s"' % data