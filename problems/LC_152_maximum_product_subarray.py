'''
# LC 152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Attempted to solve in 25 minutes
3rd September 2020, 1620--1645

Looked at answer and will try again

Finished implementing solution at time 1711 (11 minutes). 
Will circle back to this for revision.

'''
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Idea here is as follows.
        # Unless you see a zero or a negative value, including an element is
        # always good
        # Iterate through the array in one pass.
        #       - The current minimum product is always
        #    - If current product is 0: then take the number
        #       and record max_product as max(current_product, max_product).
        #    - If current product is not zero: take the number but first
        #       record max_product as max(current_product, max_product)
        if not nums:  # Handle empty array edge case
            return 0

        current_product = nums[0]
        max_mag_product = nums[0]
        max_product = nums[0]
        for num in nums[1:]:
            if current_product:
                max_product = max(current_product, max_product)
                max_product = max(max_product, num)
                current_product *= num
            else:
                max_product = max(current_product, max_product)
                max_product = max(max_product, num)
                current_product = num
        return max(max_product, current_product)


class Solution2:
    def maxProduct(self, nums: List[int]) -> int:
        # The idea here is as follows: Keep in memory current max and min products
        # and go through the array.
        # Keep multiplying, taking care to flip the sign for max and min product.
        # If you ever hit a zero the array is reset, but you'll have already
        # logged the max product in the previous step.

        if not nums:  # Handle empty array edge case
            return 0

        global_max = nums[0]
        min_product = nums[0]
        max_product = nums[0]
        for num in nums[1:]:
            if num < 0:
                # Swap max and min products
                tmp = min_product
                min_product = max_product
                max_product = tmp
            max_product = max(max_product*num, num)
            min_product = min(min_product*num, num)
            global_max = max(max_product, global_max)

        return global_max


def sol(nums: List[int]):
    s = Solution2()
    print(s.maxProduct(nums))


sol([])  # 0
sol([-1])  # -1
sol([1])  # 1
sol([-1, -2])  # 2
sol([-1, 0, -2])  # 0
sol([-1, 2, -2])  # 4
sol([-1, 2, -2, -3])  # 12
sol([-1, 2, -2, 0, -3])  # 4
sol([-1, 2, -2, 0, 6])  # 6
sol([3, -1, 4])  # 4
sol([3, -1, 4, -1, -5])  # 20 but wrong answer, I get 12..

# At 4: max_product = 4, max_magnitude_product = -12
# At -1: max_product = 4, max_magnitude_product = 12
# At 5: max_product =
