# 3637. Trionic Array I
#An array is trionic if there exist indices 0 < p < q < n − 1 such that:
#nums[0...p] is strictly increasing,
#nums[p...q] is strictly decreasing,
#nums[q...n − 1] is strictly increasing.
#Return true if nums is trionic, otherwise return false.

def isTrionic(nums: list[int]) -> bool:
        if len(nums) < 4:
            return False
        else:
            ans = []
            check = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[i-1]:
                    if check == 0 or check == -1:
                        ans.append(1)
                    check = 1
                elif nums[i] < nums[i-1]:
                    if check == 0 or check == 1:
                        ans.append(-1)
                    check = -1
                else:
                     return False
        if ans == [1, -1, 1]:
            return True
        else:
            return False