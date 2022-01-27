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
edad = 22
mayoriaEdad=18

if edad >= mayoriaEdad:
    print(f"{nombre} Es mayor de edad")
    if continente != "America":
        print("El Usuario no es americano")
    else:
        print(f"es Americano y la ciudad es {ciudad}")

else:
    print(f" {nombre} No es Mayor de edad")