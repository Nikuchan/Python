language="java"
print("Checking if else conditions")
if language=='Python':
    print(Python)
elif language=="java":
    print("java")
else:
    print("no match")

print("\nChecking Boolean Conditions")
user='Admin'
logged_in=False

if user=='Admin' and logged_in:
    print("ADMIN PAGE")
else:
    print("Bad Creds")

if not logged_in:
    print("Please Log In")
else:
    print("Welcome")

print("\nWorking with Object Identity")
a=[1,2,3]
b=[1,2,3]

print(id(a))
print(id(b))

print(a==b)
print(a is b)

b=a
print(a is b) # or
print("same as")
print(id(a)==id(b))

print("\nChecking False Conditions")
condition= '34234'

if(condition):
    print("Evaluated to true")
else:
    print("Evaluated to false")




















