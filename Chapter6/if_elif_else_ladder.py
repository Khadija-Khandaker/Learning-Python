# If elif else ladder

a = int(input("Enter your age: "))

if(a>=18):
    print("You are above the age of consent")
    print("Good for you")


elif(a==0):
    print("0 is not a valid age")
    print("Please try again")        


elif(a<0):
    print("Negative number is not a valid age")
    print("Please try again")    
   

else:
    print("You are below the age of consent")


print("End of the program")      