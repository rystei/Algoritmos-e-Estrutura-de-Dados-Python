def somaNat(n):
    if n == 0:
        return 0
    else:
        return n + somaNat(n - 1)

numero = int(input("Digite um número natural: "))
resultado = somaNat(numero)
print("A soma dos números naturais até", numero, "é:", resultado)