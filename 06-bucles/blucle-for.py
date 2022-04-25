"""
for variable in elemento iterable (lista, rango)
    bloque de instrucciones
"""

contador = 0
resultado = 0
for contador in range(0,10):
    print("Voy por el :" + str(contador))
    resultado +=contador

print(f"El resultado es: {resultado}" )