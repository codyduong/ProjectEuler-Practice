#include <stdio.h>

void findMultiples(int max) {
    int count = 0;
    int i;
    for (i=0; i<max; i+=3) {
        if (!(i%5 == 0)) {
            count+=i;
        }
    }
    i = 0;
    for (i=0; i<max; i+=5) {
        count+=i;
    }
    printf("%i\n", count);
}

void main() {
    int input = 1000;
    findMultiples(input);
}
