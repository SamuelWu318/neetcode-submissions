class MinStack:

    def __init__(self):
        self.mp = defaultdict(list)
        self.last_i = -1


    def push(self, val: int) -> None:
        self.last_i += 1
        if len(self.mp) > 0:
            self.mp[len(self.mp)] = [val, min(val, self.mp[len(self.mp) - 1][1]), max(val, self.mp[len(self.mp) - 1][2])]
        else:
            self.mp[len(self.mp)] = [val, val, val]

    def pop(self) -> None:
        self.mp.popitem()
        self.last_i -= 1

    def top(self) -> int:
        return self.mp[self.last_i][0]

    def getMin(self) -> int:
        return self.mp[self.last_i][1]
        


[1, 2, -2, -1, -2]
