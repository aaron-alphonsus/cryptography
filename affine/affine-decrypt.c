#include <stdio.h>

int main()
{
    char a[29] = "edsgickxhuklzveqzvkxwkzukcvuh";

    //printf("%s\n", a);
    for(int i=0; i < 29; i++)
        printf("%c", ((3*(a[i]-97)+22)%26)+97);
    printf("\n");

    return 0;
}
