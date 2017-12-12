# Classical Cryptosystems

Studying classical cryptosystems gives you an idea for basic concepts in
cryptography and are a nice way to get your feet wet in the subject. Most of
these cryptosystems have been rendered extremely weak with the dawn of computers.

For most of these cryptosystems, the letters of the alphabet are assigned
numbers starting with a = 0, b = 1, ..., z = 25

## Affine Cipher

The affine cipher is a slightly generalized and strengthened shift cipher. The
key for the affine cipher is two integers A and B and the function is called an
affine function. A necessary condition is gcd(A, 26) = 1.

` C -> Ax + B (mod 26) `

Here we are considering our alphabet to be our regular alphabet which is why we
have mod 26. The number of alphabets can be modified, however.

### Example

Let A = 9, B = 2
Affine function: x -> 9x + 2

Plaintext letter: h( = 7)
Encryption: 9 . 7 + 2 = 65 (mod 26) = 13
Ciphertext letter: n

Using the same function you would obtain: affine -> cvvwpm

In order to decrypt, you need to calculate the decryption function using the
modular inverse.
Decryption function: x -> 3(x-2) = 3y - 6 (mod 26) = 3y + 20 (mod 26)

Ciphertext letter: v( = 21)
Decryption: 3 . 21 + 20 = 83 (mod 26) = 5
Plaintext letter: f

Using the decryption function: cvvwpm -> affine

## Affine Attack

If you know two letters of the plaintext and the corresponding ciphertext, it
 suffices to find the key (as long as the gcd = 1)
The method to do this is to create a system of linear equations in A and B and
solve for A and B

### Example

Plaintext = if, Corresponding Ciphertext = pq
i.e. 8 maps to 15 and 5 maps to 16

Therefore we have the equations: 8A + B = 15 and 5A + B = 16 (mod 26)
Subtracting yields: 3A = -1 (mod 26) = 25.
Therefore A = 17. Using this we can solve for B and find B = 9


## Viginère Cipher

The Viginère cipher is a variation of the shift cipher. It was thought to be
secure in the twentieth century however, there were attacks shown as early as
the nineteenth century by Babbage and Kasiski. Friedman developed more methods
for breaking the Viginère Cipher and related ciphers in the 1920s.

### Cryptosystem
**Key**  
A vector of chosen key length whose entries are integers from 0 to 25.  
**Encryption Method**  
The encryption is done by shifting each letter of the plaintext by the each 
integer in the key. Once we get to the end of the key, we wrap around to the 
first number.  
**Decryption**  
Decryption is similar to encryption except we do a backwards shift.

### Example
**Key**  
(21, 4, 2, 19, 14, 17) - Corresponds to the word '_vector_'.

**Encryption**

|  (plaintext) |  h  |  e  |  r  |  e  |  i  |  s  |  h  |  o  |  w  |  i  |  t  |  w  |  o  |  r  |  k  |  s  |
|    :----:    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|     (key)    | 21  |  4  |  2  | 19  | 14  | 17  | 21  |  4  |  2  | 19  | 14  | 17  | 21  |  4  |  2  | 19  |
| (ciphertext) |  c  |  i  |  t  |  x  |  w  |  j  |  c  |  s  |  y  |  b  |  h  |  n  |  j  |  v  |  m  |  l  |

## Viginère Attack

The Viginère attack is done in 2 stages. First the key length is found by taking
displacements of the ciphertext and calculating the number of coincidences. The
displacement with the highest coinccidence is our best guess for the length of
the key.

Once we find the key length (n) we do the following
for i = 1 to n:
1. compute frequencies of letters in positions i mod n and form vector W
2. for j = 1 to 25, compute W . A<sub>j</sub>
3. Let k<sub>i</sub> = j<sub>0</sub> give the max value of W . A<sub>j</sub>
Then, the key is probably {k<sub>1</sub>, ..., k<sub>n</sub>}

## Block Cipher

In order to encrypt using a block cipher, you first pick an integer n which
indicates the size of your matrix (n x n). Your matrix M is your key.
Next, convert the message into a vector of numbers for each character. You have
 to make sure you group your plaintext into groups of size n vectors. Pad the
 plaintext with x, if necessary.

### Example

M = [[1, 2, 3], [4, 5, 6],[11, 9, 8]]  
Plaintext = "abc" -> Vector = (0, 1, 2)  
'Cipher vector' = (0, 23, 22) (mod 26) -> Ciphertext = 'axw'

The decryption here is the same algorithm, except the key is now the inverse
(mod 26). The code for this can be found in the basic number theory module

## Frequency Calculation

Takes in text and returns a dictionary with the counts of all the characters in
the text.

## References
 - Trappe, Wade, and Lawrence C. Washington. Introduction to Cryptography: with
   Coding Theory. Pearson Prentice Hall, 2006.