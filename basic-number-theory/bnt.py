# TODO: Get rid of classes? Switch to just modules of functions?

class CryptoMath:

    # TODO: Convert to iterative?
    def gcd(self, a, b):
        """
        >>> t = CryptoMath()
        >>> t.gcd(69, 3)
        3
        >>> t.gcd(3, 69)
        3
        >>> t.gcd(5, 7)
        1

        :param a: first number
        :param b: second number
        :return: greatest common divisor of a and b
        """
        if a <= 0 or b <= 0:
            return 0
        
        elif b > a:
            return self.gcd(b,a)
        
        elif a % b == 0: 
            return b
        else:
            return self.gcd(a % b, b)
    
    def extendedgcd(a, n):

        return 0

    def findModInverse(a, n):
        return 0
