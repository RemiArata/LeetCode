
import unittest

class Solution:
    def isValid(self, s):
        parens = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        strng = []

        for itm in s:
            if itm in ["(", "{", "["]:
                strng.append(itm)
            elif (strng == []) and (itm in ["]", "}", ")"]):
                return False
            else:
                if strng[-1] == parens[itm]:
                    strng.pop()
                else:
                    break
        return not bool(strng)


class tester(unittest.TestCase):
    
    def test_one(self):
        t1 = Solution()
        self.assertTrue(t1.isValid("()"))
    
    def test_two(self):
        t2 = Solution()
        self.assertTrue(t2.isValid("()[]{}"))
    
    def test_three(self):
        t3 = Solution()
        self.assertFalse(t3.isValid("(]"))
    
    def test_four(self):
        t4 = Solution()
        self.assertFalse(t4.isValid("([)]"))
    
    def test_five(self):
        t5 = Solution()
        self.assertTrue(t5.isValid("{[]}"))


if __name__ == "__main__":
    unittest.main()
