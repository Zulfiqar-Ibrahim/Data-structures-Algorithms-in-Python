
class Recursive:    
    """ 

    In this we will use Divide & Conquere  strategy for the solution of problems. Recursive functions play very
    important role in the D&C technique.

    ...

    Atributes:

    ----------
    name:

    value_a : int

        Base case for recursion

    number : int 

        key value to be searched.
    low : int

        lowest left side of array

    high : int

        higher right side of array

    Methods:

    --------

    recursive(self,value_a):

    This funtion is written to decrementing numbers from starting numbers
    using recursive method. This methad keep calling itself untill it reaches
    boundry. Print() will be called n times. O(n) is time complexity of this recursive function


    binary_search_iterative_method(self,number):

    This is the iterative method of binary search. First condition of B.S is that list must be in 
    orted form. Binary search algorithm is following the D & C strategy 

    binary_search_recursive_method(self,low , high, k):

    This is the Recursive method of binary search. First condition of B.S is that list must be in 
    sorted form. Binary search algorithm is following the D & C strategy.

    



    """

    def __init__(self,number):
        print('object crafted')
        self.value_a=number
        list_numbers=[3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
        self.low=0
        self.high=len(list_numbers)-1
        self.recursive(self.value_a)
        self.binary_search_recursive_method(self.low,self.high,number)

    def recursive(self,value_a):
        """
        [This funtion is written to decrementing numbers from starting numbers
        using recursive method. This methad keep calling itself untill it reaches
        boundry. Print() will be called n times. O(n) is time complexity of this recursive function]

        """

        #print(value_a)
        if value_a > 0:
            print(value_a, end=',')

            self.recursive(value_a-1)
        else:
            return 0
    def binary_search_iterative_method(self,number):
        """[This is the iterative method of binary search. First condition of B.S is that list must be in 
        sorted form. Binary search algorithm is following the D & C strategy ]
        """
        list_numbers=[3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]
        low=0
        high=len(list_numbers)-1
        mid=0
        
        while low <= high:


            mid=(low+high)//2
            value=list_numbers[mid]
            if value < number:
                
                low=mid+1

            elif value > number:

                high=mid-1
            
            else:
                
                print(' index of number ',mid, 'value ',list_numbers[mid])
                return mid
        return -1

    def binary_search_recursive_method(self, low , high, k):
        """[This is the Recursive method of binary search. First condition of B.S is that list must be in 
        sorted form. Binary search algorithm is following the D & C strategy ]
        """

        list_numbers=[3,6,8,12,14,17,25,29,31,36,42,47,53,55,62]

        if low == high:

            if list_numbers[low]==k:

                print('index found at ' , k)

                return k

            else:
                print('No element found',end=',')
                return 0
        else:

            mid = (low + high ) // 2

            if list_numbers[mid] == k:

                print('index found at ' , mid)

                return mid 

            elif k < list_numbers[mid]:

                return self.binary_search_recursive_method(low,mid-1,k)

            elif k > list_numbers[mid]:

                return self.binary_search_recursive_method(mid+1,high,k)
        






            




                



re=Recursive(29)
index_iterative=re.binary_search_iterative_method(29)
if index_iterative == -1:
    print('no value is being found in  terative method', end=',')
    
else:
    print('index of found element in iterative method ',index_iterative , end=',')


