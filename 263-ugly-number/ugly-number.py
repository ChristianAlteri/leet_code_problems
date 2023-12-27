class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        
        for p in [2, 3, 5]:
            while n % p == 0: # this says if n mod 2,3,5 is 0 then it is divisble by 2,3,5
                n //= p
        return n == 1




        