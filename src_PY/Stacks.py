class Stacks():
    def __init__(self):
        self.items = []
    
    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


    def isEmpty(self):
        return self.items == []
    
    def search(self,item):
        return item in self.items

    def __repr__(self):
        return self.items

    def __str__(self):
        return self.__repr__()


dict_1 = {"<":">",
        "{":"}",
        "(":")",
        "[":"]"}

def paranthesis_check(paranthesis_chk):   
    s1 = Stacks()
    for item in paranthesis_chk:
        if item in dict_1.keys():
             #left brackets
            s1.push(item);
        elif  s1.isEmpty() or dict_1[s1.pop()] != item:
            return False
    return s1.isEmpty() == True
    #self.push(item)
    
def bubbleSort(input_array):
    # Write your code here.
	Sorted = False
    counter=0
    # output_array = []
	while(not Sorted):
		for i in range(0,len(input_array)-1-counter):
			if (input_array[i] > input_array[i+1]):
				swap(i,i+1,input_array)
				Sorted = False
			else: 
				Sorted = True
        counter -=1
	return input_array
	
            


def swap(i,j,input_array):
    temp = input_array[i]
    input_array[i]= input_array[j]
    input_array[j] = temp 
	
if __name__ == "__main__":
    s1 = Stacks()
    # unittest.main()
    par_1 = '[](){([[[]]])}'


    print(paranthesis_check(par_1))

    par_2 = '[]('


    print(paranthesis_check(par_2))
    print("\n")