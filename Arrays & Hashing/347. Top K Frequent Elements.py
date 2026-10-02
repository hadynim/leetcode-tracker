import heapq
from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        # 1. Count frequencies -> dict of {value: count}
        freq = Counter(nums)                      # O(n)

        # 2. Build array of (count, value) pairs
        arr = [(count, val) for val, count in freq.items()]   # O(m)

        # 3. Convert array to a max-heap (negate count)
        heap = [(-count, val) for count, val in arr]          # O(m)
        heapq.heapify(heap)                                   # O(m) build-heap

        # 4. Pop k largest
        result = []
        for _ in range(k):
            _, val = heapq.heappop(heap)                      # O(log m) each
            result.append(val)

        return result