class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
        }

        for char in s:
            if char in brackets:
                # print("CHARACTER", char)
                stack.append(char)
                # print("STACK", stack)
            elif len(stack) == 0 or char != brackets[stack.pop()]:
                # print("POPPED", brackets[stack.pop()])
                return False
        return len(stack) == 0