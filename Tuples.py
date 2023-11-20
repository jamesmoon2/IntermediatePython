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
