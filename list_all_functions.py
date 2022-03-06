list = [1,2,3,4,5,3,5]
list7 = [1,2,3,45,4,5,4,5]
list1 = ['~','B','a','b','z','A']
list3 = ['lion','elephant','tiger']
list4 = ['tiger','lion','elephant','uv']

# return max element in the list
# Number - return max value integer
# Alphabet or string - return max value according to ASCII values
print(max(list))
print(max(list1))
print(max(list3))
print(max(list4))

print(list1.index('z'))         # Returns the index of given object
print(len(list))                # Returns the length of list
list.append(list1)              # Add element at the end of list
print(list)
print(list.count(5))            # Return how many times 5 repeat in the list
list.extend(list3)              # Append elements of another list to given list
print(list)
print(list.index(3))
list.insert(2,'bhushan')        # Add object 'bhushan' to the index 2 in list remaining elements move forward by 1 index
print(list)
list.pop(5)                     # Removes the object 5 from list appeared first not 2nd 5
print(list)
list7.remove(5)                  
print(list7)
list7.sort()
print(list7)
list1.sort()                    # sort the elements of list in Ascending Order.
print(list1)
list.reverse()                  # Reverse all elements of list 
print(list)
list.clear()
print(list)
