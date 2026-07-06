# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: None Do not return anything, modify nums in-place instead.
#         """
#         z=nums.count(0)
#         c=0
#         for i in nums:
#             if i != 0:
#                 nums[c]=i
#                 c+=1
#         # for i range()
#         for i in range(z):
#             nums[c]=0
#             c+=1
#         return nums


class Solution(object):

    def moveZeroes(self, nums):
        """Do not return anything, modify nums in-place instead."""
        # 'insert_pos' tracks where the next non-zero element should be placed
        insert_pos = 0

        # Single pass through the array
        for current in range(len(nums)):
            # When we hit a non-zero element, swap it with the element at insert_pos
            if nums[current] != 0:
                nums[insert_pos], nums[current] = (
                    nums[current],
                    nums[insert_pos],
                )
                insert_pos += 1

        return nums