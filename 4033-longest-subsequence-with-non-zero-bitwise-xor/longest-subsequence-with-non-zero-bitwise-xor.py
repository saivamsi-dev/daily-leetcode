class Solution:

  def longestSubsequence(self, nums: list[int]) -> int:
    total_xor = 0
    has_nonzero = False

    # Single pass to check for non-zero elements and compute total XOR
    for num in nums:
      if num != 0:
        has_nonzero = True
      total_xor ^= num

    # Case 1: All elements are 0
    if not has_nonzero:
      return 0

    # Case 2: Total XOR is non-zero -> keep all N elements
    if total_xor != 0:
      return len(nums)

    # Case 3: Total XOR is 0 -> remove 1 non-zero element
    return len(nums) - 1