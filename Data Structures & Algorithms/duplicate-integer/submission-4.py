class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d=set()
        for i in nums:
            if i in d:
                return True
            d.add(i)
        return False
        