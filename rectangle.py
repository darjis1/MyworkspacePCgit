import math 
global pi
pi = math.pi

print('Welcome...')


global options 
def rectangle(rectangle):
    if choice == 3:
        L = int(input("What is the Length of your rectangle:"))
        W = int(input("What is the Width of your rectangle:"))
        Area = L * W
        print('Your area is', Area)
    #Perimeter of a rectangle
    elif choice == 4: 
        L = int(input("What is the Length of your rectangle:"))
        W = int(input("What is the Width of your rectangle:"))
        Per = (L * 2) + (W * 2)
        print('Your perimeter is:', Per)










