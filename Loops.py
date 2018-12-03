nums=[1,2,3,4,5]
print("Checking break and continue Statements")

for num in nums:
    if num==3:
        print("found 3")
        continue
    print(num)

print("\nInner Loop")
for num in nums:
    for letter in 'abc':
        print(num,letter)

print("\nChecking Out Range")
for i in range(1,11):
    print(i)

print("\nWhile Loop")
x=0
while x<10:
    print(x)
    x=x+1
