class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            #for j in range(i+1,len(nums)):
            #    if(nums[i]+nums[j] == target):
             #       return [i,j]
        #return []
          diff = target-nums[i]
          if diff in hash:
            return [hash[diff],i]
          else:
            hash[nums[i]]= i