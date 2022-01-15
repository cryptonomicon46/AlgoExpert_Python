# def bubbleSort(input_array):
#     # Write your code here.
# 	Sorted = False
#     counter=0
#     # output_array = []
# 	while(not Sorted):
# 		Sorted = True
# 		for i in range(0,len(input_array)-1-counter):
# 			if (input_array[i] > input_array[i+1]):
# 				swap(i,i+1,input_array)
# 				Sorted = False
#         counter +=1
# 	return input_array
	
            
def bubbleSort(input_array):
    Sorted = False
    Counter = 0
    while(not Sorted):
        Sorted = True
        for i in range(0,len(input_array)-1-Counter):
            if input_array[i]> input_array[i+1]:
                swap(i,i+1,input_array)
                Sorted = False
        Counter +=1
    return input_array


def swap(i,j,input_array):
    input_array[i],input_array[j] = input_array[j],input_array[i]


if __name__ == "__main__":
    input_array = [8, 5, 2, 9, 5, 6, 3] 

    print(bubbleSort(input_array))

    input_array2 =  [8,5,2,9,5,6,3,-1,-3,0,-4] 
    print(bubbleSort(input_array2))

    print("\n")
