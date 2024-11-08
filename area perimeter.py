# area perimeter
#date: 1/11/2024
#Author jonah
#version: 6.9

def shape():
    length = float(input("Enter the length of the rectangle u carrot: "))
    while length < 0 or length == 0:
        print("Please enter a number more than 0 stupid")
        
        
        
        length = float(input("Enter the length of the rectangle u carrot: "))
    
    
    9
    
    width = float(input("Enter the width of the rectangle hurry up: "))
    while width < 0 or length == 0:
        print("enter a number more than 0 stupid")
        
        
        
        
        width = float(input("Enter the width of the rectangle: "))
    
    
    
    
    area = length * width
    perimeter = 2 * (length + width)
    print(f"The area of the rectangle is {area} \nThe perimeter is {perimeter}")




running = ""
while running == "":
    shape()
    running = input("Press <enter> to continue or any key to stop") == ""
