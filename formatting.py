person = {'name': 'Jenn', 'age': 23}

l=['jin',23]

#sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.'
#print(sentence)


#sentence='My name is {} and I am {} years old'.format(person['name'],person['age'])
#print(sentence)

sentence='My name is {0[name]} and I am {1[age]} years old'.format(person,person)
print(sentence)

sentence='My name is {0[0]} and I am {0[1]} years old'.format(l)
print(sentence)

#sentence=f'My name is {person['name']} and I am {person['age']} years old'
#print(sentence)

# sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
# print(sentence)


tag = 'h1'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag, text)
print(sentence)


#sentence = 'My name is {0} and I am {1} years old.'.format(person['name'], person['age'])
#print(sentence)



