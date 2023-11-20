# tuples: ordered, immutable, allows duplicate elements; must have a comma to be a tuple

mytuple = ("Max", 28, "Boston")

#you can create tuples from a list or other function by using the tuple function tuple()

print(mytuple)

item = mytuple[0] #selects first index in tuple; negative index goes from back to front

print(item)

# mytuple[0] = "Tim" # this will throw an error becuase tuples are immutable.

if "Max" in mytuple:  #check a tuple to see if an element is present
    print("yes")
else:
    print("No")

print(len(mytuple)) #returns the number of elements in a tuple

print(mytuple.count("Max")) #counts the number of times a value appears in an tuple

print(mytuple.index(28)) #returns the index  of the identified value

my_list = list(mytuple) #converts a tuple into a list

print(my_list)

#slicing a tuple - access subparts by using a colon

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

b = a[2:5] # select a given range of a tuple using index ranges

print(b)
