# Import for twoSum argument data structures
from typing import List, Dict

class Solution:

    # O(n^2) - time | O(1) - space
    def twoSumBrute(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            fn = nums[i]
            for j in range(i+1, len(nums) - 1):
                sn = nums[j]
                if fn + sn == target:
                    return[fn,sn]
        return []


    # O(nlog(n)) - time | O(1) - space
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        # Left pointer
        l = 0

        #Right pointer
        r = len(nums) - 1

        # Looping right and left pointer to find first match 
        while l < r:
            current = nums[l] + nums[r]
            if current == target:
                return [nums[l], nums[r]]
            elif current < target:
                l += 1
            elif  current > target:
                r -= 1
        return[]

    # O(n) - time | O(n) - space
    def twoSumDict(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        for n in nums:
            match = target - n
            if match in arr:
                return[match,n]
            else:
                arr[n] = True

        return []










