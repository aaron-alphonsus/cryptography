/*
 * Build: gcc primality-testing.c -o pt -lgmp -lm
 * Run: ./pt
 * 
 * Author: Aaron Alphonsus
 */
#include <stdio.h>
#include <gmp.h>

int main(int argc, char *argv[])
{
    mpz_t prime, prime_product, test_prime;
    //mpz_t prime_array[101];
    mpz_inits(prime, prime_product, test_prime, NULL);
    int is_prime = 0;

    //for(int i; i < 101; i++)
        //mpz_init(prime_array[i]);

    //for(int i; i < 101; i++)
        //mpz_set_ui(prime_array[i], i+1);

    mpz_set_ui(prime_product, 1);

    for(int i = 0; i < 101; i++)
    {
        mpz_nextprime(prime, prime);
        mpz_mul(prime_product, prime_product, prime);   
        mpz_add_ui(test_prime, prime_product, 1);
        is_prime = mpz_probab_prime_p(test_prime, 50);        

        //printf("%d: ", is_prime);
        gmp_printf("%d: %Zd\n", is_prime, test_prime); 
    }

    mpz_clears(prime, prime_product, test_prime, NULL);
    //for(int i; i < 101; i++)
        //mpz_clear(prime_array[i]);

    return 0;
}
