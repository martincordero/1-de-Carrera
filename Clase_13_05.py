def palabras(frase):
    '''
    Función que recibe una frase y devuelve un diccionario con las palabras
    '''
    palabras = frase.split()
    longitud = map(len, palabras)
    palabras = dict(zip(palabras, longitud))
    return palabras

frase = input('Introduce una frase: ')
print(palabras(frase))