class Heap:
    def __init__(self, comparator = lambda x,y: x > y ):
        self.storage = []
        self.size = 0
        self.comparator = comparator

    def insert(self, value):
        self.size += 1
        self.storage.append(value)
        self._bubble_up(self.size - 1)

    def delete(self):
        self.size -= 1
        value = self.storage[0]
        self.storage[0] = self.storage[-1]
        del self.storage[-1]
        self._sift_down(0)
        return value

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return self.size

    def _bubble_up(self, index):
        if index <= 0:
            return
        s = self.storage
        parent_index = (index - 1) // 2
        child = s[index]
        parent = s[parent_index]
        if self.comparator(child, parent):
            s[index], s[parent_index] = s[parent_index], s[index]
            self._bubble_up(parent_index)


    def _sift_down(self, index):
        s = self.storage
        child_one = 2 * index + 1
        child_two = 2 * index + 2
        if child_one > self.size - 1:
            return
        elif child_two > self.size - 1:
            swap_index = child_one
        else:
            swap = self.comparator(s[child_one], s[child_two])
            swap_index = child_one if swap else child_two
        if self.comparator(s[swap_index], s[index]):
            s[index], s[swap_index] = s[swap_index], s[index]
            self._sift_down(swap_index)
