'''
The two sum problem is stated as follows: given an unsorted list and a number S, find all the pairs of numbers in that list such that their sum equals S.

For example, if the list is [3, 5, 2, -4, 8, 11][3,5,2,−4,8,11] and the value of S is 77, then the program should return pairs (11,-4)(11,−4) and (2,5)(2,5) 

since 11 +(-4)11+(−4) and 2+52+5 are equal to 77.

'''

def twoSumProblem(s,arr):
    sums = []
    hashtable= {}
    for i in range(0,len(arr)):
        result = s - arr[i]
        if result in hashtable:
            print("S is ",s,"and is : (",arr[i],',',result,")")
        hashtable[arr[i]] = arr[i]
        
num_arr=[3 , 5 , 2 , -4 , 8 ,11]
sum = 7

twoSumProblem(sum,num_arr) 