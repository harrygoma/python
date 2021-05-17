#creating a function and calling it
x = eval(input("enter your first number"))
y = eval(input("enter your second number"))
def add(x,y): #defining the function
	print(x + y) 
add(x,y) #calling the function

course = "Python Programming"
print(len(course)) #length of character
print(course[0]) #accessing a particular character
print(course[5]) # fifth character
print(course[-1]) # second character moving to the left
print(course[0:3]) #first three charactersS
print(course[0:7])
print(course[0:3])
print(course[:]) #displayes the whole text

#escape sequences
 #\"
#\'
#\\
#\n another line
course = "Python \n Programming" #escape character, using double quotation makes the supportig code invalid
print(course)

# formatted strings
first = "Harry"
last = "Benjamin"
full = first + " " + last 
print(full)
# or
first = "Harry"
last = "Benjamin"
full = f"{first} {last}"
print(full)

first = "Harry"
last = "Benjamin"
full = f"{len(first)} {2 + 2}"
print(full)

#strings method
course = "     python Programming"
print(course.upper()) #uppercase
print(course.lower()) #lowercase
print(course.title()) # capitalize the first alphabet
print(course.strip()) # removes widespaces




