# https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        def new_function(n):
            if n % 3 != 0 and (n-1) % 3 != 0:
                return False
            elif n == 0:
                return True
            elif (n-1) % 3 == 0:
                return new_function(n-1)
            else:
                return new_function(n//3)
        print(new_function(n))
        return new_function(n)
