

def fact(n):
    #Check if n is a positive integer
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be positive")
    
    if n == 0:
        return 1
    else:
        return n * fact(n-1) 
    

for n in range(0,502):
    print(f"{n}! : {fact(n)}")
