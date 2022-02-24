class Solution:
    def longestCommonPrefix(self, strs):
        prefix = ""
        shortest = min(strs, key = len)

        for idx, val in enumerate(shortest):
            in_all = True
            for strng in strs:
                if strng[idx] != val:
                    in_all = False
                    break
            if in_all:
                prefix += val
            else:
                break
        return prefix


test = Solution()
pr = test.longestCommonPrefix(["flower","flow","flight"])
print(pr)

pr = test.longestCommonPrefix(["dog","racecar","car"])
print(pr)

pr = test.longestCommonPrefix(["cir","car"])
print(pr)