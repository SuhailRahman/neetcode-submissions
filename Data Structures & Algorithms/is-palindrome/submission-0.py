class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0 
        r = len(s)-1

        def isNonAlphaNumeric(ch):
            if (ord('a') <= ord(ch) and ord(ch) <= ord('z')) or (ord('A') <= ord(ch) and ord(ch) <= ord('Z')) or (ord('0') <= ord(ch) and ord(ch) <= ord('9')):
                return False
            return True

        while l < r:
            if isNonAlphaNumeric(s[l]):
                l += 1
            elif isNonAlphaNumeric(s[r]):
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1

        return True