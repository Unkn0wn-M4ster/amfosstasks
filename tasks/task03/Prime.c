#include <stdio.h>
#include <stdbool.h>

bool is6k1(int num) {
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;

    int i = 5;
    while (i * i <= num) {
        if (num % i == 0 || num % (i + 2) == 0) return false;
        i += 6;
    }
    return true;
}

int main() {
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);
    printf("Prime till %d are:\n", n);
    for (int i = 2; i <= n; i++) {
        if (is6k1(i)) printf("%d\n", i);
    }
    return 0;
}
