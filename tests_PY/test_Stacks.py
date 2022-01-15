import unittest

from Stacks import Stacks, dict_1, paranthesis_check

class test_Stacks(unittest.TestCase):
    def setUp(self):
        self.s1 = Stacks()
        for i in range(10,110,10):
            self.s1.push(i)
        
        self.par_true_case = '[](){([[[]]])}' #True Case
        self.par_false_case = '[(})' #Calse Case


    def test_pushStack(self):
        self.assertEqual([10,20,30,40,50,60,70,80,90,100],self.s1.items)

    def test_popStack(self):
        for i in range(1,6,1):
            self.s1.pop()
        self.assertEqual([10,20,30,40,50],self.s1.items)

    def test_sizeStack(self):
        self.assertEqual(10,self.s1.size())

        self.assertEqual(False,self.s1.isEmpty())
        for i in range(1,11,1):
            self.s1.pop()
        self.assertEqual(True,self.s1.isEmpty())


    def test_searchStack(self):
        self.assertEqual(True,self.s1.search(10))
        self.assertEqual(False,self.s1.search(110))

    def test_paranChecker(self):
        self.assertTrue(paranthesis_check(self.par_true_case))
        self.assertFalse(paranthesis_check(self.par_false_case))



    def tearDown(self):
        self.s1= None
        self.par_true_case = None
        self.par_false_case = None

if __name__ == "__main__":
    unittest.main()
