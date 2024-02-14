a = 3
b = 1.2345
c = "Lyon"

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

a = str('París')
b = int(1.2345)
c = float(3.2)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

PI, ciudad, ii = 3.14, "Burdeos", 58

print(PI)
print(ciudad)
print(ii)

print(type(PI))
print(type(ciudad))
print(type(ii))

lineas = '''París
es
la capital de 
Francia.'''

print(lineas)
print(type(lineas))

def dividir(a, b):
    if b is 0:
        return str("División por cero prohibida")
    return a/b
    
print(dividir(5.4, 2))

print(dividir(5.4, 0))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n  * factorial(n-1)

print("Factorial de 4 = ", factorial(4))
print("Factorial de 10 = ", factorial(10))
