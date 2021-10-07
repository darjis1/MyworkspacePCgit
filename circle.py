#Shrey Darji circle.py 
import math
print('Welcome to circle and rectangle area finder...')
global options
pi = math.pi
choice = int(input('\n1) Area of a circle \n2) For Circumference of a circle \n3) Area of a rectangle \n4) Perimeter of a rectangle \n5)QUIT'))

#Area of a circle
def circle(circle):
    if choice == 1:
        radius = int(input('What is the radius of your circle:'))
        Area = pi * radius ** 2
        print('Your area is:', Area) 
    #Circumference of a circle
    elif choice == 2:
        radius = int(input('What is the radius of your circle:'))
        Cir = 2 * pi * radius
        print('Your circumference is:', Cir)

    else:
        print('Invalid Operator...')










