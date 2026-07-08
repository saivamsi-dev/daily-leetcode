# # class Solution(object):
# #     def sumAndMultiply(self, s, queries):
# #         MOD = 10**9 + 7
# #         m = len(s)
        
# #         # 1. Extract non-zero digits
# #         A = [int(c) for c in s if c != '0']
# #         n = len(A)
        
# #         if n == 0:
# #             return [0] * len(queries)
            
# #         # 2. Precompute next and previous non-zero index mappings
# #         next_nz = [0] * m
# #         curr = 0
# #         for i in range(m):
# #             if s[i] != '0':
# #                 next_nz[i] = curr
# #                 curr += 1
# #             else:
# #                 next_nz[i] = curr
                
# #         prev_nz = [0] * m
# #         curr = -1
# #         for i in range(m):
# #             if s[i] != '0':
# #                 curr += 1
# #             prev_nz[i] = curr

# #         # 3. Precompute powers of 10 modulo MOD
# #         pow10 = [1] * (n + 1)
# #         for i in range(1, n + 1):
# #             pow10[i] = (pow10[i-1] * 10) % MOD

# #         # 4. Precompute Prefix Sums and Prefix Values
# #         pref_sum = [0] * (n + 1)
# #         pref_val = [0] * (n + 1)
        
# #         for i in range(n):
# #             pref_sum[i+1] = pref_sum[i] + A[i]
# #             pref_val[i+1] = (pref_val[i] * 10 + A[i]) % MOD
            
# #         # 5. Process Queries
# #         ans = []
# #         for l, r in queries:
# #             L = next_nz[l]
# #             R = prev_nz[r]
            
# #             # If there are no non-zero digits in the range [l, r]
# #             if L > R:
# #                 ans.append(0)
# #             else:
# #                 # Get the digit sum in O(1)
# #                 digit_sum = pref_sum[R+1] - pref_sum[L]
                
# #                 # Get the concatenated value x in O(1)
# #                 x = (pref_val[R+1] - pref_val[L] * pow10[R - L + 1]) % MOD
                
# #                 # Multiply and store the result
# #                 ans.append((x * digit_sum) % MOD)
                
# #         return ans


# from bisect import bisect_left, bisect_right

# class Solution(object):
#     def sumAndMultiply(self, s, queries):
#         MOD = 10**9 + 7
        
#         # 1. Store non-zero digits and their original string indices
#         nz_digits = []
#         nz_indices = []
#         for i, c in enumerate(s):
#             if c != '0':
#                 nz_digits.append(int(c))
#                 nz_indices.append(i)
                
#         n = len(nz_digits)
#         if n == 0:
#             return [0] * len(queries)
            
#         # 2. Precompute Prefix Sums and Prefix Values
#         pref_sum = [0] * (n + 1)
#         pref_val = [0] * (n + 1)
#         for i in xrange(n):
#             pref_sum[i+1] = pref_sum[i] + nz_digits[i]
#             pref_val[i+1] = (pref_val[i] * 10 + nz_digits[i]) % MOD
            
#         # 3. Precompute powers of 10
#         pow10 = [1] * (n + 1)
#         for i in xrange(1, n + 1):
#             pow10[i] = (pow10[i-1] * 10) % MOD
            
#         # 4. Fast query processing using Binary Search
#         ans = []
#         for l, r in queries:
#             # Find the first non-zero digit index >= l
#             L = bisect_left(nz_indices, l)
#             # Find the last non-zero digit index <= r
#             R = bisect_right(nz_indices, r) - 1
            
#             if L > R:
#                 ans.append(0)
#             else:
#                 digit_sum = pref_sum[R+1] - pref_sum[L]
#                 x = (pref_val[R+1] - pref_val[L] * pow10[R - L + 1]) % MOD
#                 ans.append((x * digit_sum) % MOD)
                
#         return ans

from bisect import bisect_left as b_left, bisect_right as b_right

class Solution(object):
    def sumAndMultiply(self, s, queries):
        MOD = 10**9 + 7
        
        # 1. Fast parsing using local variable bindings
        nz_digits = []
        nz_indices = []
        for i, c in enumerate(s):
            if c != '0':
                nz_digits.append(int(c))
                nz_indices.append(i)
                
        n = len(nz_digits)
        if n == 0:
            return [0] * len(queries)
            
        # 2. Allocate tracking arrays directly 
        pref_sum = [0] * (n + 1)
        pref_val = [0] * (n + 1)
        pow10 = [1] * (n + 1)
        
        # Unroll calculations into a single fast loop
        for i in xrange(n):
            digit = nz_digits[i]
            pref_sum[i+1] = pref_sum[i] + digit
            pref_val[i+1] = (pref_val[i] * 10 + digit) % MOD
            pow10[i+1] = (pow10[i] * 10) % MOD
            
        # 3. Cache functions locally for maximum performance inside the loop
        ans = []
        local_left = b_left
        local_right = b_right
        
        for l, r in queries:
            L = local_left(nz_indices, l)
            R = local_right(nz_indices, r) - 1
            
            if L > R:
                ans.append(0)
            else:
                digit_sum = pref_sum[R+1] - pref_sum[L]
                x = (pref_val[R+1] - pref_val[L] * pow10[R - L + 1]) % MOD
                ans.append((x * digit_sum) % MOD)
                
        return ans