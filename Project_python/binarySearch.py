from gettext import find


def binarySearch(array,target):
    return binarySearchHelper(0,len(array)-1,array,target)




def binarySearchHelper(left,right,array,target):
    mid = (left+right)//2
    if left >right:
        return -1
    if target == array[mid]:
        return mid
    elif target>array[mid]:
        left = mid+1
        return binarySearchHelper(left,right,array,target)
    elif target<array[mid]:
        right = mid-1
        return binarySearchHelper(left,right,array,target)

def findThreeLargestNumbers(array):
    threeGreatest = [None]*3
    for item in array:
        checkThreeGreatest(threeGreatest,item)
    return threeGreatest

def checkThreeGreatest(threeGreatest,target):
    if threeGreatest[2] is None or target > threeGreatest[2]:
        helperFunction(threeGreatest,target,2)
    elif threeGreatest[1] is None or  target > threeGreatest[1]:
        helperFunction(threeGreatest,target,1)
    elif threeGreatest[0] is None or  target > threeGreatest[0]:
        helperFunction(threeGreatest,target,0)


def helperFunction(array,target,location):
    for i in range(location+1):
        if i == location:
            array[i]= target
        else:
            array[i] = array[i+1]

if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 100
    indexFound = binarySearch(array,target)


    arr2 = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]

    result_arr2_chk = [18,141,541]
    # result = checkThreeGreatest(result_arr2,200)
    result_arr2_out = findThreeLargestNumbers(arr2)

    arr3 = [55, 43, 11, 3, -3, 10]
    print(findThreeLargestNumbers(arr3))
    print("\n")