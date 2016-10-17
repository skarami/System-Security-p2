#!/usr/bin/env python

from struct import pack
import socket
import sys
import time

from console import console

if len(sys.argv) != 3:
    sys.exit("Usage: %s PORT LISTEN_PORT" % sys.argv[0])

def send_cmd(cmd):
    port = int(sys.argv[1])
    sock = socket.create_connection(('127.0.0.1', port),
                                    socket.getdefaulttimeout(),
                                    ('127.0.0.1', 0))

    sock.sendall(cmd)

    while True:
        buf = sock.recv(1024)
        if not buf:
            break
        sys.stdout.write(buf)
    sock.close()

send_cmd("PUT SECRET p455w0rd! Secret value\r\n")
send_cmd("GET SECRET password1\r\n")
send_cmd("GET SECRET p455w0rd!\r\n")

# :vim set sw=4 ts=8 sts=8 expandtab:
