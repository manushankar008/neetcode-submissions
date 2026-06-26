class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums :
            freq[n]=freq.get(n,0)+1
        sorted_freq=sorted(freq.items(),key=lambda x:x[1],reverse=True)

        out=[]
        for i in range(k):
            out.append(sorted_freq[i][0])

        return out