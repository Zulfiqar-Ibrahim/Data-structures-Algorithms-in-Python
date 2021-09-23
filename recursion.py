def main(value):
    '''
    This fucntion is written to understand or refresh my recursion concepts
    
    '''
    a=value
    print(a)
    if a == 10:
        print("Base condition achieved")
        return 0
    else:
        main(a+1)
#main(1)


def findNthnumber_Fibo(value):

    if  value < 2:
        
        return value
    else:
        return findNthnumber_Fibo(value - 1) + findNthnumber_Fibo(value - 2)
  
       
print(findNthnumber_Fibo(4))

