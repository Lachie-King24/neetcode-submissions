class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1 # We want a Left and right pointer

        while l < r:
            # Use function to check if pointers are alphaNum
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            # compare the 2 sides, if they don't match, end function here and return False
            if s[l].lower() != s[r].lower():
                return False
            # increment
            l, r = l + 1, r - 1
        return True

    def alphaNum(self, c):
        # Create a function that checks if 'c' is in between the ASCII values of alphanumeric characters
        return (ord('A') <= ord(c) <= ord('Z') or 
        ord('a') <= ord(c) <= ord('z') or 
        ord('0') <= ord(c) <= ord('9'))