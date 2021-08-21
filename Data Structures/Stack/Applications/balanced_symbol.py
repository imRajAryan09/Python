# Import the Stack class as defined
from Stack_ADT import Stack

def parity_checker(symbol_string):
    
    s=Stack()    # Create an object s of thhe class Stack
    balanced=True 
    index=0    # An indexing variable
    
    while index<len(symbol_string) and balanced:
        
        symbol=symbol_string[index]
        
        if symbol=="(":
            s.push(symbol)
            
        else:
            
            if s.is_empty():
                balanced=False
            
            else:
                top=s.pop()
                
                opens = "([{"
                closes = ")]}"
                ans=opens.index(top) == closes.index(symbol)
                
                if  ans==False:
                    balanced=False
                
        index+=1
    
    if balanced and s.is_empty():
        return True
    
    else:
        return False
    

print(parity_checker('{{([][])}()}'))
print(parity_checker('[{()]'))
