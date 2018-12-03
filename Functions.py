# if we write pass after a function , we are mentioning that we want to define the function later
#def hello_func():
    #pass


#def hello_func(greeting,name="you"):
 #   return f"{greeting}, {name}"

#print(hello_func("abhijeet").upper())
#print(hello_func("Hello","Abhijeet "))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
courses=['Math','Art']
info={'name':'john','age':22}

#student_info('Math','Art',name='John',age=22)
student_info(*courses,**info)