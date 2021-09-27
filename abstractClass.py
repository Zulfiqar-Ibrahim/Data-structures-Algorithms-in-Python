"""


An abstract class can be considered as a blueprint for other classes. 
It allows you to create a set of methods that must be created within any 
child classes built from the abstract class. A class which contains one or 
more abstract methods is called an abstract class. An abstract method is a method 
that has a declaration but does not have an implementation. While we are designing 
large functional units we use an abstract class. When we want to provide a 
common interface for different implementations of a component, we use an abstract class. 


"""

from abc import ABC, abstractmethod

class Polygon(ABC):
    
    @abstractmethod
    def no_of_sides(self):
        pass
    
class Triangle(Polygon):
    
    # overriding abstract method
    def no_of_sides(self):
        
        print("Traingle has three sides")
        
class Pentagon(Polygon):
    
    # overriding abstract method
    def no_of_sides(self):
        
        print("Pentagone has 5 sides")
        


class Hexagon(Polygon):
 
    # overriding abstract method
    
    def no_of_sides(self):
        
        print("Hexagon has 6 sides")
        
class Quadrilateral(Polygon):
 
    # overriding abstract method
    
    def no_of_sides(self):
        
        print("Quadrilateral has 4 sides")


#poly = Polygon()
R = Triangle()
R.no_of_sides()
 
K = Quadrilateral()
K.no_of_sides()
 
R = Pentagon()
R.no_of_sides()
 
K = Hexagon()
K.no_of_sides()