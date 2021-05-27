import math


print('Hello world') #Hello world
print(1+2,1*2,1/2,1-2) #addtion,mulitiplication,division,subtraction
print((17/3)) # division always returns a floating point number
print((17//3)) # // remove the floating point part
print(17 % 3) # remainder operator
print(4 * 3.75 - 1)
tax = 12.5 / 100
price = 100.50
print(price * tax)
print(price)

#strings
print('Zulfiqar Ibrahim')
print('"Yes," they said.')
print('doesn\'t')
print('C:\some\n Jame \n Kocko ')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
word = 'Python'
print(word[0])   # character in position 0
print(word[1])   # character in position 1
print(word[2])   # character in position 2
print(word[3])   # character in position 3
print(word[4])   # character in position 4
print(word[5])   # character in position 5
print(' ')
print(word[-5])  # character in position -5
print(word[-4])  # character in position -4
print(word[-3])  # character in position -3
print(word[-2])  # character in position -2
print(word[-1])  # character in position -1
print(word[0])   # character in position 0
print((' '))
print(word[0:2]) # characters from position 0 (included) to 2 (excluded)
print(word[2:5]) # characters from position 2 (included) to 5 (excluded)
print(word[:2] ) # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end

print(""" +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
""")
print(' ')
print('LISTS')
squares = [1, 4, 9, 16, 25]
print(squares)
print(squares[0])
print(squares[4])
print(squares[-5:])
print(squares + [36, 49, 64, 81, 100])

print('Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:')
cubes = [1, 8, 27, 65, 125]
print(cubes)
print(4 ** 3)
cubes[3] = 64
print(cubes)
cubes.append(216)
print(cubes)
cubes.append(7 ** 3)
print(cubes)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)
letters = ['a', 'b', 'c', 'd']
print(len(letters))
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print(x[0][1])
print(' ')
print(' Febonacci Series ')
a,b=0,1
while a < 10:
    print(a)
    a=b
    b=a+b

numbers=[1,2,3,4,5]
print('length of numbers is ',len(numbers))
l=1
R=len(numbers)
print('mid is ',(l+R)/2)