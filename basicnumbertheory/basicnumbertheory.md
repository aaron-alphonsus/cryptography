# Basic Number Theory

My cryptomath library has a bunch of number-theoretic algorithms which may be
useful in cryptographic applications.

The first group of algorithms are the gcd algorithms
 - gcd
 - extendedgcd
 - modinverse
The other group are algorithms related to primes
 - is_prime (Miller-Rabin)
 - random_prime
 - factor (Fermat, Pollard rho, Pollard p-1)

## Greatest Common Divisor

### gcd (aka Euclid's algorithm)

the greatest common divisor of two integers a and b, not both zero is the
largest of the set of common divisors of both a and b.

The algorithm for this is a simple recursive function:
```
if b == 0:
        return a
    else:
        return gcd(abs(b), abs(a % b))
```
The abs function was added to correct an error with getting negative gcds.

### Extendedgcd

The extended gcd goes a step further than just calculating the gcd of a and b,
it also returns coefficients for a and b such that they can sum to their gcd.

The way we do this on paper is to do the continuous division and then
'walk back' the chain once we are done. The recurrence relation however provides
a [shorter solution](http://anh.cs.luc.edu/331/notes/xgcd.pdf)

### modInverse

The modular inverse heavily makes use of the extended gcd function, but it
provides the result in a more useful form in some cases. The algorithm is
simple, if the gcd is not one, the modular inverse does not exist. If it does
exist, we return the smallest positive mod inverse

```
    if extendedgcd(a, b)[0] != 1:
        # We always return the smallest positive mod inverse so this is good.
        return -1
    else:
        if extendedgcd(a, b)[1] < 0:  # return the smallest positive mod inverse
            return extendedgcd(a, b)[1] + b
        else:
            return extendedgcd(a, b)[1]
```

## Prime algorithms

### is_prime



###

### factorization

## Extra: Inverse Matrix mod

## References
 - Trappe, Wade, and Lawrence C. Washington. Introduction to Cryptography: with
   Coding Theory. Pearson Prentice Hall, 2006.