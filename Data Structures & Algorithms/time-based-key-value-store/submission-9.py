class TimeMap:

    def __init__(self):
        self.keyValues = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keyValues:
            self.keyValues[key].append(value)
            self.timestamps[key].append(timestamp)
        else:
            self.keyValues[key] = [value]
            self.timestamps[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.keyValues:
            return ""

        timestamps = self.timestamps[key]

        l = 0
        r = len(timestamps) - 1
        lastLeft = l
        m = -1

        while l < r:
            m = (l + r) // 2

            if timestamps[m] == timestamp:
                return self.keyValues[key][m]
            elif timestamps[m] < timestamp:
                lastLeft = l
                l = m + 1
            else:
                r = m
        
        m = (l + r) // 2
        if timestamps[m] <= timestamp:
            return self.keyValues[key][m]
        elif timestamps[lastLeft] <= timestamp:
            return self.keyValues[key][lastLeft]
        else:
            return ""






