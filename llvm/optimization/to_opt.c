#include <stdio.h>

void foo() {
    int a = 42;
    int b = 2 * a;
    printf("%d\n", b);
}

int main() {
    foo();
    return 0;
}

