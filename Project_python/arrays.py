#For each number in the array, check if another number other than itself adds up to targetSum
#Return [number,otherNumber] if found else return [] empty array

#O(nlon) time |  O(1) space


#x+y = targetSum
#y = targetSum -x 

#O(nlogn) time || O(n) space
from audioop import reverse
from curses import start_color
from tkinter import S
from turtle import right


def twoNumberSum(array,targetSum):
    array.sort()  #log(n) time
    idx_L = 0
    idx_R = len(array)-1
    twoSumResult = []
    while (idx_L < idx_R): #n time 
        if array[idx_R] == targetSum - array[idx_L]:
            return [array[idx_L], array[idx_R]]
        elif  targetSum - array[idx_L] > array[idx_R]:
            idx_L+=1
        else:
            idx_R-=1

    return twoSumResult #nlog(n) time



#threeNumberSum Function
#Input: Non-empty array of integers , target sum.
#Output: triplets that sum up to targetSum
        # each sorted in ascending order, 
        # whole triplet sorted in ascending order
        # else return empty array 

# O(n*n) time || O(n) space
def threeNumberSum(array,threeSum):
    threeSumArray = []
    array.sort()
    for i in range(len(array)-2):
        idx_L = i+1
        idx_R = len(array)-1

        while(idx_L < idx_R):
            left = array[idx_L]
            num = array[i]
            right = array[idx_R]
       
            sumOfThree = num + left + right 
            if sumOfThree > threeSum:
                idx_R-=1
                # right = array[idx_R]
            elif sumOfThree < threeSum:
                idx_L+=1
                # left = array[idx_L]
            else:
                threeSumArray.append([num,array[idx_L],array[idx_R]])
                idx_L+=1
                idx_R-=1
        
    return threeSumArray





#Check if 'sequence' is a subarray of 'array'
#O(n) time and O(1) space
def isValidSubsequence(array, sequence):
    # Write your code here.
    while(array):
        number_to_check= array.pop()
        if not sequence:
            break
        elif sequence[-1] == number_to_check:
            sequence.pop()

    return len(sequence) == 0

#Return squares in same order as input array
#O(n) time || O(n) space where n is space for the squaredList
def sortedSquaredArray(array):
    # Write your code here.
    if len(array)>0:
        squaredList=[i*i for i in array]
        squaredList.sort() #Sorts in place can also be sorted(squaredList)
        return squaredList
    else:
        return []



    # competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    # results = [0, 0, 1]
    # winner = 'Python'

def tournamentWinner(competitions, results):
    # Write your code here.
    i = 0
    dict_scores= {}
    while i<len(results):
        if results[i]==0:
            print(f"{competitions[i][1]} beats {competitions[i][0]}", end = ",")  
            dict_scores = updateScoring(competitions[i][1],competitions[i][0],dict_scores)
        else:
             print(f"{competitions[i][0]} beats {competitions[i][1]}",end =",")
             dict_scores = updateScoring(competitions[i][0],competitions[i][1],dict_scores)

        i+=1
    print("\n")
    for k,v in dict_scores.items():
        print(f"{k} - {v} points ")

    return max(dict_scores, key = dict_scores.get)
    

def updateScoring(team1, team2,dict_scores):
    if team1 in dict_scores:
        dict_scores[team1] = dict_scores[team1]+3
    else:
        dict_scores[team1] =3
    if team2 in dict_scores:
        dict_scores[team2] = dict_scores[team2]+0
    else:
        dict_scores[team2] =0
    return dict_scores


 #nlog(n) Time from coins.sort() | O(1) space
def nonConstructibleChange(coins):
    createChange = 0
    coins.sort()

    for coin in coins:
        # print(coin)
        if coin > createChange+1:
            return createChange +1
        createChange+= coin

    return createChange+1 

    
#Find a pair of numbers one from each array with absolute difference closest to 0
#O(N*M + log(N) + log(M)) time || O(1) space
#Using nested For loops
def smallestDifferenceFor(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort() # log(N) time
    arrayTwo.sort() #log(M) time
    delta = float('inf')
    smallestDiff = []
    for numOne in arrayOne: #Time N 
        for numTwo in arrayTwo:  #Time M 
            # delta = abs(numOne- numTwo)
            if numTwo-numOne == 0:  
                return [numOne,numTwo]
            elif delta > abs(numOne- numTwo):
                delta = abs(numTwo- numOne)
                smallestDiff = [numOne,numTwo]
    return smallestDiff


#Using While loop
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort() # Nlog(N) quick sort time
    arrayTwo.sort() #Mlog(M) quick sort time
    currentDelta = float('inf')
    smallestDelta = float('inf')
    smallestDiff = []
    idx_One = 0
    idx_Two = 0
    #Time N+M 
    while (idx_One <len(arrayOne)) and (idx_Two < len(arrayTwo)):
        numOne = arrayOne[idx_One]
        numTwo = arrayTwo[idx_Two]
    
        if numOne < numTwo:
            currentDelta = numTwo- numOne
            idx_One+=1
        elif numTwo < numOne:
            currentDelta = numOne - numTwo
            idx_Two+=1
        else:
            return [numOne, numTwo]
        if smallestDelta >= currentDelta:
            smallestDelta = currentDelta
            smallestDiff = [numOne, numTwo]

    return smallestDiff
    #Total Time = {N*log(N) + M*log(M) + M+N} 
    # ~= {N*log(N) + M*log(M)}  
    

#Move all instances of 'toMove' in 'array' to the end of the array , mutate in place 
#O(n) Time | O(1) Space
def moveElementToEnd1(array, toMove):
    # Write your code here.
    idx = 0
    loopCounter = 0 
    while (loopCounter < len(array)):
        numToCheck = array[idx]
        if numToCheck == toMove:
            itemPopped = array.pop(idx)
            array.append(itemPopped)
            idx=0
        loopCounter +=1
        idx=1

    return array



def moveElementToEnd(array, toMove):
    # Write your code here.
    idx_L = 0
    idx_R = len(array)-1
    while (idx_L < idx_R):
        while (idx_L< idx_R and array[idx_R] == toMove):
            idx_R-=1
        if array[idx_L] == toMove:
            array[idx_L],array[idx_R] = array[idx_R], array[idx_L]
        idx_L+=1

    return array


#Check if array is monotonic, non-increasing or Monotonic non-decreasing
# O(n) time || O(1) space 
def isMonotonic1(array):
    # Write your code here.
    idx_L = 0
    idx_R = len(array)-1
    delta = 0 
    if len(array)<=1:
        return True
    
    if array[idx_L] > array[idx_R]:
        while (idx_L < idx_R):
            delta = array[idx_L]- array[idx_L+1]
            if delta <0:
                return False
            idx_L+=1
    else:
        while (idx_L < idx_R):
            delta = array[idx_L+1]- array[idx_L]
            if delta <0:
                return False
            idx_L+=1

    return True


def isMonotonic(array):
    nonDecreasing = True
    nonIncreasing = True

    for i in range(1,len(array)):
        if array[i]> array[i-1]:
            nonDecreasing = False
        if array[i] < array[i-1]:
            nonIncreasing = False
    return nonDecreasing or nonIncreasing


def spiralTraverse(array):
    # Write your code here.
    SpiralArray =[]
    startRow,endRow = 0,len(array)-1
    startCol, endCol = 0, len(array[0])-1
   
    while startRow<= endRow and startCol <= endCol:
        
        for col in range(startCol,endCol+1):
            SpiralArray.append(array[startRow][col])

        for row in range(startRow+1, endRow+1):
            SpiralArray.append(array[row][endCol])
        
        for col in reversed(range(startCol,endCol)):
            if startRow== endRow:
                break
            SpiralArray.append(array[endRow][col])

        for row in reversed(range(startRow+1,endRow)):
            if startCol== endCol:
                break
            SpiralArray.append(array[row][startCol])

        startRow+=1
        endRow-=1
        startCol+=1
        endCol-=1

    return SpiralArray

    

def longestPeak(array):
    # Write your code here.
    longestPeakCount = 0 
    currentLongestPeak = 0 
    i = 0 


    while i < len(array):

       
        if not (array[i]>array[i-1] and array[i]>array[i+1]):
            i+=1
            continue
        else:
            leftIdx = i-2
            while (leftIdx >=0 and array[leftIdx]<array[leftIdx+1]):
                leftIdx-=1
            rightIdx = i+2
            while (rightIdx< len(array) and array[rightIdx]<array[rightIdx-1]):
                rightIdx+=1
            currentLongestPeak = rightIdx-leftIdx-1
            longestPeakCount = max(longestPeakCount,currentLongestPeak)

            i=rightIdx

    return longestPeakCount


      def arrayOfProducts(array):
            # Write your code here.
    pass


if __name__ == "__main__":


    #Two Number Sum
    #Find 'y' such that y = 10-x
    array = [3, 5, -4, 8, 11, 1, -1, 6] #x
    targetSum = 10 
    #Result = [11,11]

    print(twoNumberSum(array,targetSum))
    


    #Valid Sub Sequence 
    array1 = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array1,sequence))


    #Sorted Squared Array
    input = [1, 2, 3, 5, 6, 8, 9]
    expected = [1, 4, 9, 25, 36, 64, 81]
    print(sortedSquaredArray([-5, -4, -3, -2, -1]))
    print(sortedSquaredArray([-10, -5, 0, 5, 10]))

    #Tournement Winner
    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]
    print(tournamentWinner(competitions, results))
  


    #Non Constructible Change
    coins = [5, 7, 1, 1, 2, 3, 22]
    print(nonConstructibleChange(coins)) #20
    print(nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100])) #55
    print(nonConstructibleChange([87])) #1 
    print(nonConstructibleChange([5, 6, 1, 1, 2, 3, 4, 9])) #32
    print(nonConstructibleChange([1,1,1,1,1])) #6


    #ThreeSum test 
    numbers = [12, 3, 1, 2, -6, 5, -8, 6]
    targetSum= 0 
    results = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    print(threeNumberSum(numbers,targetSum))


    #Smallest difference
    arrayOne = [-1, 5, 10, 20, 28, 3]
    arrayTwo = [26, 134, 135, 15, 17]
    #smallestDiff = [28,26] #Answer
    print(smallestDifference(arrayOne,arrayTwo))


    #Move Elements to the end 
    array = [2, 1, 2, 2, 2, 3, 4, 2]
    toMove = 2
    print(moveElementToEnd(array,toMove))


    #Is Monotonic Array
    array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
    array2= [1]
    array3 = [1, 5, 10, 1100, 1101, 1102, 9001]
    array4 = [1, 2, 0] #Fail
    array5 = [1, 1, 1, 2, 3, 4, 1] #Fail
    array6 = [-1, -5, 10]
    print(isMonotonic(array6))


    #Spiral Traverse

    matrix = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
    matrix1= [
    [1, 2, 3, 4],
    [12, 13, 14, 5],
    [11, 16, 15, 6],
    [10, 9, 8, 7]
    ]
    matrix2= [
    [1, 2, 3],
    [8, 9, 4],
    [7, 6, 5]
  ]
    print(spiralTraverse(matrix2))

    #Longest Peak

    array =  [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
    array2 = [5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10]
    array3 = [1, 2, 3, 4, 5, 1]
    print(longestPeak(array3))
    print("\n")


