def palindrom(string):
    
    for i in range(0,int(len(string)/2)):
        mystring=string[i]
        testString=string[len(string)-i-1]
        if mystring!=testString:
            return False
        return True
            
        

print(palindrom('malayalam'))
        