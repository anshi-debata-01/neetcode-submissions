class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        #made dict
        d1 = {}
        for i in s:
            if i in d1:
                d1[i]+=1
            else:
                d1[i]=1
        #check t string and compare
        for j in t:
            if j not in d1:
                return False
            d1[j]-=1

            if d1[j]<0:
                return False

        return True
        