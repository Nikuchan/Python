# Lists
courses=['History','Math','Physics','Compsci']
courses_2=['Football','Basketball']
print("Slicing Examples")
print(len(courses))
print(courses)
print(courses[-1])
print(courses[0:3])
print(courses[::-1])

print("\nAdd")
courses.append('Art')
print(courses)


print("\nInsert at the beginning")
courses.insert(0,'Science')
print(courses)

#Not what we want
#courses.insert(0,courses_2)
#print(courses)
#print(courses[0])


print("\nAppend we use to add individual items , Extend we use to add another list in the form of individual items")
courses.extend(courses_2)
print(courses)

print("\nremove")
courses.remove('Math')
print(courses)

print("\nTo remove the last value")
popped=courses.pop()
print(courses)
print (f"popped value is {popped}")

print("Reverse")
courses.reverse()
print(courses)

print("\nSort")
courses.sort()
print(courses)

num=[4,21,54,1,34]
num.sort()
print(num)

print("\nSort in descending Order")
courses.sort(reverse=True)
num.sort(reverse=True)
print(courses)
print(num)


print("\nSorting the list without altering the original list using the function sorted other than the sort method")
Sorted_courses=sorted(courses)
print(courses)
print(Sorted_courses)

print("\nFinding Min and Max Values")
print(min(num))
print(max(num))
print(sum(num))

print("\nFinding the Index\n")
print(courses.index('Compsci'))

print('Print("Art in Courses")')
print('Art' in courses)

print("\nUsing for Loop")
for course in courses:
    print(course)

# TO get the index also
print("\nGetting Index value also using for loop")
for index,course in enumerate(courses):
    print(index,course)

print("\nTO start with 1 as the index")
print("\n")
for index,course in enumerate(courses,start=1):
    print(index,course)

print("\nturning the list into a string separated by some character")
course_str=' - '.join(courses)

print(course_str)

print("\nConverting the string back to List")
new_list=course_str.split(' - ')
print(new_list)
