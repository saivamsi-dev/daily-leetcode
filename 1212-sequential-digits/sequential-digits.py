# class Solution(object):
#     def sequentialDigits(self, low, high):
#         """
#         :type low: int
#         :type high: int
#         :rtype: List[int]
#         """
#         result = []
#         sample = "123456789"
        
#         # Determine the minimum and maximum possible lengths based on low and high
#         min_len = len(str(low))
#         max_len = len(str(high))
        
#         # Iterate through all valid window lengths
#         for length in range(min_len, max_len + 1):
#             # Slide the window across the sample string
#             for start in range(10 - length):
#                 num = int(sample[start:start + length])
                
#                 if low <= num <= high:
#                     result.append(num)
#                 elif num > high:
#                     break # Optimization: numbers only get larger from here
                    
#         return result


class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        
        min_len = len(str(low))
        max_len = len(str(high))
        
        for length in range(min_len, max_len + 1):
            if length > 9:
                break
                
            # Construct the baseline number and the adder step for this length
            # e.g., for length 3: num = 123, step = 111
            num = 0
            step = 0
            for i in range(1, length + 1):
                num = num * 10 + i
                step = step * 10 + 1
            
            # Mathematically roll through the sequential numbers of this length
            for _ in range(10 - length):
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    return result # Since lengths & numbers only grow, we can exit early completely
                
                num += step
                
        return result