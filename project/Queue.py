class Queue():
    def __init__(self):
        self.items = []


    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) ==0

    def sizeOf(self):
        return len(self.items)


if __name__ == "__main__":

    q1 = Queue()
    for i in range(0,130,20):
        q1.enqueue(i)

    print("\n")

    