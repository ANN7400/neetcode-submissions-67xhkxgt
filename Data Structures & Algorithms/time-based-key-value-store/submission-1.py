class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Get the list of values for this key
        values = self.store.get(key, [])
        
        # Binary search for the timestamp
        low, high = 0, len(values) - 1
        while low <= high:
            mid = (low + high) // 2
            # If current timestamp is <= target, it's a potential answer
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                low = mid + 1 # Look for a more recent valid timestamp
            else:
                high = mid - 1
                
        return res