#Dictionary

#Key-Value Storage
#A dictionary stores data as key: value pairs — like a real dictionary
            # where you look up a word (key) to find its meaning (value).

#Vanilla Python
d = {10:100, 20:200, 30:300, 40:400}

d[50]=505        #Creating a new value in pair
#print(d(40))      #Reading a value
d[50]=500        #Updating a key value that already exist
print(d)

#Method approach
#Method	                            Description
#clear()	               Removes all the elements from the dictionary
d.clear()
print(d)
d = {10:100, 20:200, 30:300, 40:400, 5:500}

#copy()	                   Returns a copy of the dictionary
#d.copy()

#fromkeys()	               Returns a dictionary with the specified keys and value
q = d.fromkeys([10,20,30,40,50], 50)
print(q)

#get()	                   Returns the value of the specified key
print(d.get(10))

#items()	                Returns a list containing a tuple for each key value pair
print(d.items())

#keys()	                    Returns a list containing the dictionary's keys
print(d.keys())
print(d.values())
#pop()	                    Removes the element with the specified key
print(d.pop(30))
print(d)
#popitem()	                Removes the last inserted key-value pair
print(d.popitem())
print(d)
#setdefault()	            Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
print(d.setdefault(60,600))

#update()	                Updates the dictionary with the specified key-value pairs
d.update({70:700})

#values()	                Returns a list of all the values in the dictionary
print(d.values())

print(d)

#Traversing (loops)
