class Cryptomath:
    
    def gcd (self, a, b):
        
        if a <=0 or b <= 0:
            return 0
        
        elif b > a:
            return self.gcd(b,a)
        
        elif a % b == 0: 
            return b
        else:
            return self.gcd(a % b, b)
    
    def extendedgcd (a, n):
        return 0

    def findModInverse(a, n):
        return 0
