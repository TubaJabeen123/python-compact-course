from math import pi


if __name__ == "__main__":

#Task 1:  Area of a Circle
    print("Task 1: Area of a Circle: ")
    radius = float(input("Enter the radius of the circle: "))
    print("The area of the circle with radius "+ str(radius)+ " is: " +str(pi * radius ** 2))




#Task 2:  Simple Variable Declaration and Output
    print("\nTask 2: Simple Variable Declaration and Output")
    zahl= 10
    kommazahl = 10.5
    text = "Hello World!"
    wahrheitswert= True


    print("First Variable "+str(zahl))
    print("Type of zahl: "+str(type(zahl)))

    print("Second Variable "+str(kommazahl))
    print("Type of kommazahl: "+str(type(kommazahl)))

    print("Third Variable "+str(text))
    print("Type of text: "+str(type(text)))

    print("Fourth Variable "+str(wahrheitswert))
    print("Type of wahrheitswert: "+str(type(wahrheitswert)))


#Task 3:  Data type conversion
    print("\nTask 3: Data type conversion")
   #integer to float
    variable1 = 10
    variable1 = float(variable1)
    print("integer to float: "+str(variable1))

    #float to integer
    variable2 = 3.14
    variable2 = int(variable2)
    print("float to integer: "+str(variable2))

    #integer to string
    variable3 = 453
    variable3 = str(variable3)
    print("integer to string: "+str(variable3))

    #string to integer
    variable4 = "123"
    variable4 = int(variable4)
    print("string to integer: "+str(variable4))

    #integer to boolean
    variable5 = 0  
    variable5 = bool(variable5)
    print("integer to boolean: "+str(variable5))



    #task 4:  factorial of a number
    print("\nTask 4: Factorial of a number")
    number = int(input("Enter a number to calculate its factorial: "))
    factorial = 1
    for i in range(1, number + 1):
        factorial *= i
    print("The factorial of " + str(number) + " is " + str(factorial))