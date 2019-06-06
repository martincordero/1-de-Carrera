def cuadrado(n):
    return n*n

def aplica(f, n):
    return f(n)

def cubo(n):
    return n**3

def rectangulo(n, m):
    return n*m

print(aplica(cuadrado, 2))

print(aplica(cubo, 2))

list(map(cuadrado, [1, 2, 3]))

list(map(rectangulo, [1, 2, 3], [4, 5, 6]))