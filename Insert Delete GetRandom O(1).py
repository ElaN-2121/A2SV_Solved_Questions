class RandomizedSet:

    def __init__(self):
        self.store  = {} # to insert and delete at O(1)
        self.num_store = [] # to get random elements at O(1)

    def insert(self, val: int) -> bool:
        if val in self.store:
            return False

        self.num_store.append(val)
        self.store[val] = len(self.num_store) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.store:
            return False

        last_element = self.num_store[-1]
        index = self.store[val]

        self.num_store[index] = last_element
        self.store[last_element]= index

        self.num_store.pop()
        del self.store[val]
        return True

    def getRandom(self) -> int:
        random_integer = random.randint(0, len(self.num_store)-1)
        return self.num_store[random_integer]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
