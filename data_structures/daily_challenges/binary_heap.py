"""
Binary heap implementation
"""


class BinaryHeap:
    def __init__(self):
        self.min_heap = []
        self.last_index = -1

    def push(self, num):
        self.last_index += 1
        self.min_heap.append(num)
        self._sift_up(self.last_index)

    def pop(self):
        if self.length() == 0:
            raise Exception("Heap is empty")
        self.min_heap[0], self.min_heap[self.last_index] = (
            self.min_heap[self.last_index],
            self.min_heap[0],
        )
        elt = self.min_heap[self.last_index]
        self.last_index -= 1
        if self.length() > 1:
            self._sift_down(0)

        return elt

    def parent(self, index, default_val):
        if index == 0:
            return None, default_val
        parent_index = (index - 1) // 2
        return parent_index, self.min_heap[parent_index]

    def left_child(self, index, default_val):
        new_index = 2 * index + 1
        if new_index <= self.last_index:
            return new_index, self.min_heap[new_index]
        return None, default_val

    def right_child(self, index, default_val):
        new_index = 2 * index + 2
        if new_index <= self.last_index:
            return new_index, self.min_heap[new_index]
        return None, default_val

    def _sift_up(self, index):
        while True:
            parent_idx, parent_val = self.parent(index, self.min_heap[index])
            if parent_val <= self.min_heap[index]:
                break
            self.min_heap[index], self.min_heap[parent_idx] = (
                self.min_heap[parent_idx],
                self.min_heap[index],
            )

            index = parent_idx

    def _sift_down(self, index):
        val = self.min_heap[index]
        while True:
            left_index, left_val = self.left_child(index, val)
            right_index, right_val = self.right_child(index, val)
            if self.min_heap[index] <= left_val and self.min_heap[index] <= right_val:
                break
            index_to_be_changed_with = -1
            # print(left_val, right_val)
            if left_val < right_val:
                index_to_be_changed_with = left_index
            else:
                index_to_be_changed_with = right_index
            self.min_heap[index], self.min_heap[index_to_be_changed_with] = (
                self.min_heap[index_to_be_changed_with],
                self.min_heap[index],
            )
            index = index_to_be_changed_with

    def length(self):
        return self.last_index + 1


heap = BinaryHeap()
heap.push(10)
heap.push(5)
heap.push(12)
heap.push(7)
heap.push(9)
heap.push(8)
heap.push(7)
heap.push(8)
print("===============================")
while heap.length() > 0:
    print(heap.pop(), end=" ")
    # print(heap.min_heap)

print()
