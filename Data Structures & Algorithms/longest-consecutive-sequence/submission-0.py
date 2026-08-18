class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
           
        longest = 0
        n = set(nums)
        for i in n:
            if i-1 not in n:
                current = 1
                while i+1 in n:
                    i+=1
                    current+=1
                longest=max(longest,current)
        return longest    
        