class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictFreq={}
        h=0
        op=[]
        for i in nums:
            dictFreq[i]=dictFreq.get(i, 0)+1
        while k>0:
            h=max(dictFreq, key=dictFreq.get)
            op.append(h)
            del dictFreq[h]
            k-=1
        return op