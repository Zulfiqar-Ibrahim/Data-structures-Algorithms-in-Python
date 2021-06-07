
class quickSort:
    """
    Quick Sort is considered very efficient Ds for sorting based on 
    divide and conquer strategy. 

    ...

    Atributes:

    ----------
    name:

    arr : array

        array contains values which are being sorted

    low : int 

        top left side of array
    
    left : int

        top right side of array 



    

    Methods:

    --------

    partition(self,value_a):

    this is the function written to find the partition index. 
    While dividing the array, the pivot element should be positioned in such a way that elements less than 
    pivot are kept on the left side and elements greater than pivot are on the right side of the pivot.

    quicksort_func(self,arr,low,high):

    Use recursion to find the pivot element. 
    


    """

    def __init__ (self,arr):

        self.arr=arr

    
    def partition_arr(self,arr,low,high):

        pivot=arr[high]

        i = low - 1

        for j in range(low, high):

            if self.arr[j] <= pivot:

                i= i + 1

                (self.arr[i],self.arr[j])=(self.arr[j],self.arr[i])

        (self.arr[i+1],self.arr[high])=(self.arr[high],self.arr[i+1])

        return i + 1

    def quicksort_func(self,arr,low,high):

        if low <= high:

            pi= self.partition_arr(self.arr,low,high)

            self.quicksort_func(self.arr,low,pi - 1)

            self.quicksort_func(self.arr,pi + 1, high)



arr=[1,8,9,2,5,7,3,0,6]
size=len(arr)
a1=quickSort(arr)
a1.quicksort_func(arr,0,size - 1)

print(arr)


                


