# cc.py

# This file contains the menu to call and run all the modules in this section.

# TODO
#  - Figure out multiple file Python programs
#  - Affine Ciphers, encode and decode, letting the user provide α, β and the 
#    text (both plain and cipher text). 
#  - Multi-alphabet cipher (Vigenère Cipher), encode and decode, letting the 
#    user provide the key and text (both plain and cipher text). 
#  - Frequency calculation, let the user provide a text, and calculate the 
#    frequency of the different characters in the text.  This is the basis for 
#    an attack. 
#  - Affine Cipher attacks 
#  - An attack on Vigenère Cipher, by finding the key length and the key. 
#  - At least one of the following: 
#     - ADFGX cipher, encode and decode 
#     - Block Cipher, encode and decode 
#     - One-Time pads, by either Pseudo-random Bit Generation, or Linear 
#       Feedback Shift 
#     - Register Sequence, encode and decode 
#     - Attack on Linear Feedback Shift Register 
#     - An Enigma simulator. 

# Mock main function
# Authors: Aaron Alphonsus and Dr. John Weiss
def main():
    while True:
        cmd = input("a: Affine Cipher\n"\
        "b: Vigenère Cipher\n"\
        "c: Frequency Calculation\n"\
        "d: Affine Cipher Attacks\n"\
        "e: Vigenère Cipher Attack\n"\
        "f: Extra Module\n"\
        "x: Exit\n"\
        "Enter a command: ")
        
        if   cmd == 'a': a()                                                     
        elif cmd == 'b': b()                                                     
        elif cmd == 'c': c()                                                     
        elif cmd == 'd': d()                                                     
        elif cmd == 'e': e()
        elif cmd == 'f': f()                                                     
        elif cmd == 'x': break                                                   
        else: print( "\nInvalid command, please try again!\n" ) 

def a(): print("\nYou selected Affine Cipher!\n" )                          
def b(): print("\nYou selected Vigenère Cipher!\n" )                                  
def c(): print("\nYou selected Frequency Calculation!\n" )                          
def d(): print("\nYou selected Affine Cipher Attacks!\n" )                    
def e(): print("\nYou selected Vigenère Cipher Attack!\n" )
def f(): print("\nYou selected Extra Module!\n" )    

# For the main() function
if __name__ == '__main__':                                                       
    main()
