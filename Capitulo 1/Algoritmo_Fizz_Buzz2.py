for numero in range(1,100):
    if int(numero) % 3 == 0 and int(numero) % 5 == 0:
        print("FIZZBUZZ,")
    elif int(numero) % 3 ==0:
        print("FIZZ,")
    elif int(numero) % 5 == 0:
        print("Buzz,")
    else:
        print(str(numero) + ",")