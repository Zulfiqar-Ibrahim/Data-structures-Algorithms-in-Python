''' 
In this we will use Divide & Conquere  strategy for the solution of problems. Recursive functions play very
important role in the D&C technique.
'''
class Recursive:

    def __init__(self,number):
        print('object crafted')
        self.value_a=number
        self.recursive(self.value_a)
    def recursive(self,value_a):
        """
        This funtion is written to decrementing numbers from starting numbers
        using recursive method. This methad keep calling itself untill it reaches
        boundry. 
        """

        #print(value_a)
        if value_a > 0:
            print(value_a, end=',')

            self.recursive(value_a-1)
        else:
            return 0

re=Recursive(10)

