class Solution:
    import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert all weights to negative to simulate a Max-Heap using Python's Min-Heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)
        
        # Continue smashing until 0 or 1 stone is left
        while len(max_heap) > 1:
            # Pop the two heaviest stones (remember they are negative)
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)
            
            # If they are not equal, the remaining weight is put back into the heap
            # Since stone1 is heavier (more negative) than stone2, stone1 - stone2 will be negative
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)
        
        # If the heap is empty, return 0; otherwise, return the absolute value of the last stone
        return -max_heap[0] if max_heap else 0
   