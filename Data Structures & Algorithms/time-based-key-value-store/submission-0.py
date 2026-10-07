class TimeMap:

    def __init__(self):
        #key -> val pair {key -> [value, timestamp]} [1,2,,4]
        self.map = defaultdict(list)    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append([value, timestamp])
#find latest /most recent timestamp
    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.map.get(key, [])
        L, R = 0, len(values) - 1
        while L <= R:
            mid = (L+R) //2
            if values[mid][1] == timestamp:
                res = values[mid][0]
                return res
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                L = mid +1
            else:
                R = mid -1
        return res
