'''
work in progress
'''



class Solution:
    def myAtoi(self, s):
        self.val = ""
        self.strip_chars(s)
        if self.val == "" or ("-" in self.val and '+' in self.val):
            return 0
        self.val = int(self.val)
        if self.val > -2 ** 31 and self.val < (2 ** 31) - 1:
            return self.val
        elif self.val < 0:
            return -2 ** 31
        else:
            return (2 ** 31) - 1

    def strip_chars(self, s):
        for itm in s:
            if itm == " ":
                pass
            elif itm in '-+0123456789':
                self.val += itm
            else:
                break
        self.val = self.val.replace(' ', '')
    


test = Solution()

print(test.myAtoi("-91283472332"))


