def create_stack():
    stack=[]
    return stack

def check_empty(stack):

    if len(stack)==0:
        return True
    else:
        False

      
def push(stack,item):

    stack.append(item)
    print('item is pushed: ',item)
def pop(stack):

    if check_empty(stack):
        print('no value in stack')

    else:

        return stack.pop()
def pop_LIFO(stack):

    if check_empty(stack):
        print('no value in stack')

    else:
        i= -1
        while (i >= -(len(stack))):
            

            print(stack[i])
            i=i-1

            
stack=create_stack()
pop(stack)
push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
push(stack,5)
push(stack,6)
push(stack,7)
pop_LIFO(stack)
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
print('item is poped ',pop(stack))
