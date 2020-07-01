#include <stdio.h>

int main (void) {

    int aList[5] = {5, 4, 3, 2, 1};
    int tmp;
    int minIdx;

    for (int i=0; i < 5; i++) {

        for (int j=i; j < 5; j++) {            

            if (aList[j] <= aList[i]) { // from smallest to largest: <= from largest to smallest: >=
                minIdx = j;
            }
        }

        if (i != minIdx) {
            tmp = aList[i];
            aList[i] = aList[minIdx];
            aList[minIdx] = tmp;
        }
    }

    for (int k=0; k < 5; k++) {
        printf("%d\n", aList[k]);
    }


    return 0;
}