class LinkedList():
    def __init__(self,value):
        self.value = value
        self.next = None

    def addMany(self,values):
        #While loop to Traverse to the end of the current linked list
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedList(value)
            current = current.next
        return self
        

    def getNodesInArray(self):
        current = self
        output_array = []
        while current is not None:
            output_array.append(current.value)
            current = current.next
        return output_array


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    current = linkedList

    while current.next is not None:
        if current.value == current.next.value:
            current.next = current.next.next
        else:
            current = current.next
    return linkedList


class  Node:
    def __init__(self,name):
        self.name = name
        self.children = []

    def addChild(self,name):
        self.children.append(Node(name))
        return self
    
    def depthFirstSearch(self, array):
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)
        # else:
        return array
            


    # def depthFirstSearchHelper(self,array):


                
        # return array
        # Write your code here.pass

if __name__ == "__main__":
 
   # input_array = [1, 3,3,3, 4, 4, 4, 5, 6, 6]
    input_array = [3,3,4]
    ll_1 = LinkedList(1).addMany(input_array)
    list_1 = ll_1.getNodesInArray()
    ll_2 = removeDuplicatesFromLinkedList(ll_1)
    list_2 = ll_2.getNodesInArray()



    graph = Node("A")
    graph.addChild("B").addChild("C").addChild("D")
    graph.children[0].addChild("E").addChild("F")
    graph.children[2].addChild("G").addChild("H")
    graph.children[0].children[1].addChild("I").addChild("J")
    graph.children[2].children[0].addChild("K")

    dfs_array = graph.depthFirstSearch([])
    print("\n")
