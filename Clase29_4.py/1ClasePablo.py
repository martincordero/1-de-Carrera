n = input("Dame un número: ")
archivo = 'tabla-' + str(n) + '.txt'
f = open(archivo, 'w')
for i in range(1,11):
    f.write(str(n) + '*' + str(i) + " = " + str(int(n) * i) + '\n')
f.close()