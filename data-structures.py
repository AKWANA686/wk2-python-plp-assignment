# Creating an empty list called my_list
my_list = []

# Appending this elements(10, 20, 30, 40) to my_list.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting the value 15 at the second position in the list
my_list.insert(1, 15)

# Extending my_list with another list: [50, 60, 70].
my_list.extend([50, 60, 70])

# Removing the last element from "my_list"
my_list.remove(70)

# Sorting "my_list" in ascending order
my_list.sort()

# Finding and printing the index of the value 30 in my_list.
# Find the index of the value 30
index = my_list.index(30)

# Print the index
print("Index of 30:", index)

# Prints the whole list
print(my_list)