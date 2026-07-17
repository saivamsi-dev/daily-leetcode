import bisect

class Solution(object):
    def gcdValues(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[int]
        :rtype: List[int]
        """
        max_num = max(nums)
        
        # 1. Count the frequency of each number in nums
        count = [0] * (max_num + 1)
        for num in nums:
            count[num] += 1
            
        # gcd_counts[i] will store the exact number of pairs with GCD equal to i
        gcd_counts = [0] * (max_num + 1)
        
        # 2 & 3. Process backwards to implement inclusion-exclusion
        for i in range(max_num, 0, -1):
            # Count how many numbers in nums are multiples of i
            multiples_count = 0
            for j in range(i, max_num + 1, i):
                multiples_count += count[j]
            
            # Total pairs that have 'i' as a common divisor
            total_pairs = (multiples_count * (multiples_count - 1)) // 2
            
            # Subtract pairs that have a larger multiple of i as their actual GCD
            minus_pairs = 0
            for j in range(2 * i, max_num + 1, i):
                minus_pairs += gcd_counts[j]
                
            gcd_counts[i] = total_pairs - minus_pairs
            
        # 4. Build the Prefix Sum array
        pref = [0] * (max_num + 1)
        for i in range(1, max_num + 1):
            pref[i] = pref[i - 1] + gcd_counts[i]
            
        # 5. Answer each query using binary search
        ans = []
        for q in queries:
            # We look for the first index where pref[idx] > q
            idx = bisect.bisect_right(pref, q)
            ans.append(idx)
            
        return ans