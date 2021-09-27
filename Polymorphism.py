"""
Polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).

"""

class Panguin:
    
    def fly(self):
        
        
        print("Panguin can not fly ")
        
    def swim(self):
        
        print("Panguin can swim")
class eagle:
    
    def fly(self):
        
        print("Eagle can fly")
        
    def swim(sef):
        
        print("Eagle cannot swim")
        
        
def flying_test(bird):
    bird.fly()
    
ea = eagle()
pa = Panguin()
flying_test(ea)
flying_test(pa)

"""
In the above program, we defined two classes Parrot and Penguin. 

Each of them have a common fly() method. However, their functions are different.

To use polymorphism, we created a common interface i.e flying_test() function
 
that takes any object and calls the object's fly() method. Thus, when we passed

the blu and peggy objects in the flying_test() function, it ran effectively.

"""