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
    mpz_inits(prime, prime_product, test_prime, NULL);
    int prime_count = 0, is_prime = 0;

    mpz_set_ui(prime_product, 1);

    for(int i = 0; i < 101; i++)
    {
        mpz_nextprime(prime, prime);
        mpz_mul(prime_product, prime_product, prime);   
        mpz_add_ui(test_prime, prime_product, 1);
        is_prime = mpz_probab_prime_p(test_prime, 50);        

        if(is_prime)
        {
            prime_count++;       
            gmp_printf("%d: %Zd\n", is_prime, test_prime);
        } 
    }
    printf("\nNumber of primes: %d\n", prime_count);

    mpz_clears(prime, prime_product, test_prime, NULL);

    return 0;
}
