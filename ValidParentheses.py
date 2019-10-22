class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        return not stack
