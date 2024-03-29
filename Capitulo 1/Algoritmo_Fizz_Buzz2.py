listado = input ("Ingrese una lista de numeros : ")
listado = list(listado)
print(type(listado))
for numero in listado:
    if int(numero) % 3 and int(numero) % 5:
        print("FIZZBUZZ,")
    elif int(numero) % 3 ==0:
        print("FIZZ,")
    elif int(numero) % 5 == 0:
        print("Buzz,")
    else:
        print(numero + ",")