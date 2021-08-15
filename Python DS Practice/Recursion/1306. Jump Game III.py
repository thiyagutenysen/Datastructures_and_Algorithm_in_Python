# https://leetcode.com/problems/jump-game-iii/
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        def recursion(arr, start):
            if start >= 0 and start < len(arr):
                if arr[start] == 0:
                    return True
                else:
                    next1 = start + arr[start]
                    next2 = start - arr[start]
                    if next1 < next2:
                        return False
                    else:
                        arr[start] = -1
                        return (recursion(arr, next1) or recursion(arr, next2))
            else:
                return False

        #print(recursion(arr.copy(), start))
        return recursion(arr, start)
