# NOTE FOR THIS SEGMENT

# there is called CASTING, to specify the data type, example
x = int(3.5) # so variable x be an integer type
y = float(3) # so variable y be an float type
print(x) # the output 3
print(y) # the output 3.0

# get the type of your variable
print(type(x))

# one value to mutiple variable
x=y=z = 'Im the god of programming languages'
print(x)
print(y)
print(z)

# unpacking the values from the list or tuple
fruits = ['apple', 'banana', 'mango']
x,y,z = fruits
print(x)
print(y)
print(z)

'''
variable that are outside the function (def) are global variable,
which is can be use inside or outside the function. then if the variable 
inside the function, the variable will be local or just use inside the function.
we can make the variable inside the function to be a global variable. 
'''
x = 'Universitas Singaperbangsa Karawang'

def university():
    global x # to make this variable global, just add "global" before the variable initiate
    x = 'Universitas Indonesia' 
    print('im a student at ' + x)

university()
print('im a student at ' + x)

# exercise 1
carname = 'Volvo'

# exercise 2
x = 50

# exercise 3
x = 5
y = 10
print(x + y)

# exercise 4
x = 5
y = 10
z = x + y
print(z)

# exercise 5
x, y, z = "Orange", "Banana", "Cherry"

# exercise 6
x = y = z = "Orange"

#exercise 7
def myfunc():
    global x
    x = 'fantastic'