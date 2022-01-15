import unittest
from Queue import *
from LinkedList import LinkedList, removeDuplicatesFromLinkedList, Node

class test_LinkedLists(unittest.TestCase):
    def setUp(self):
        self.input_array1 = [1, 3, 3, 4, 4, 4, 5, 6, 6]

        self.input_array2 = [-2, -2, 3,- 4, -4, -4, 5,]       
        self.input_array1_NOrepeats = [1,3,4,5,6]
        self.input_array2_NOrepeats = [-2,3,-4,5]
        self.LL_1 = LinkedList(self.input_array1[0]).addMany(self.input_array1[1:])
        self.LL_2 = LinkedList(self.input_array2[0]).addMany(self.input_array2[1:])
        self.dfs_output = ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']
        self.bfs_output = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]

        self.graph = Node("A")
        self.graph.addChild("B").addChild("C").addChild("D")
        self.graph.children[0].addChild("E").addChild("F")
        self.graph.children[2].addChild("G").addChild("H")
        self.graph.children[0].children[1].addChild("I").addChild("J")
        self.graph.children[2].children[0].addChild("K")

        print("\n======= TREE ============")
        print("""          A         """)
        print("""        / |  \      """)
        print("""       B  C  D     """)
        print("""      / \   /  \   """)
        print("""     E   F  G    H  """)
        print("""    /        \       """)
        print("""   I          J   \n""")


    def test_createLL(self):
        self.assertEqual(self.input_array1,self.LL_1.getNodesInArray())
        self.assertEqual(self.input_array2,self.LL_2.getNodesInArray())

    def test_remoteDuplicates(self):
        self.output1 = removeDuplicatesFromLinkedList(self.LL_1)
        self.output2 = removeDuplicatesFromLinkedList(self.LL_2)

        self.assertEqual(self.input_array1_NOrepeats,self.output1.getNodesInArray())
        self.assertEqual(self.input_array2_NOrepeats,self.output2.getNodesInArray())

    def test_dfsOutputArray(self):
        self.assertEqual(self.dfs_output,self.graph.depthFirstSearch([]))

    def test_breadbreadthFirstSearch(self):
        self.assertEqual(self.bfs_output,self.graph.breadthFirstSearch([]))

    def tearDown(self):
        self.input_array1_NOrepeats = None
        self.input_array1 = None
        self.input_array2_NOrepeats = None
        self.input_array2 = None
        self.graph = None
        self.dfs_output = None
        self.output1 = None
        self.output2 = None 


if __name__ == "__main__":
    unittest.main()
