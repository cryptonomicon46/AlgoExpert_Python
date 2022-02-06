import unittest
from arrays import *

class test_arrays(unittest.TestCase):
    def setUp(self):
        self.array1= [3, 5, -4, 8, 11, 1, -1, 6]
        self.targetSum1= 10
        self.result1 = [11,-1]


    

    def tearDown(self):
        self.array1 = None
        self.targetSum1 = None




    def test_twoNumberSum(self):
        self.assertEqual([-1,11],twoNumberSum(self.array1,self.targetSum1))
        self.assertEqual([4,6],twoNumberSum([4,6],10))
        self.assertEqual([1,4],twoNumberSum([4,6,1],5))
        self.assertEqual([-3,6],twoNumberSum([4,6,1,-3],3))
        self.assertEqual([8,9],twoNumberSum([1,2,3,4,5,6,7,8,9],17))
        self.assertEqual([3,15],twoNumberSum([1,2,3,4,5,6,7,8,9,15],18))
        self.assertEqual([-5,0],twoNumberSum([-7, -5, -3, -1, 0, 1, 3, 5, 7],-5))
        self.assertEqual([],twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6],15))
        self.assertEqual([],twoNumberSum([14],15))
        self.assertEqual([],twoNumberSum([15],15))


    def test_createSum(self):
        self.assertEqual(20,nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
        self.assertEqual(55,nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100]))
        self.assertEqual(1,nonConstructibleChange([87]))
        self.assertEqual(32,nonConstructibleChange([5, 6, 1, 1, 2, 3, 4, 9]))
        self.assertEqual(6,nonConstructibleChange([1,1,1,1,1])) #6
    
    def test_tournament(self):
        self.competitions1 = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        self.results1 = [0, 0, 1]
        self.assertEqual('Python',tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]],[0, 0, 1])) 


    def test_threeNumberSum(self):
        pass





if __name__ == "__main__":
    unittest.main()