class bank_account:
    
    def __init__(self,name):
        
        self.__Account_number = "CBC1236578"
        
        self.name = name
        
    def acountHolderName(self):
        
        if self.name == "Thomas":
            
            print(self.__Account_number)
        else :
             
            self._Account_number = "RDB1236578"
            
            print(self.__Account_number)
        
            
b1 = bank_account("Thomas ali")

b1.acountHolderName()

        
        
        