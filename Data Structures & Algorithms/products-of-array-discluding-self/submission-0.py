class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=(len(nums))
        output=[0]*n
        pre=1
        post=1
        for i in range(n):
            if i==0:
                output[i]=1
            output[i]=pre
            pre=pre*nums[i]
        for i in range(n-1, -1, -1):
            if i==n-1:
                post=post*nums[i]
                continue
            output[i]=output[i]*post
            post=post*nums[i]
        return output


        