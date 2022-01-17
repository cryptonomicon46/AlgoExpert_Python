class MinHeap:
    def __init__(self,array):
        self.heap = self.buildHeap(array)

    def buildHeap(self,array):
        firstParent = (len(array)-2)//2
        for CurrentIdx in reversed(range(firstParent+1)):
            self.siftDown(CurrentIdx,len(array)-1,array)
        return array


    def siftDown(self,CurrentIdx,EndIdx,heap):
        childOneIdx = 2*CurrentIdx+1
        while childOneIdx < EndIdx:
            childTwoIdx = -1 if 2* CurrentIdx+2 >= EndIdx else 2*CurrentIdx+2
            if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
                IdxToSwap = childTwoIdx
            else:
                IdxToSwap = childOneIdx
            if  heap[CurrentIdx] > heap[IdxToSwap]:
                self.swap(CurrentIdx,IdxToSwap,heap)
                CurrentIdx = IdxToSwap
                childOneIdx = 2*CurrentIdx +1 
            else:
                break
    


    def siftUp(self,CurrentIdx,heap):
        ParentIdx = (CurrentIdx-1)//2
        while CurrentIdx >0 and self.heap[CurrentIdx]< self.heap[ParentIdx]:
            self.swap(CurrentIdx,ParentIdx,self.heap)
            CurrentIdx = ParentIdx
            ParentIdx = (CurrentIdx-1)//2
        return heap

    def peek(self):
        return self.heap[0]


    def remove(self):
        self.swap(0,len(self.heap)-1,self.heap)
        itemRemoved = self.heap.pop()
        self.siftDown(0,len(self.heap)-1,self.heap)
        return itemRemoved

    def lenM1(self,array):
        return len(array)-1

    def insert(self,item):
        self.heap.append(item)
        self.siftUp(len(self.heap)-1,self.heap)
    
    def swap(self,i,j,heap):
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