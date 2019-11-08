#include <iostream>
#include <cstdio>
using namespace std;

int main() {
    int i;     // "%d"
    long lg;   // "%ld"
    char ch;   // "%c"
    float fl;  // "%f"
    double d;  // "%lf"

    scanf("%d %ld %c %f %lf", &i, &lg, &ch, &fl, &d);
    printf("%d \n%ld \n%c \n%f \n%lf", i, lg, ch, fl, d);

    return 0;
}
