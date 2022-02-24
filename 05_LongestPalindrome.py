class Solution:
    def longestPalindrome(self, s):
        lngst = ''
        for i in range(0, len(s)):
            if len(lngst) > len(s) - i: break
            for j in range(len(s), i, -1):
                sub = s[i:j]
                if sub == sub[::-1]:
                    if len(lngst) < len(sub):
                        lngst = sub
        return lngst