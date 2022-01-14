import array as arr



class BST():
    def __init__(self,value= None):
        self.value = value
        self.left = None
        self.right = None


    def insert(self,value):
        
        if value < self.value: #Go left until you hit a leaf with none
            if self.left == None:
                # self.nodeCount +=1
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right == None:
                self.right = BST(value)
                # self.nodeCount +=1
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
#Construct a BST with Min height from an inOrderArray as input

def minHeightBst(array):
    return minHeightHelperFunction(array,None)

def minHeightHelperFunction(array,root):
    if len(array)==0:
        return
    mid = len(array)//2
    valueToAdd = array[mid]

    if root is None:
        root = BST(valueToAdd)
    else:
        root.insert(valueToAdd)

    minHeightHelperFunction(array[0:mid],root)
    minHeightHelperFunction(array[1+mid:],root)
    return root
    
def maxTreeHeight(root):
    if root is None:
        return 0 
    else:
        h = max (maxTreeHeight(root.left),maxTreeHeight(root.right)) +1
    return h






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

    
def findClosestValueInBst(tree, target):
    # Move right


    if tree.right and tree.left:
        if target> tree.value or abs(target-tree.right.value)< abs(target-tree.left.value):
            new_target = findClosestValueInBst(tree.right, target)
        elif target< tree.value or abs(target-tree.left.value)< abs(target-tree.right.value):
            new_target = findClosestValueInBst(tree.left, target)
    elif (target < tree.value and tree.left is None) or (target> tree.value and tree.right is None):
        new_target = tree.value
    return new_target
    


    
    

        



		


# This is the class of the input tree. Do not edit.
class BST_1:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# @classmethod
def validateBST(tree):
    return validateBSTHelper(tree,float("-inf"),float("inf"),"Start")

    # self.left.validateBSTHelper(self.value,max)
  


  




if __name__ == "__main__":

    b2 = BST(10)
    b2.insert(5)
    b2.insert(15)
    b2.insert(13)
    b2.insert(22)
    b2.insert(14)
    b2.insert(2)
    b2.insert(1)

    # self.assertTrue(b2.contains(1))
    # self.assertTrue(b2.contains(14))

    # b2.remove(22)
    # self.assertFalse(b2.contains(22))

    print(findClosestValueInBst(b2,12))

    array = [1, 2, 5, 7, 10, 13, 14, 15, 22] #inOrder Traversal
    bst_return = minHeightBst(array)
    

    b2 = BST(10)
    b2.insert(5)
    b2.insert(15)
    b2.insert(13)
    b2.insert(22)
    b2.insert(14)
    b2.insert(2)
    array2 = []
    inOrderTraverse(b2,array2)
    array2 = []
    postOrderTraverse(b2,array2)
    array2 = []
    preOrderTraverse(b2,array2)

    height = maxTreeHeight(b2)
    print("\n")
#      10
#     /    \
#    5      15
#   /  \    /  \
#  2    5  13   22
# /          \
# 1          14

#Remove  =10