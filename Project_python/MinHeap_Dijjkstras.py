class MinHeap:
    def __init__(self,array):
        self.vertexes = {id:id for id in range(len(array))}
        self.heap = self.buildHeap(array)
  
    # O(n) Time | O(1) space
    def buildHeap(self,array):
        firstParent = (len(array)-2)//2
        for CurrentIdx in reversed(range(firstParent+1)):
            self.siftDown(CurrentIdx,len(array)-1,array)
        return array

 #    # O(logn) Time | O(1) space
    def siftDown(self,CurrentIdx,EndIdx,heap):
        childOneIdx = 2*CurrentIdx+1
        while childOneIdx < EndIdx:
            childTwoIdx = -1 if 2* CurrentIdx+2 >= EndIdx else 2*CurrentIdx+2
            if childTwoIdx != -1 and heap[childTwoIdx][1] < heap[childOneIdx][1]:
                IdxToSwap = childTwoIdx
            else:
                IdxToSwap = childOneIdx
            if  heap[CurrentIdx][1] > heap[IdxToSwap][1]:
                self.swap(CurrentIdx,IdxToSwap,heap)
                CurrentIdx = IdxToSwap
                childOneIdx = 2*CurrentIdx +1 
            else:
                break
    

    # O(n) Time | O(1) space
    def siftUp(self,CurrentIdx,heap):
        ParentIdx = (CurrentIdx-1)//2
        while CurrentIdx >0 and self.heap[CurrentIdx][1]< self.heap[ParentIdx][1]:
            self.swap(CurrentIdx,ParentIdx,self.heap)
            CurrentIdx = ParentIdx
            ParentIdx = (CurrentIdx-1)//2
        return heap

    # O(1) Time | O(1) space

    def peek(self):
        return self.heap[0]

    # O(logn) Time | O(1) space

    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        vertex,itemRemoved = self.heap.pop()
        self.vertexes.pop(vertex)
        self.siftDown(0,len(self.heap)-1,self.heap)
        return vertex,itemRemoved

    def lenM1(self,array):
        return len(array)-1

    # O(n) Time | O(1) space
    def insert(self,item):
        self.heap.append(item)
        self.siftUp(len(self.heap)-1,self.heap)
    
    def update(self,Idx,item):
        self.heap[self.vertexes[Idx]] = (Idx,item)
        self.siftUp(self.vertexes[Idx],self.heap)

    def swap(self,i,j,heap):
        self.vertexes[self.heap[i][0]]=j
        self.vertexes[self.heap[j][0]] =i
        heap[j],heap[i]=  heap[i],heap[j]
        return heap[j],heap[i]
    

def isMinHeapPropertyTrue(array):
    for CurrentIdx in range(1,len(array)+1):
        ParentIdx = (CurrentIdx-1)//2
        if array[ParentIdx]> array[CurrentIdx]:
            return False
        return True

if __name__ == "__main__":
    array2 = [48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41]


    print("Before:",array2)
    print(f"Initial Check of MinHeap Property:",isMinHeapPropertyTrue(array2))

    print("Building Min Heap....")
    array2_return = MinHeap(array2)
    print("After:",array2,"\n",isMinHeapPropertyTrue(array2))

    insert = 76
    print("Inserting into heap {insert}..")
    array2_return.insert(76)
    print(array2)

    print("Peeking into heap..")
    print(array2_return.peek())
    peeked = array2_return.peek()

    print(f"Removing {peeked} from the min heap")
    array2_return.remove()
    print(array2)

    print("Peeking into heap..")
    print(array2_return.peek())
    peeked = array2_return.peek()

    print(f"Removing {peeked} from the min heap")
    array2_return.remove()
    print(array2)

    print("Peeking into heap..")
    print(array2_return.peek())
    peeked = array2_return.peek()

    insert = 87
    print(f"Inserting into heap {insert}..")
    array2_return.insert(87)
    print(array2)

    print(f"Final Check of MinHeap Property:",isMinHeapPropertyTrue(array2))


    print("\n")