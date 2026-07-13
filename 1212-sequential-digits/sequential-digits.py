class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        result = []
        sample = "123456789"
        
        # Determine the minimum and maximum possible lengths based on low and high
        min_len = len(str(low))
        max_len = len(str(high))
        
        # Iterate through all valid window lengths
        for length in range(min_len, max_len + 1):
            # Slide the window across the sample string
            for start in range(10 - length):
                num = int(sample[start:start + length])
                
                if low <= num <= high:
                    result.append(num)
                elif num > high:
                    break # Optimization: numbers only get larger from here
                    
        return result