nombre1 = "Martín"
peso1= 70
altura1= 1.80

nombre2 = "Ces"
peso2 = 60
altura2 = 1.8

nombre3 = "Gio"
peso3 = 90
altura3 = 1,60

def calcular_bmi (nombre, peso, altura):
    bmi = peso / (altura ^ 2)
    print("bmi: ")
    print(bmi)


resultado1 = calcular_bmi(nombre1, peso1, altura1)
print(resultado1)
resultado2 = calcular_bmi(nombre2, peso2, altura2)
print(resultado2)
resultado3 = calcular_bmi(nombre3, peso3, altura3)
print(resultado3)




