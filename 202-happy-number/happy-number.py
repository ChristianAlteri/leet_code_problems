class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        seen = set()  
        
        while n != 1:
            if n in seen:
                return False  
            seen.add(n)
            n = self.solve(n)

        return True

    def solve(self, num):
        ans = 0
        while num > 0:
            digit = num % 10
            ans += digit ** 2
            num //= 10
        return ans