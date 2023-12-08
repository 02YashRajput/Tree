class Maxheap:
    def __init__(self):
        self.heap = []

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up()

    def heapify_up(self):
        index= len(self.heap)-1
        while(index>0):
            parent = (index-1)//2
            if self.heap[parent]<self.heap[index]:
                self.heap[parent],self.heap[index] = self.heap[index],self.heap[parent]
                index= parent
            else:
                break

    def delete(self):
        if len(self.heap)==0:
            print("Empty heap")
            return
        elif len(self.heap)==1:
            return self.heap.pop(0)
        val = self.heap[0]
        self.heap[0]= self.heap.pop()
        self.heapify_down()
        return val
    
    def heapify_down(self):
        index = 0
        while True:
            left_child_index = 2*index+1
            right_child_index = 2*index+2
            largest = index
            if left_child_index<len(self.heap) and self.heap[left_child_index]>self.heap[index]:
                largest = left_child_index
            if right_child_index<len(self.heap) and self.heap[right_child_index]>self.heap[largest]:
                largest = right_child_index
            if largest!=index:
                self.heap[index],self.heap[largest]=self.heap[largest],self.heap[index]
                index = largest
            else:
                break




Max = Maxheap()
Max.insert(10)
Max.insert(50)
Max.insert(9)
Max.insert(16)
Max.insert(20)
print(Max.heap)
Max.delete()
print(Max.heap)