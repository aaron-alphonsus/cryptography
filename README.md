# Cryptography Portfolio
A collection of programs developed in CSC 412 - Cryptography, Fall 2017

### Introduction

The motivation behind this project is twofold - to introduce the reader to
implementations of various algorithms in cryptography and to learn these
algorithms through implementation. Some were created while learning the
algorithms for the first time, so their implementation will be naive in a
lot of places. However, it is hoped that what they lack in rigor, they make up
for in being easy to understand and follow (Although I will concede that the
differential cryptanalysis is really painful to go through)

There were a lot of things enjoyable about this project. Of course there were a
few hair-pulling moments for the more verbose algorithms, but all's well that
ends well, and once I had them done, it was cool to look back at them.
My favorite part has to be the random prime generation. To be able to code up an
algorithm to produce a prime large enough for rsa was pretty neat.

This project has the following sections:
 - Classical Cryptosystems
 - Basic Number Theory
 - Data Encryption Standard
 - RSA

In creating this project, I thought about my target audience and how I wanted to
present this. I decided on designing my project to be hosted on an online
repository.
For one, it's the way I have come across a lot of helpful code in the past. It
is also a great way to receive feedback and continue to develop your code.
Another reason is that these functions are probably only going to be of interest
to other programmers curious about cryptography. Keeping these things in mind, I
have striven to document my code well, both with docstrings and examples and
with markdown pages introducing the algorithms at a higher level.

In describing the algorithms, I borrow heavily from our textbook "Introduction
to Cryptography: with Coding Theory". I do this to maintain as much accuracy as
possible.

### Design

I picked Python 2.7 for the implementation of this project mainly because it's
easy to use when you're working with large numbers. It has a lot of string
manipulation tools that are also very nice.

Being taught in c++ makes it a little awkward to get out of the mindset of
interactive console programming. With this project, it made a lot more sense to
create a collection of modules. This was especially handy with the cryptomath
module which I was able to import easily whenever I needed it.

### Project Structure
 - Classical Cryptosystems - Elementary cryptosystems to learn basic ideas in
 cryptography
    - Viginère
       - cipher - A variation of the shift cipher
       - attack - An attack on the cipher to find the key
       - helper - A text frequency calculator to help with the attack
    - Affine
       - cipher - A generalized and slightly strengthened shift cipher
    - Block cipher - A simple implementation of a block cipher. Useful to learn
    as a lot of modern cryptosystems are block ciphers
 - Basic Number Theory - Number theoretic algorithms useful in cryptography
    - inverse matrix mod n - Inverts a matrix when we have mod n
    - cryptomath - I placed almost all the functions in this section in this
    module which made it easy to import functions that I needed in other parts.
       - gcd - Greatest common divisor of two numbers
       - extended gcd - Calculates the gcd as well as the coefficients of
       Bézout's identity.
       - modular inverse - Division mod n is done by calculating the modular
       inverse of the number.
       - is_prime - Uses Miller-Rabin's primality test
       - random_prime - Generates a random prime within a given range using
       Miller-Rabin's primality test at its core.
       - factor - 3 different factorization algorithms (Fermat's, Pollard rho
       and Pollard p-1)
 - Data Encryption Standard - Learning about more recent cryptographical systems
    - Simplified DES - Eases you into the kind of algorithm that DES is
    - Differential Cryptanalysis - How to break the DES cipher with a chosen
    plaintext attack
    - Full DES - The full DES algorithm in all its glory
 - RSA - The famous RSA public-key cryptosystem. Great tool to get you to think
 about primes and factorization.
    - RSA - A simple version of how RSA works with its private and public keys
    - Shank's factorization - A variation on Fermat's factorization method
    - Sieve of Sundaram - A sieve to generate all primes less than a given n
    value

### Libraries Used
I tried to minimize the external dependencies for this project and the only one
I made use of (I believe) is numpy.

There are some cool things I would like to implement with 3rd party libraries,
but I would first like to learn how to package the entire project and its
dependencies. I took a few stabs at it while working on this project, but I
didn't get too far.

### Next Steps:
As with any project, there's usually something you think of that ends up out of
the scope due to constraints. This section is so that I can keep track of things
on my wishlist to try out next to keep growing this project.
  - Packaging with dependencies
  - Flag for verbose/test output
  - Additions within modules for better output
    (e.g. english dictionary implementation in ciphertext only affine attack)
  - Implement the AES