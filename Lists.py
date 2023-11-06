    # Lists: ordered, mutable, allows duplicate elements

my_list = ["Banana", "Cherry", "Apple"]

print(my_list)

item = my_list[0]
print(item)

for fruit in my_list:
    print(fruit)

if "Cherry" in my_list:  #search within a list
    print("Yes")
else:
    print("No")

print(my_list)

print(len(my_list))  # calculate the number of entries in a list

my_list.append("Lemon")  # add item to end of list

print(my_list)

my_list.insert(1, "Blueberry") #insert an item a specific index in the list

print(my_list)

my_list.pop() #returns the last entery and removes it

print(my_list)

my_list.remove("Banana")  #remove a specific item

print(my_list)

my_list.reverse() #reverses the order

print(my_list)

my_list.sort() #sorts alphabetically, permanently. You can also create a new list sorted to keep both

print(my_list)

