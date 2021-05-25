# Data Structures and Algorithms in Python
This Repo is used for the implementation of data structures and algorithms and practices common programming technical interview questions. Python is used for these tasks but
any language can be used. why did I choose python? Because python is easy to code/read, if I have to use some pointers then  I will use C/C++. Many non-High-Performance-computing tasks can be implemented using python. Using C/C++ for high-performance tasks does make sense since it is more close to the hardware (precompiled and better performance, memory efficiency).  

## ALGORITHMS:
Step by step procedure to solve the problem. What is the difference between algorithm and program? Algorithms are written as design time and program is written at implementation time.
A person who has domain knowledge, understand the problem and design algorithm for the solution. A programmer can  convert this human readable code into programming language.
A programmer can also be designer.  
A prior analysis is performed on algorithm and it is language/hardware independent. Time and space analysis of algorithm can be considered as performance matrics of algorithm 
CHaracteristics of Algorithm:
input/output
Definitness (Every step is crystel clear)
Finiteness (There must be end of algorithm)
Effectiveness (Must produce expected results)

### Example
A=8,2,9,4,2 

n=5
  
```C++
int sum(A,n)
{
   s=0; // 1
   for(i=0;i<n;i++) // n+1
   {
      s=s+A[i]; // n
   }
return s // 1
}
```
Time complexity F(n)= 2n+1 .


Order(n)


A----n


n----1


s----1


i----1 ,


Space complexity S(n)=n+3 (number of variable used in computation).

Some Time complexity formulas for forloops


```C++
for(i=0;i<n;i++) // O(n)
for(i=0;i<n;i+2) // n/2 O(n)
for(i=i;i>1;i--) // O(n)
for(i=0;i<n;i*2) // O(log_2 n)
for(i=0;i<n;i*3) // O(log_3 n)
for(i=0;i<n;i=i/2) // O(log_2 n)
```
Time complexity of while loop

```C++
i=0 //1
while(i<n) // n+1
{
   statement; // n
   i++;       // n
}
```
F(n) = 3n+1

O(n)

### Asymptotics Notations 

Ω


 x<sup>2</sup>

