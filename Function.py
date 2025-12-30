# def message(name):
#     print(f"Hello {name}")
# message("Qasim")

# def addition(num1,num2):
#     print(f"Addition is {num1+num2}")
# addition(2,3)
# addition(21,32)
# addition(0,5)
# addition(34,1)


# '''Key Argument'''

# def mess(name=None,appointed=None): # default value if user didn't pass the arguments 
#     print(f"{name} you are hired as a {appointed}")
# mess(appointed="Data Scientist",name="Qasim")

# it help us to pass input in correct location

def checkEvenOdd(num):
    if num%2==0:
        return f"{num} is even"
    else:
        return f"{num} is odd"
ch = 'z'
while ch !='n':
    print(checkEvenOdd(int(input("Enter a number"))))
    ch = input("Character :")