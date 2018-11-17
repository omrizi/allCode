

l1 = []
s1 = set()
s2 = set()
s1.add("12.12")
s1.add(True)
s2.add("12.124")
s2.add(False)
l1.append(s1)
l1.append(s2)
print(list(l1[0])[1])
