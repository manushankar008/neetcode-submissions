class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        mx=0
        for n in seen:
            if n-1 not in seen:
                count=0
                for i in range(len(nums)):
                    if n+i in seen:
                        count+=1
                    else:
                        break
                if mx<count:
                    mx=count
        return mx
                    
