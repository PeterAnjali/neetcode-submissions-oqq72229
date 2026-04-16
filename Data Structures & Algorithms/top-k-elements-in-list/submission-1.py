class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        keys = sorted(c,key = c.get,reverse=True)[:k]
        return keys