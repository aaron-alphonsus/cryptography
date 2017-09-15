#include <stdio.h>

int main()
{
    char a[6] = "affine";
    int alpha = 0, beta = 2;


    //printf("%s\n", a);
    for(int i=0; i<55; i++)
    {
        alpha += 1;
        printf("----alpha = %d----\n", alpha);
        for(int i=0; i < 6; i++)
            printf("%c", ((alpha*(a[i]-97)+beta)%26)+97);
        printf("\n");
    }

    return 0;
}
