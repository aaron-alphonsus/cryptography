class Affine:
    
    """The encode function works on the input string, transforming each letter 
    by multiplying it by alpha and adding beta to it. It handles both uppercase
    and lowercase inputs."""
    def encode(self, plaintext, alpha, beta):
        ciphertext = ''
        for letter in plaintext:
            if 65 <= ord(letter) <= 90:
                ciphertext += chr((alpha * (ord(letter)-65) + beta) % 26 + 65)   
            elif 97 <= ord(letter) <= 122:
                ciphertext += chr((alpha * (ord(letter)-97) + beta) % 26 + 97) 
        
        print(ciphertext) 
    
    """decode calculates the decryption function (if possible) and then decrypts
    the string"""
    # def decode(ciphertext, alpha, beta):
        # gmpy -> invert(alpha, beta) 
