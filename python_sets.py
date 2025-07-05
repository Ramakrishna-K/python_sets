# A set in Python is an unordered, unindexed, and mutable collection of unique elements.

#   Creating a Set


# my_set =  {1,2,3}
# fruits = {"apple","mango","cherry"}
# #  correct  way to create an empty set
# empty_set = set()  

# print(my_set)

#  Adding and Removing Elements 
my_seet = {1, 2, 2, 3, 4}

my_seet.add(5)
my_seet.update([6, 7])     # Add multiple items

my_seet.remove(2)          # Removes 2; ❌ Error if 2 not found
my_seet.discard(3)         # Removes 3; ✅ No error if not found

# my_seet.clear()            # Removes all items

print(my_seet) 