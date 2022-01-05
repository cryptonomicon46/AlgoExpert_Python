from types import NoneType
import unittest
from binarySearchTree import *
import array as arr

class test_BST(unittest.TestCase):
    def setUp(self):
        self.InOrder_array = arr.array("i",[1, 2, 5, 5, 10, 13, 14, 15, 22]) #Integer arrray for inorder or ASCENDING order
        self.PreOrder_array = arr.array("i",[10,5,2,1,5,15,13,14,22]) #Integer arrray for preorder 
        self.PostOrder_array = arr.array("i",[1,2,5,5,14,13,22,15,10]) #Integer arrray for preorder 
        self.PreCheck_array = arr.array("i",[]) #Empty Array for checking
        self.PostCheck_array = arr.array("i",[]) #Empty Array for checking
        self.InCheck_array = arr.array("i",[]) #Empty Array for checking

        self.test_return = False
        self.root1 = BST(10)
        self.root1.left = BST(5)
        self.root1.left.left = BST(2)
        self.root1.left.left.left = BST(1)
        self.root1.left.right = BST(5)
        self.root1.right = BST(15)
        self.root1.right.left = BST(13)
        self.root1.right.left.right = BST(14)
        self.root1.right.right = BST(22)
    #      root1 (follows BST variant)
    #       10
    #     /     \
    #     5      15
    #    / \     /  \
    #   2   5  13   22
    #  /        \  
    # 1          14

        # print(validateBST(root1))
    

        self.root2 = BST(10)
        self.root2.left = BST(5)
        self.root2.left.left = BST(2)
        self.root2.left.left.left = BST(1)
        self.root2.left.right = BST(5)
        self.root2.right = BST(15)
        self.root2.right.left = BST(13)
        self.root2.right.left.right = BST(14)
        self.root2.right.right = BST(11)

    #     self.root2 (doesn't follow BST invariant)
    #       10
    #     /     \
    #     5      15
    #    / \     /  \
    #   2   5  13   11
    #  /        \  
    # 1          14





    def tearDown(self):
        self.root1 = None
        self.root2 = None
        self.InOrder_array = None
        self.PreOrder_array = None
        self.PostOrder_array = None
        self.test_return = None
        self.PreCheck_array = None
        self.PostCheck_array = None
        self.InCheck_array = None






    
    def test_InsertContains(self):
   
        self.test_contains = self.root1.contains(10)
        self.assertTrue(self.test_contains)
        self.test_contains = self.root1.contains(50)
        self.assertFalse(self.test_contains)
        self.root1.remove(22)
        self.test_contains = self.root1.contains(22)
        self.assertFalse(self.test_contains)



    def test_BSTValidate(self):
        self.assertTrue(validateBST(self.root1)) #root1 follows BST invariant 

        self.assertFalse(validateBST(self.root2)) #self.root2 doens't follow BST invariant


    def test_inOrderParse(self):
        inOrderTraverse(self.root1,self.InCheck_array)
        self.assertEqual(self.InCheck_array,self.InOrder_array)

    def test_preOrderParse(self):
        preOrderTraverse(self.root1,self.PreCheck_array)
        self.assertEqual(self.PreCheck_array,self.PreOrder_array)

    def test_postOrderParse(self):
        postOrderTraverse(self.root1,self.PostCheck_array)
        self.assertEqual(self.PostCheck_array,self.PostOrder_array)



if __name__ == "__main__":
    unittest.main()
