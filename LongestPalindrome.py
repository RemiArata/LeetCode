'''
class Solution:
    def longestPalindrome(self, s):
        lngst = ""
        for i in range(0, len(s)):
            for j in range(i, len(s)):
                sub_string = s[i: j + 1]
                if sub_string == sub_string[::-1]:
                    if len(sub_string) > len(lngst):
                        lngst = sub_string
        return lngst

test = Solution()

print(test.longestPalindrome("babad"))
'''
    
class Solution:
    def longestPalindrome(self, s):
        pass
    
