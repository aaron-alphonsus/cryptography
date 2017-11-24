# Viginère Cipher


The Viginère cipher is a variation of the shift cipher. It was thought to be 
secure in the twentieth century however, there were attacks shown as early as 
the nineteenth century by Babbage and Kasiski. Friedman developed more methods 
for breaking the Viginère Cipher and related ciphers in the 1920s.

## Cryptosystem
**Key**  
A vector of chosen key length whose entries are integers from 0 to 25.  
**Encryption Method**  
The encryption is done by shifting each letter of the plaintext by the each 
integer in the key. Once we get to the end of the key, we wrap around to the 
first number.

## Example
Key: (21, 4, 2, 19, 14, 17) - Corresponds to the word _vector_.

Encryption:

|  (plaintext) |  h  |  e  |  r  |  e  |  i  |  s  |  h  |  o  |  w  |  i  |  t  |  w  |  o  |  r  |  k  |  s  |
|    :----:    |:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|     (key)    | 21  |  4  |  2  | 19  | 14  | 17  | 21  |  4  |  2  | 19  | 14  | 17  | 21  |  4  |  2  | 19  |
| (ciphertext) |  c  |  i  |  t  |  x  |  w  |  j  |  c  |  s  |  y  |  b  |  h  |  n  |  j  |  v  |  m  |  l  |

## References
 - Trappe, Wade, and Lawrence C. Washington. Introduction to Cryptography: with
   Coding Theory. Pearson Prentice Hall, 2006.