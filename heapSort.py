class heapsort:
    """
    Heap Sort is a popular and efficient sorting algorithm in computer programming.

    Atributes:

    ----------
    name:

    arr : int

        arry containing numbers which are to be sorted.

    
    Methods:

    --------

    def heapify(self,arr,size_arr,location_arr):

    This method involves recursion where we replace child nodes with root to maintain max heap property

    
    def heapsort():

    Contains heapify recursion function which will swap the largest child node with root node until
    max heap tree (base case)




    """
    def __init__(self,arr):
        self.arr=arr

    def heapify(self,arr,size_arr,location_arr):
        """
        This method involves recursion where we replace child nodes with root to maintain max heap property


        Args:
            arr ([int]): [array contains the numbers which are to be sorted]
            size_arr ([int]): [size of array]
            location_arr ([int]): [location of value]
        """
        
        largest=location_arr 
        left_number = 2 * location_arr + 1
        right_number = 2 * location_arr +2

        if left_number < size_arr and arr[location_arr] < arr[left_number]:

            largest=left_number

        if right_number < size_arr and arr[largest] < arr[right_number]:

            largest=right_number

        if largest != location_arr:

            arr[location_arr], arr[largest] = arr[largest], arr[location_arr]

            self.heapify(arr,size_arr,largest)

    def heapsort(self):

        """[Use looping through i-th recursive function]
        """
        size_arr=len(self.arr)

        for i in range(size_arr//2, -1, -1):

            self.heapify(self.arr,size_arr,i)

        for i in range(size_arr-1, 0, -1):
            
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]

            self.heapify(self.arr, i, 0)


arr = [3,4,9,1,4,8,10,0,5,7]  
a1=heapsort(arr)

a1.heapsort()

print(arr)


    



