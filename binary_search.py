from typing import List, Dict

class Solution:
    # O(log(n)) - time, O(1) - space
    def binarySearchIterate(self, nums: List[int], target: int):

        left=0
        right=len(nums) - 1

        if left > right:
            return -1

        while left <= right:
            middle = (left + right) // 2
            match = nums[middle]

            if target == match:
                return middle
            
            elif target < match:
                right = middle - 1
            
            else:
                left = middle + 1

        return -1


# O(log(n)) - time, O(log(n)) - space
def binarySearchRecurse(nums: List[int], target: int):
    return binarySearchRecurseUtil(nums, target, 0, len(nums) - 1)

def binarySearchRecurseUtil(nums: List[int], target: int, left, right):

    if left > right:
        return -1
    middle = (left + right) // 2
    match = nums[middle]
    if target == match:
        return middle
    
    elif target < match:
        return binarySearchRecurseUtil(nums, target, left, middle - 1)
    
    else:
        return binarySearchRecurseUtil(nums, target, middle + 1, right)
        