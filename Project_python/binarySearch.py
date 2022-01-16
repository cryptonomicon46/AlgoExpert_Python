def binarySearch(array,target):
    return binarySearchHelper(0,len(array)-1,array,target)




def binarySearchHelper(left,right,array,target):
    mid = (left+right)//2
    if target == array[mid]:
        return mid
    elif target>array[mid]:
        left = mid+1
        return binarySearchHelper(left,right,array,target)
    elif target<array[mid]:
        right = mid-1
        return binarySearchHelper(left,right,array,target)



if __name__ == "__main__":
    array = [0, 1, 21, 33, 45, 45, 61, 71, 72, 73]
    target = 33
    indexFound = binarySearch(array,target)
    print("\n")