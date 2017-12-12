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
 
And then there's the extra
 - Inv matrix (mod n)

## gcd (aka Euclid's algorithm)

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

### Example

gcd(24, 60)  
= gcd(60, 24)  
= gcd(24, 12)  
= gcd(12, 0)  
return 12

## Extendedgcd

The extended gcd goes a step further than just calculating the gcd of a and b,
it also returns coefficients for a and b such that they can sum to their gcd.

The way we do this on paper is to do the continuous division and then
'walk back' the chain once we are done. The recurrence relation however provides
a [shorter solution](http://anh.cs.luc.edu/331/notes/xgcd.pdf)
The algorithm is effectively calculating the backwards direction while solving
forward.

### Example

Extendedgcd(19, 16)  
q = 1  
x, prevx = 1 0  
y, prevy = -1 1  
a, b = 16 3  

q = 5  
x, prevx = -5 1  
y, prevy = 6 -1  
a, b = 3 1  

q = 3  
x, prevx = 16 -5  
y, prevy = -19 6  
a, b = 1 0

(1, -5, 6)

## modInverse

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

The example here is exactly the same as extendedgcd, because it's the actual
function that does the work.

## is_prime

The is_prime function was implemented using Miller-Rabin. The algorithm is
probabilistic and gives a false positive of 1/4. While this sounds pretty bad,
we can immediately do way better by bumping up the number of trials we do,
because then the probability becomes (1/4)^r. Even for a value as small as r=9,
the chance of being wrong is about 1 in 3 million. If you increase this r
further it starts to get impossibly unlikely

If you supply Miller with a prime, it will always identify it as a prime. If the
algorithm returns a 0, the number provided to it is definitely not a prime. The
issue is that sometimes it could think a composite is a prime.

The algorithm is as follows (loop for r>1):
Given a number n to test, we represent n-1 as 2^k*m where m is odd.
Now that we have k and m calculate b0 = a^m(mod n).
If b(0) = (+/-) (mod n), return probably prime
Else choose rand a = (1, n-1)
    run a loop from 1 to k-2
        If b = -1 (mod n), return probably prime
        If b = 1 (mod n), return composite
last test: if b(k-1) != -1 (mod n), return composite

### Example

n = 561.  
560 = 16 . 35. k = 4, m = 35  
If a = 2  
    b0 = 2^35 = 263 (mod 561)  
    b1 = b0^2 = 166 (mod 561)  
    b2 = b1^2 =  67 (mod 561)  
    b3 = b^2  =   1 (mod 561)  
b(k-1) != -1 (mod n) therefore return composite

## random_prime

The random prime generator runs a loop picking a random number in the range
given to it, and sends it to is_prime to test. This works well, and I was able
to generate a 1024 bit prime within a couple of seconds with a r value for my
Miller-Rabin being 64

## Fermat Factorization

Fermat's factorization method relies on the fact that a difference of squares
can be factored i.e. <code>x<sup>2</sup>-y<sup>2</sup> = (x-y)(x+y)</code>

So, given a prime p, we calculate p + 1<sup>2</sup>, p + 2<sup>2</sup>,
p + 3<sup>2</sup>, ... and we test this number for being a perfect square. If it
is, we can now represent p as a difference of two squares, and therefore factor
it.

### Example

p = 295927  
The first perfect square we find is 295927 + 3<sup>2</sup>  
= 295936 = 544<sup>2</sup>  
Therefore 295927 = (544-3)(544+3) = 541 . 547

## Pollard-Rho

The Pollard-Rho has 4 initial things to define before the algorithm. Values of 
x, y, d and the definition of function g. Then, the algorithm is as follows:

```
x, y, d = 2, 2, 1
g = lambda a: (a ** 2 + 1) % n
while d == 1:
    x = g(x)
    y = g(g(y))
    d = gcd(abs(x-y), n)
if d == n:
    if not d & 1:
        return int(2), int(n/2)
else:
    return int(d), int(n/d)

```

### Example
n = 517
x, y, d = 5 26 1  
x, y, d = 26 268 11  
(11, 47)

## Pollard p-1

The Pollard p-1 algorithm takes a choice for a bound and calculates b as 
b_prev^j (mod n). This goes on until b(bound) = b (mod n) is reached. At this 
point, d = gcd(b-1, n) and if 1 < d < n, we've found a non trivial factor.
If not, we increment the bound and try again. We can keep doing this if we are 
guaranteed to receive a composite number to factor!

### Example
n = 987  

b1 = 2  
d = 1  

b1 = 3  
b2 = 9  
d = 1

b1 = 4  
b2 = 16  
b3 = 148  
d = 21

(21, 47)

## Extra: Inverse Matrix mod

To be invertible mod n, the gcd of the determinant of the matrix with n has to 
be 1. If this is not the case, we return an empty list

To calculate inv mod n, calculate the adj of the matrix as normal. Now, in the 
usual algorithm, we would have to divide this value by the determinant of the 
matrix. Here, we just calculate the inverse mod of the determinant and multiply
the matrix with that instead. Then we take mod n to get rid of any negative 
values.

### Example
M = [[1, 1, 1,], [1, 2, 3], [1, 4, 9]] (mod 11)  
det(M) = 2  
adj(M) = [[6 -5 1], [-6 8 -2], [2 -3 1]]  
modInverse(2, 11) = 6  
M = [[3, 3, 6,], [8, 4, 10], [1, 4, 6]] (mod 11)

## References
 - Trappe, Wade, and Lawrence C. Washington. Introduction to Cryptography: with
   Coding Theory. Pearson Prentice Hall, 2006.