import random
# If you don't want a field just comment with an ("#") the variable name and the "+(var name)" in "string"      
lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numbers = "0123456789"
symbols= "!@#$%^&*()."

string = lower + upper + numbers + symbols
lenght = 12
passw = "".join(random.sample(string,lenght))
print(f"{passw}") 
         
        

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        