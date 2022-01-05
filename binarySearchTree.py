import array as arr


class BST():
    nodeCount = 0 # Track size of the tree

    def __init__(self,value= None):
        self.value = value
        self.left = None
        self.right = None


    def insert(self,value):
        
        if value < self.value: #Go left until you hit a leaf with none
            if self.left == None:
                self.nodeCount +=1
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right == None:
                self.right = BST(value)
                self.nodeCount +=1
            else:
                self.right.insert(value)
        return self



    def remove(self,value, parent = None):
        if value< self.value:
            self.left.remove(value,self)
        elif value > self.value:
            self.right.remove(value,self)
        else:
            if self.left and self.right: #Both child nodes present
                self.value = self.right.findMinValue() #Smallest value in right most tree
                self.right.remove(self.value,self)
            elif parent is None:
                if self.left is not None:
                    self.value = self.left.value
                    self.right = self.left.right
                    self.left = self.left.left
                elif self.right is not None:
                    self.value = self.right.value
                    self.left = self.right.left
                    self.right = self.right.right
                else:
                    pass
            elif parent.left == self:
                parent.left = self.left if self.left is not None else self.right
            elif parent.right ==self:
                parent.right = self.left if self.left is not None else self.right

        
        return self


            

    def findMinValue(self):
        if self.left is None:
            return self.value
        else:
            return self.left.findMinValue() 


    def contains(self,value):

        if value < self.value:
            if self.left is None:
                print(f"Search result NOT Found: {value}!")
                return False
            else:
                self.left.contains(value)
        elif value > self.value: 
            if self.right is None:
                return False
            else:
                self.right.contains(value)
        else:
            return True



def inOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return
    inOrderTraverse(tree.left,array)
    array.append(tree.value)
    print(tree.value,end=" ")
    inOrderTraverse(tree.right,array)
    

def preOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return
    array.append(tree.value)
    print(tree.value,end=" ")
    preOrderTraverse(tree.left,array)
    preOrderTraverse(tree.right,array)

def postOrderTraverse(tree, array):
    # Write your code here.
    if tree is None:
        return
    postOrderTraverse(tree.left,array)
    postOrderTraverse(tree.right,array)
    array.append(tree.value)
    print(tree.value,end=" ")


# @classmethod:
def validateBSTHelper(tree,Min,Max,LeftOrRight):
    #Start with min,max = -inf,+inf for root node
    #For left move: update Max
    #For right move: udpate Min
    #If Tree is none, (leaf node) return true
    # print(LeftOrRight)
    if tree is None:
        return True
    elif tree.value< Min or tree.value > Max:
        return False
    else:
        return validateBSTHelper(tree.left,Min, tree.value,"Left Tree") and validateBSTHelper(tree.right,tree.value,Max,"Right Tree")

    

# @classmethod
def validateBST(tree):
    return validateBSTHelper(tree,float("-inf"),float("inf"),"Start")

    # self.left.validateBSTHelper(self.value,max)
  


  




if __name__ == "__main__":

    b1 = BST(10)
    b1.insert(5)
    b1.insert(15)
    b1.insert(13)
    b1.insert(22)
    b1.insert(12)
    b1.insert(14)
    b1.insert(2)
    b1.insert(1)

    # self.assertTrue(b1.contains(1))
    # self.assertTrue(b1.contains(14))

    # b1.remove(22)
    # self.assertFalse(b1.contains(22))


#      10
#     /    \
#    5      15
#   /  \    /  \
#  2    5  13   22
# /          \
# 1          14

#Remove  =10