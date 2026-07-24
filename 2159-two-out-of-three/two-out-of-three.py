# class Solution:
#     def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
#         s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        
#         # Combine pairs present in at least two sets
#         return list((s1 & s2) | (s2 & s3) | (s1 & s3))

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        setnums = set(nums1+nums2+nums3)
        ans = []
        for i in setnums:
            if ((i in nums1 and i in nums2) or (i in nums1 and i in nums3) or (i in nums2 and i in nums3)):
                ans.append(i)
        return ans;
        


        
        