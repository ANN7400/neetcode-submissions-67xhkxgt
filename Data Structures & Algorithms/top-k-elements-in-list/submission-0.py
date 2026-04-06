class Solution:
    def topKFrequent(self, nums, k):
        count = {}
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Sort by frequency (value) in descending order, take first k keys
        return sorted(count, key=lambda x: count[x], reverse=True)[:k]