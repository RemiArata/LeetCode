class Solution:
    def romanToInt(self, s):
        possible = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, 
                    "CD": 400, "CM": 900, "M": 1000, "D": 500, 
                    "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        val = 0
        for dig in possible.keys():
            val += s.count(dig) * possible[dig]
            s = s.replace(dig, "")
        return val
        
test = Solution()

print(test.romanToInt("MCMXCIV")) 