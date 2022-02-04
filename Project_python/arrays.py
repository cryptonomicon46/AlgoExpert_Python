#For each number in the array, check if another number other than itself adds up to targetSum
#Return [number,otherNumber] if found else return [] empty array

#O(n) time and Space?
def twoNumberSum(array,targetSum):
    arr_hash = {k:v for k,v in enumerate(array)}
    return_arr =[]
    for number in array:
        return_arr.append(number)
        delta = targetSum- number
        if delta in arr_hash.values() and delta != number:
            return_arr.append(delta)
            break
        else:
            return_arr.pop()
    return return_arr



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

import functools
from venv import create

def nonConstructibleChange_fails(coins):
    # Write your code here
    if len(coins) <=1:
        return 1
    coins.sort() #Sort in ascending order
    coinsSum = functools.reduce(lambda a,b : a+b,coins[:-1])

    if coinsSum+1 < coins[-1]:
        return coinsSum+1
    elif coins[0]== coins[-1]:
        return coins[0]+1
    else:
        return coinsSum+ coins[-1] +1
 

def nonConstructibleChange(coins):
    createChange = 0
    coins.sort()

    for coin in coins:
        # print(coin)
        if coin > createChange+1:
            return createChange +1
        createChange+= coin

    return createChange+1 

    



    




def TripletSum(array,targetSum):
    pass

def QuadrapuleSum(array,targetSum):
    pass


if __name__ == "__main__":
    array = [3, 5, -4, 8, 11, 1, -1, 6] #x
    targetSum = 10 
    #Result = [11,-1]
    #Find 'y' such that y = 10-x



    print(twoNumberSum(array,targetSum))


    array1 = [5, 1, 22, 25, 6, -1, 8, 10]
    sequence = [1, 6, -1, 10]
    print(isValidSubsequence(array1,sequence))


    input = [1, 2, 3, 5, 6, 8, 9]
    expected = [1, 4, 9, 25, 36, 64, 81]
    print(sortedSquaredArray([-5, -4, -3, -2, -1]))
    print(sortedSquaredArray([-10, -5, 0, 5, 10]))

    competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
    results = [0, 0, 1]

    tournamentWinner(competitions, results)
  

    coins = [5, 7, 1, 1, 2, 3, 22]
    print(nonConstructibleChange(coins)) #20
    print(nonConstructibleChange([1, 5, 1, 1, 1, 10, 15, 20, 100])) #55
    print(nonConstructibleChange([87])) #1 
    print(nonConstructibleChange([5, 6, 1, 1, 2, 3, 4, 9])) #32
    print(nonConstructibleChange([1,1,1,1,1])) #6

    print("\n")