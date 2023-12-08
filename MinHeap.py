class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()

    def delete_min(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        return min_val

    def _heapify_up(self):
        index = len(self.heap) - 1

        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self):
        index = 0
        while True:
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2
            smallest = index

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break

    def preorder_traversal(self, index=0):
        result = []
        if index < len(self.heap):
            result.append(self.heap[index])
            result += self.preorder_traversal(2 * index + 1)
            result += self.preorder_traversal(2 * index + 2)
        return result

    def inorder_traversal(self, index=0):
        result = []
        if index < len(self.heap):
            result += self.inorder_traversal(2 * index + 1)
            result.append(self.heap[index])
            result += self.inorder_traversal(2 * index + 2)
        return result

    def postorder_traversal(self, index=0):
        result = []
        if index < len(self.heap):
            result += self.postorder_traversal(2 * index + 1)
            result += self.postorder_traversal(2 * index + 2)
            result.append(self.heap[index])
        return result

# Example usage:
min_heap = MinHeap()
min_heap.insert(4)
min_heap.insert(8)
min_heap.insert(2)
min_heap.insert(5)
min_heap.insert(10)
min_heap.insert(11)
min_heap.insert(13)
min_heap.insert(3)
min_heap.insert(9)
min_heap.insert(20)
print(min_heap.heap)
print("Min Heap:")
print("Heap:", min_heap.heap)

print("\nPreorder Traversal:", min_heap.preorder_traversal())
print("Inorder Traversal:", min_heap.inorder_traversal())
print("Postorder Traversal:", min_heap.postorder_traversal())

print("\nDeleting Min Element:", min_heap.delete_min())
print("Heap after deletion:", min_heap.heap)
