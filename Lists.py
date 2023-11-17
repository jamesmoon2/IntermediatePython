    # Lists: ordered, mutable, allows duplicate elements

my_list = ["Banana", "Cherry", "Apple"]

print(my_list)

item = my_list[0] #selects an item from the list at index 0
print(item)

for fruit in my_list: #the "fruit" lable does not matter. it will just run through the items in the list
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

my_list = [0] * 5 # select an index and execute a function on it

print(my_list)

my_list = [1, 2, 3, 4, 5]

my_list2 = [6, 7, 8, 9]

new_list = my_list + my_list2 # you can combine lists using the add function

print(new_list) 

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

a = my_list[1:5]  #selects a portion of a list based on index; if you dont specify a start, it starts at 0 and if
# you dont specify an endpoint, it stops at the end

print(a)

b = my_list[1::]  # double colons is the step; default is one, 2 = every second item, etc

list_org = ["banana", "cherry", "apple"]

list_cpy = list_org # copies list; sets them equal;
    # .copy method makes an actual copy or list function
    # and use orignal list as an argument or use a slice [:]

## modiying a copy will also modify the original list



