class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < k:
            return []
        
        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count.setdefault(num, 1)

        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)

        return sorted_elements[:k]