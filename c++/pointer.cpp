#include <stdio.h>


// & address
// * dereferencing 

void update(int *a,int *b) {

    x = a + b;
    y = abs(a - b);

    return a, b;
}

int main() {
    int a, b;
    // pa points to address of val a
    int *pa = &a, *pb = &b;
    // read a, b vals
    scanf("%d %d", &a, &b);
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}

