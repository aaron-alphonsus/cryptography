/*
 * Build: gcc primality-testing.c -o pt.c -lgmp -lm
 * Run: ./pt
 * 
 * Author: Aaron Alphonsus
 */
#include <stdio.h>
#include <gmp.h>

int main(int argc, char *argv[])
{
    mpz_t prime, next;
    mpz_inits (prime, NULL);
    int i = 0;

    mpz_set_ui (prime, 0);

    for(int i; i < 101; i++)
    {
        mpz_nextprime (prime, prime);
        gmp_printf("%Zd\n", prime);  
    }

    return 0;
}
