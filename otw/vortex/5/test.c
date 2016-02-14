#include <stdio.h>
#include <stdlib.h>

int main() {
    unsigned char canary[5];
    unsigned char foo[4];

    memset(foo, "\x00", sizeof (foo));
    /* 0 *before */ strcpy (canary, "AAAA");
    /* Need to calculate the addr of the GOT thing */
    printf("%127u%n%256u%n%256u%n%256u%n",
            1, (int *) &foo[0],
            1, (int *) &foo[1],
            1, (int *) &foo[2],
            1, (int *) &foo[3]);
    /* 5 *after */ 
    printf("%02x%02x%02x%02x\n", foo[0], foo[1], foo[2], foo[3]);
    printf("canary: %02x%02x%02x%02x\n", canary[0], canary[1], canary[2], canary[3]);
}
