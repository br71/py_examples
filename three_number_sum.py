from typing import List


# O(n^2) - time, O(n) - space
def three_number_sum(array: List[int], target_sum) -> list:

    # Sorting is nlog(n) operation
    array.sort()
    triplets = []

    # Iterating to -2 because we are looking for triplets
    for i in range(len(array) - 2):

        # We will have left and right pointers for iteration
        left = i + 1
        right = len(array) - 1

        # Break iteration in when left and right overlap
        while left < right:
            current_sum = array[i] + array[left] + array[right]

            # if we find sum then we will append triplets
            if current_sum == target_sum:
                triplets.append(array[i])
                triplets.append(array[left])
                triplets.append(array[right])
                left += 1
                right -= 1

            # If sum is less than target we will move left pointer
            # because we want to increase sum (array is sorted)
            elif current_sum < target_sum:
                left += 1

            # If sum is greater than target we will move right pointer
            # because we want to decrease sum (array is sorted)
            elif current_sum > target_sum:
                right -= 1

    return triplets


myarray = [12, 3, 1, 2, -6, 5, -8, 6]
mytarget_sum = 0

print(three_number_sum(myarray, mytarget_sum))
# Expected result: [-8, 2, 6, -8, 3, 5, -6, 1, 5]


