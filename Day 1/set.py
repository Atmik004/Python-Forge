l = [1,1,1,2,4,5,3,6,3,5,3,4,5,2,4,5,7,8,4,8]
s = set(l)
print(s)

s = {10,20,30,40,50}
print(s)

# add()
s.add(60)
print(s)

#discard
s.add(69)
print(s)
s.discard(69)
print(s)

#pop
p = s.pop()
print(p)
print(s)

#Signs in sets
s1 = {1,2,3,4,5,6}
s2 = {5,6,7,8,9,0}

print(s1.difference(s2))

#alternate way could be
print(s2-s1)
#    s2 -= s1
#   print(s2)

#intersection
print(s1.intersection(s2))
