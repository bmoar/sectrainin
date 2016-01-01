#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char buf[16];
    read(0, buf, 1024);
    return 0;
}
