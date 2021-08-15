# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alpha = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        def recursion(n, output):
            if len(n) == 0:
                return output
            else:
                new_output = []
                for i in range(len(output)):
                    for j in alpha[int(n[0])-2]:
                        new_output.append(output[i]+j)
                return recursion(n[1:], new_output)
        if len(digits) == 0:
            return []
        else:
            output = [""]
            return recursion(digits, output)
