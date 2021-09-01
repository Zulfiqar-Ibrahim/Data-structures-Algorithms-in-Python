class priorityQueue:


    def __init__(self):
        self.myList=[]

    def heapify(self, arr, n, i ):

        largest = i

        left = 2 * i + 1

        right = 2 * i + 2

        if left < n and arr[i] < arr[left]:

            largest = left

        if right < n and arr[i] < arr[right]:

            largest = right
        
        if largest != i:

            arr[i],arr[largest] = arr[largest],arr[i]

            self.heapify(arr, n, largest)

    def insert (self, arr, newNum):

        size = len(arr)

        if size == 0:
            arr.append(newNum)

        else: 
            arr.append(newNum)
            for i in range((size//2) - 1, -1, -1):
                self.heapify(arr, size, i)
    def deleteNode(self, array, num):

        size = len(array)

        i = 0

        for i in range(0, size):

            if num == array[i]:

                break

        array[i], array[size - 1] = array[size - 1], array[i]

        array.remove(size - 1)

        for i in range((len(array) // 2) - 1, -1, -1):

            self.heapify(array, len(array), i)

arr = []

a1=priorityQueue()

a1.insert(arr, 3)
a1.insert(arr, 4)
a1.insert(arr, 9)
a1.insert(arr, 5)
a1.insert(arr, 2)

print ("Max-Heap array: " + str(arr))

a1.deleteNode(arr, 4)

print("After deleting an element: " + str(arr))


