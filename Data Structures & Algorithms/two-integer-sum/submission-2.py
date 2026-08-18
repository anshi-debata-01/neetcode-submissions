class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            sub=target-nums[i]
            if sub not in dic:
                dic[nums[i]]=i
            else:
                return [dic[sub],i]


                
 
        