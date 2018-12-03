# Lists
courses=['History','Math','Physics','Compsci']
courses_2=['Football','Basketball']
print(len(courses))
print(courses)
print(courses[-1])
print(courses[0:3])
print(courses[::-1])

# Add
courses.append('Art')
print(courses)


#Insert at the beginning
courses.insert(0,'Science')
print(courses)

#Not what we want
#courses.insert(0,courses_2)
#print(courses)
#print(courses[0])


# Append we use to add individual items , Extend we use to add another list in the form of individual items
courses.extend(courses_2)
print(courses)

#remove
courses.remove('Math')
print(courses)

# To remove the last value
popped=courses.pop()
print(courses)
print ("popped value from Courses is " +popped)

#Reverse
courses.reverse()
print(courses)

#Sort
courses.sort()
print(courses)

num=[4,21,54,1,34]
num.sort()
print(num)

#Sort in descending Order
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)


# Sorting the list without altering the original list using the function sorted other than the sort method
Sorted_courses=sorted(courses)
print(courses)
print(Sorted_courses)


print(min(num))
print(max(num))
print(sum(num))
print(courses.index('Compsci'))

print('Art' in courses)


for course in courses:
    print(course)

# TO get the index also

for index,course in enumerate(courses):
    print(index,course)

# TO start with 1 as the index
print("\n")
for index,course in enumerate(courses,start=1):
    print(index,course)

# turning the list into a string separated by some character
course_str=' - '.join(courses)

print(course_str)

new_list=course_str.split(' - ')
print(new_list)

























