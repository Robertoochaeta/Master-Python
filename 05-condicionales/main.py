#Ejemplo1#"######

color = "rojo"
#color= input("Adivina el color favorito: ")
if color== "rojo":
    print("El color es rojo")
else:
    print("El color es incorrecto")
print("\n####################################################################")
#Operadores de comparacion

#year = int(input("¿En que año estamos?"))
#if year < 2022:
 #   print("Estamos antes de 2022")
#else:
  #  print("Es un año inferior a 2022")

#Ejemplo 3
print("\n####################################################################")
nombre = 'Roberto'
ciudad = 'San Francisco'
continente= 'Oceania'
edad = 12
mayoriaEdad=18

if edad >= mayoriaEdad:
    print(f"{nombre} Es mayor de edad")
    if continente != "America":
        print("El Usuario no es americano")
    else:
        print(f"es Americano y la ciudad es {ciudad}")

else:
    print(f" {nombre} No es Mayor de edad")

print("\n###############Ejemplo 4 ###################")

dia = int(input("Introduce el dia de la semana: "))
"""

if dia ==1:
    print("Es Lunes")
else:
    if dia ==2:
        print("Es Martes")
    else:
        if dia ==3:
            print("Es Miercoles")
        else:
            if dia == 4:
                print("Es Jueves")
            else:
                if dia == 5:
                    print("Es viernes")
                else:
                    print("Es fin de Semana")
"""
if dia == 1:
    print("Es Lunes")
elif dia ==2:
    print("Es Martes")
elif dia ==3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
else:
    print("Es Fin de semana")

print("\U0001F602")

print("################################Ejemlo 5######################")
edadMinima = 18
edadMaxima = 65
edadReal = int(input("Ingresa tu edad: "))

if edadReal >= 18 and edadReal <= 65:
    print("Esta en edad de trabajar")
else:
    print("No esta en edad de trabajar")

#print("\U0001F60D")

print("################################Ejemlo 5######################")
pais = input("Ingresa el pais: ")
if pais== "Guatemala" or pais == "Colombia" or pais == 'España':
    print(f"{pais} es un pais de habla hispana")
else:
    print(f"{pais} No es un pais de habla hispana")
print("##################################################################")
pais = input("Ingresa el pais: ")
if not(pais== "Guatemala" or pais == "Colombia" or pais == 'España'):
    print(f"{pais}  es un pais de habla hispana")
else:
    print(f"{pais} Es un pais de habla hispana")

print("""""""""""""""""""""""""""""""")
pais = input("Ingresa el pais: ")
if pais!= "Guatemala" and pais !=  "Colombia" and pais != 'España':
    print(f"{pais} No es un pais de habla hispana")
else:
    print(f"{pais} es un pais de habla hispana")

