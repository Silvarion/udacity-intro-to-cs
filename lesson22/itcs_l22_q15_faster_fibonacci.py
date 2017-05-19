#Define a faster fibonacci procedure that will enable us to computer
#fibonacci(36).

def fibonacci(n):
    a = 0
    b = 1
    result = 0
    for i in range(0,n-1):
        result = a + b
        a = b
        b = result
    return result

print fibonacci(0)
#>>> 0
print fibonacci(1)
#>>> 1
print fibonacci(15)
#>>> 610
print fibonacci(36)
#>>> 14930352
