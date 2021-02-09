#include <stdio.h>

void evenFib() {
    int stored1 = 1;
    int stored2 = 2;
    int fibNumber = 0;
    int evenSum = 2; //Since we already have 2
    int i;
    for (i=0; fibNumber<=4000000; i++) {
        fibNumber = stored1+stored2;
        stored1 = stored2;
        stored2 = fibNumber;
        if (fibNumber%2==0) {
            evenSum += fibNumber;
        }
    }
    printf("%i\n", evenSum);
}

void main() {
    evenFib();
}