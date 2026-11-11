city = ("london", "paris","tokyo","newyork", "mumbai")
print(city[0])
print(city[-1])
print(city[1:4])

t = (4,)
print(type(t))

student = ("Anu", 85, "A")
name, mark, grade=student
print(name)
print(mark)
print(grade)


a = 10
b = 20
a,b = b,a
print(a)
print(b)

numbers = (10, 20, 30, 40, 50)
first, *rest = numbers
print (first)
print(rest)


subject =["maths", "english", "hindi"]
t = tuple(subject)
print(t)
t = t+("computer",)
print(t)

t = (4, 9, 4, 1, 4)
print(t.count(4))
print(t.index(4))
