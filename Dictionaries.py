student={'name':'john','age':25,'courses':['Math','CompSci']}

print(student)
print(student['name'])
print(student['courses'])
# print(student['phone'])

print(student.get('name'))
print(student.get('phone',"Not Found"))


# Adding
#student['phone']='555-5555'
#print(student['phone'])

# Updating
#student['name']="jane"
#print(student)

# OR

student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)

# Delete
#del student['age']
#print(student)

age = student.pop('age')

print(student)
print(age)

print(len(student))

print(student.keys())

print(student.values())

print(student.items())

#for key in student:
 #   print(key)

for key,values in student.items():
    print(key,values)










