class Bird:
    
    def __init__(self):
        self.name = "Bird"
        
    def fly(self):
        
        print("Flying") 
        
class aves:
    def __init__(self):
        
        pass
    def attributes(self):
        
        print("Bird class belongs to aves which have feathers")
    
        
class parrot(Bird,aves):
    
    def __init__(self):
        super().__init__()
        self.name = "Parot"
        
    def run(self):
        
        print("can fly and run")
        
pa = parrot()

pa.run()
pa.fly()
pa.attributes()

    