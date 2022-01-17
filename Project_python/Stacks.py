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
    
            	
if __name__ == "__main__":
    s1 = Stacks()
    # unittest.main()
    par_1 = '[](){([[[]]])}'


    print(paranthesis_check(par_1))

    par_2 = '[]('


    print(paranthesis_check(par_2))
    print("\n")