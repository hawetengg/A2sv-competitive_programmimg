class OrderedStream:

    def __init__(self, n: int):
        self.stream = {}
        self.key_count = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey] = value
        tmp = []
        while self.key_count in self.stream:
            tmp.append(self.stream[self.key_count])
            self.key_count += 1
        return tmp
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)