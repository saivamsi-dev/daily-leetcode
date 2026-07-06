from functools import cmp_to_key

class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # Define a custom comparison function
        def compare(a, b):
            # If start points are different, sort by start point ascending
            if a[0] != b[0]:
                return a[0] - b[0]
            # If start points are equal, sort by end point descending
            else:
                return b[1] - a[1]
        
        # Sort using the comparison function converted to a key
        intervals.sort(key=cmp_to_key(compare))
        
        count = 0
        max_end = 0
        
        for start, end in intervals:
            if end > max_end:
                count += 1
                max_end = end
                
        return count