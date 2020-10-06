from typing import List


class Solution:
    # Part 1: LC 217
    def containsDuplicate(self, nums: List[int]) -> bool:
        record = {}
        for num in nums:
            if num not in record:
                record[num] = True
            else:
                return True

        return False

    '''
    # Part 2: LC 219
    Given an array of integers and an integer k, find out whether there
    are two distinct indices i and j in the array such that nums[i] = nums[j]
    and the absolute difference between i and j is at most k.
    '''

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        record = {}
        for index, num in enumerate(nums):
            if num not in record:
                record[num] = [index]
            else:
                last = record[num][-1]
                diff = abs(index - last)
                record[num].append(index)

                if diff <= k:
                    return True
        return False
        pass

    '''
    # Part III: LC 220
    Given an array of integers, find out whether there are two distinct
    indices i and j in the array such that the absolute difference between
    nums[i] and nums[j] is at most t and the absolute difference between i
    and j is at most k.
    '''

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        pass


sol = Solution()

# Empty array
print(sol.containsDuplicate([]))  # false
# Unary array
print(sol.containsDuplicate([1]))  # false
# Regular arrays
print(sol.containsDuplicate([1, 2]))  # false
print(sol.containsDuplicate([2, 2]))  # true
print(sol.containsDuplicate([1, 2, 2]))  # true
print(sol.containsDuplicate([1, 2, 3, 4]))  # false
