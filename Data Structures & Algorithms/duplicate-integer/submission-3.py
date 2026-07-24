class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l=[]
        for i in range(len(nums)):
            if nums[i] in l:
                continue
            l.append(nums[i])
        if len(nums)==len(l):
            return False
        else:
            return True