message='''adsasdds
asdasdasd ASDASD'''

print(message.count("as"))
print(message.find("as"))

#returns -1 if fails
print(message.find("Universe"))

message2=message.replace("as","universe")
print(message2)

greetings='Hello'
name="Abhijeet"
message=greetings+' '+name

# OR

#Using Place Holders
message= '{}, {}. Welcome!'.format(greetings,name)

# OR

#Using fStrings
message=f'{greetings}, {name.upper()}. Welcome'

print(message)

print(dir(name))

print(help(str))

print(help(str.lower))














