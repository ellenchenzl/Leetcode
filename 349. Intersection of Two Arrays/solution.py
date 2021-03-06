class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersection (nums2,nums1)
        find =set()
        for i in nums1:
            find.add(i)
        
        result=[]
        for i in nums2:
            if i in find:
                result += i,
            find.discard(i)   
        
        return result 
        