point = (10, 20)
dob = (15, "August", 2005)
single = (5,)
not_tuple = (5)
print(type(single))
print(type(not_tuple))
empty = ()



days = ("mon", "tue", "wed", "thu", "fri")
print(days[0], days[-1])
print(days[1:3])
print(days[::-1])
print(len(days))









t = (1, 2, 3)
t = t+(4,)
t = t + (4,5)
print (t)
x = (1,[2, 3])
x[1].append(4)
print(x) 



t = (3, 7, 3, 9, 3)
print(t.count(3))
print(t.index(9))
print(7 in t)
print(max(t),min(t),sum(t))
print(t + (1,2))
print(sorted(t))


student = "Anu", 19, "BCA"
print(student)
print(type(student))
boarding = ("Riya", "12A", "Gate 5")
print(boarding)


student = "Anu", 19, "BCA"
name ,age , course = student 
print(name, age)
a,b = 10, 20
a,b = b,a 
print (a,b)
first, *rest = (1, 2, 3, 4, 5)
print(first,rest)
*start, last = (1, 2, 3, 4)
print(start, last)


lst = [1,2,3]
t=tuple(lst)
back = list(t)
back.append(4)
t=tuple(back)
print(t)