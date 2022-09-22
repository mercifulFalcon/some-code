x = int(input("Enter the number to multiply: ")) # A x ...
i = x - 1

while i < x :
    y = int(input("Enter the number at which the multiplication stops: "))  # ... x B
    j = 0
    i += 1
    while j <= y:
        print(f"{i} x {j} = {i * j}")
        j+=1