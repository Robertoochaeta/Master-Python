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