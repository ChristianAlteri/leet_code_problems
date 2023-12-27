class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        # i, length = len(s) - 1, 0

        # while s[i] == " ":
        #     i -= 1
        # while i >= 0 and s[i] != " ":
        #     length += 1
        #     i -= 1
        # return length
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count the length of the last word
        length = 0 if i < 0 else s[:i + 1].rfind(" ") - i

        return abs(length)
        


            


        