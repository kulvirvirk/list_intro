# List is a type of data sturcture, similar to arrays. 

# 1. create & print a list of fruits
# 2. Access list elements with index number
# 3. Access last element of list by Negative index
# 4. Slice the list to print only element at index 1,2,3
# 5. try out append method to add element at the end of the list


# 1.create & print a list of fruits
my_fav_fruits = ["mango", "kiwi", "banana", "blueberry", "orange"]
numbers_list = [1,2,3,4,5,2.5]
print(my_fav_fruits)
print(numbers_list)

# 2.Access list elements with index number
# As an ordered sequence of elements, each item in a list can be called individually, through indexing.
# Each item in a list corresponds to an index number, which is an integer value, starting with the index number 0.

print(my_fav_fruits[2])
print(my_fav_fruits[4])

print(numbers_list[3])


# 3.Access last element of list by Negative index
print(my_fav_fruits[-1])
print(numbers_list[-1])


# 4. Slice the list to print only element at index 1,2,3 
print(my_fav_fruits[1:4]) 
#the first index number is where the slice starts (inclusive), and the second index number is where the slice ends (exclusive), which is why in our example above the items at the position, 1, 2, and 3 are the items that print out.

# 5. try out append method to add element at the end of the list
my_fav_fruits = ["mango", "kiwi", "banana", "blueberry", "orange"]
my_fav_fruits.append('watermelon')
print(my_fav_fruits)

