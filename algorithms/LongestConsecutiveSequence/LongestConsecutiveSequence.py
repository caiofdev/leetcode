"""
Solution for LongestConsecutiveSequence
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        nums.sort()
        prev = 0.5

        best = 1
        current = 1

        for i in nums:

            if i == prev:
                continue

            if i == prev + 1:
                current += 1
            else: 
                current = 1
            
            if current > best:
                best = current
            
            prev = i

        return best