class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            # print(haystack.index(needle))
            return haystack.index(needle)
        else:
            # print('False')
            return -1