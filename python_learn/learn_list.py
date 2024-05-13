x=[1,2,3,4,5,6]
print(len(x))

# print the first 3 elements
print(x[:3])
# print everithin after the 3rd element
print(x[3:])

# print the last 2
print(x[-2:])


x.extend([7,8])
print(x)



def Square(x):
    return x*x

print(Square(2))

def DoSomething(f,x):
    return f(x)

print(DoSomething(Square,3))

# lambda function
print((lambda x: x*x)(3))

print(1==3)

print(True or False)
print(True and False)
print(not True)


for x in range(5):
    print(x)
    