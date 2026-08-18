class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        d1={}
        for i in nums:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1   
        sorted_freq = sorted(d1.items(), key=lambda x: x[1], reverse=True)

        ans = []

        # Take first k keys
        for i in range(k):
            ans.append(sorted_freq[i][0])

        return ans


        