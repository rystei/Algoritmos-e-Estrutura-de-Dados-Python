print("Os números ímpares entre 1 e 50 são:", end=" ")
for numero in range(1, 51):
    if numero % 2 != 0:
        print(numero, end=",")