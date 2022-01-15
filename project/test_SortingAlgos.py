import unittest
from SortingAlgorithms import *

class test_SortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.input_array1 =  [8,5,2,9,5,6,3] 
        self.sorted_array1 = [2,3,5,5,6,8,9]

        self.input_array2 =  [8,5,2,9,5,6,3,-1,-3,0,-4] 
        self.sorted_array2 = [-4,-3,-1,0,2,3,5,5,6,8,9]



    def test_bubbleSort(self):
        self.assertEqual(self.sorted_array1,bubbleSort(self.input_array1))
        self.assertEqual(self.sorted_array2,bubbleSort(self.input_array2))



    def tearDown(self) -> None:
        self.input_array = None
        self.sorted_array2 = None



if __name__ == "__main__":
    unittest.main()