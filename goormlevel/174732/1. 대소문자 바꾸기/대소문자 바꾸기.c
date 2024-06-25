#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    int len;
    scanf("%d", &len);
    char input[len + 1];
    scanf("%s", input);

    for (int i = 0; i < len; i++) {
        if (isupper(input[i])) {
            input[i] = tolower(input[i]);
        } else if (islower(input[i])) {
            input[i] = toupper(input[i]);
        }
    }

    printf("%s\n", input);

    return 0;
}
