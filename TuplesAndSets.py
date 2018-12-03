# Immutable
tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# It wont work
#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)

# Sets: unlike tuples and list , sets does not care about order
# There are also no duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}

art_courses = {'History', 'Math', 'Art', 'Design'}

print(cs_courses)

# We can do this with list and tuples also , but sets are optimised for it
print('Math' in cs_courses)

print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
# OR
empty_list = list()

# Empty Tuples
empty_tuple = ()
# OR
empty_tuple = tuple()

# Empty Sets
#empty_set = {} # This isn't right! It's a dict
empty_set = set()








