class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        sum1=0
        addtot=0
         
        for i,v in enumerate (A):
            addtot=addtot+v
            sum1=sum1+v*i
        res=sum1    
        for i in range(len(A)):
            sum1=sum1+addtot-len(A)*A[-i-1]
            
            res=  max(sum1,res)
        return res
        