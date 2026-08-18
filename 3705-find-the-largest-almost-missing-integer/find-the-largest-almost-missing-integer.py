class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        # return a[0]>a[-1]?a[0]:a[-1]
        if k == len(nums):
            return max(nums)
        if k==1:
            s=[x for x in nums if nums.count(x)==1]
            return max(s) if s else -1
        ans=-1
        if nums.count(nums[0])==1:
            ans=max(ans,nums[0])
        if nums.count(nums[-1])==1:
            ans=max(ans,nums[-1])
        return ans
