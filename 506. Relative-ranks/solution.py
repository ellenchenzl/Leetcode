class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        n=sorted(nums,reverse=True)
        res=[]
        for i in nums:
            if n.index(i)==0:
                res.append("Gold Medal")
            elif n.index(i)==1:
                res.append("Silver Medal")
            elif n.index(i)==2:
                res.append("Bronze Medal")
            else:
                res.append(str(n.index(i)+1))
        return res