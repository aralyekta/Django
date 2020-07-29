class Person:
    num_of_people = 1

d1 = Person()
d2 = Person()
d1.num_of_people = 10
print(d1.num_of_people)
print(d2.num_of_people)
print(Person.num_of_people)
Person.num_of_people = 2
print(d1.num_of_people)
print(d2.num_of_people)
print(Person.num_of_people)