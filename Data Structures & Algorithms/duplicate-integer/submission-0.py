class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict={}
        for i in nums:
          if i in dict:                #if dict[i]:
             return True
          else:
             dict[i]=1
        return False