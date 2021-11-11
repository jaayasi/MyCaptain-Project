#Task1
r=float(input("Input the radius of the circle :"))
a=3.14*r*r
print("The area of the circle with radius ",r" is: ",a)

#Task2
filename = input("Input the Filename: ")
f_extns = filename.split(".")
print ("The extension of the file is:"  + repr(f_extns[-1]))
