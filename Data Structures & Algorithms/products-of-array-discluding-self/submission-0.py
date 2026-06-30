class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[0]* len(nums)
        right=[0]*len(nums)
        ans=[0]*len(nums)
        for i in range (len(nums)):
            if i==0:
                left[i]=1
            else:
                left[i]=nums[i-1]*left[i-1]
        j=len(nums)-1
        while j >=0:
            if j==len(nums)-1:
                right[j]=1
                j-=1
            else:
                right[j]=nums[j+1]*right[j+1]
                j-=1
        for i in range (len(nums)):
            ans[i]=left[i]*right[i]

        return ans
