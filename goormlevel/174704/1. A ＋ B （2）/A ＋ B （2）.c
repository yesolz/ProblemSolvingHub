#include <stdio.h>

int main() {
    double num1, num2;
    scanf("%lf %lf", &num1, &num2);
    double sum = num1 + num2;
    printf("%.6lf\n", sum);

    return 0;
}
