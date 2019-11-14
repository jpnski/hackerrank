#include <stdio.h>
#include <stdlib.h>


// & address
// * dereferencing 

void update(int *a, int *b) {
    int x, y;

    x = (*a + *b);
    y = abs(*a - *b);
    
    *a = x;
    *b = y;
}

int main() {
    int a, b;
    // assign pointer pa to memory address of a, b
    int *pa = &a, *pb = &b;
    // read ints a, b
    scanf("%d %d", &a, &b);
    // pointers pa, pb = inputs to update fn
    // fn returns dereferenced pointers modified by fn
    update(pa, pb);
    printf("%d\n%d", a, b);

    return 0;
}
