"""
    Given an integer n, add a dot (".") as the thousands separator and return it in string format
"""

class Solution:
    def thousandSeparator(self, n: int) -> str:
        result = ''
        nstr = str(n)

        for i in range(len(nstr) - 1, -1, -1):
            print(i)

        return result

a = Solution()
a.thousandSeparator(1239458)
print("end")



