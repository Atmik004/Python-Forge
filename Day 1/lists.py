###   List ###
#Creating and Accessing Lists
fruits = ["apple", "banana", "mango"]

print(fruits[0])    # apple
print(fruits[-1])   # mango
print(fruits[0:2])  # ['apple', 'banana']

fruits[1] = "grape"  # mutation — lists allow this!

#Key List Methods
lst = [3, 1, 4, 1, 5]

lst.append(9)       # [3,1,4,1,5,9]   — add to end
lst.insert(0, 0)    # [0,3,1,4,1,5,9] — insert at index
lst.remove(1)       # removes first 1
lst.pop()            # removes last element
lst.sort()           # sort ascending
lst.reverse()        # reverse in place
len(lst)             # number of items

#list is ordered.
a = [12, 23, 34, 16, 87]
print(a)
print(type(a))
print(a[-1])

# List is mutable so we can change the overall anything in the list
l = [1,2,3,4,5,6,4,8,9,0]
print(l)
l[6]= 7
print(l)

# Traversing on list
l2 = [0,1,2,3,4,5,6,7,8,9]

# Traversing on values
for i in a:
    print(i)

# Traversing on index
for i in range(0, len(l2)):
    print(f"{i} : {l2[i]}")

# Inbuild Funtions in LIST

ls = [11,12,13,14,16,17,18] # Normal list

# list.append()

l2.append(19) # this functions adds the new value in the end of list.
print(l2)

# list.insert()

l2.insert(4, 15) #this function adds new value at disered location by using index.
print(l2)

# New list
l3 = [123,23,25,26,27,28,34,29]
print(l3)

# list.pop()
p = l3.pop(5) # it can pop certain value and save it into a variable
print(p)
print(l3)

# list.clear()
l3.clear()  # IT removes all the list elements
print(l3)

# New list
l4 = [123,23,25,26,27,28,34,29]
print(l4)

# list.remove
l4.remove(34)
# if value is given then the it gets removed. Value can be index of specific Charater.
print(l4)

# New list
l5 = [23,56,45,76,90,34,82,25,48,85]

# list.sort()
l5.sort() # Sorting in Asending order
print(l5)

l5.sort(reverse=True) # Sorting in Desending order!
print(l5)

# # #  questions # # #

#Q1. Print all positive and negative elements separately.
# Input: [3, -1, 4, -5, 9]
# Positive: [3,4,9] Negative: [-1,-5]

l6 = [-23,34,-65,67,-53,-69,64,54]
pve = []
nve = []
for i in l6:
    if i > 0:
        pve.append(i)
    else:
        nve.append(i)

print(pve)
print(nve)

#Q2. Find the mean (average) of all list elements.
#Input: [10, 20, 30, 40]
#Mean = 25.0

l6 = [32,45,76,54,38,81,49,95]
sum = 0
for i in l6:
    sum += i
mean = sum/len(l6)
print(f"Mean : {mean}")

#Q3. Find the greatest element and print its index.
#Input: [4, 8, 2, 9, 1]
#Greatest = 9 at index 3

l7 = [8,3,5,9,2,6,1]
largest = 0
index = 0
for i in range(len(l7)):
    if l7[i] > largest:
        largest = l7[i]
        index = i

print(f"Your Largest Number is {largest} on Index of {index}")

# Q4. Find the second greatest element.
#Input: [4, 8, 2, 9, 1]
#Second greatest = 8
#same list l7 will be used

largest = 0
sec_largest = 0

for i in l7:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i

print(l7)
print(f"Second largest Number is {sec_largest}")

# Q5. Check if the list is already sorted.
#Input: [1, 3, 5, 7]
#List is sorted ✅
#Input: [3, 1, 4]
#Not sorted ❌
'''copyl7 = l7
print(l7)
l7.sort()
print(l7)
if copyl7 == l7:
    print("list is sorted")
elif l7 != copyl7:
    print("List is not sorted!")
    print(f"this is unsorted list {copyl7}")
    print(f"New sorted list {l7}")
'''
for i in range(len(l7)-1):
    if l7[i] > l7[i+1]:
        print("Your list is Unsorted!")
        break
else:
    print("Your list is sorted!")