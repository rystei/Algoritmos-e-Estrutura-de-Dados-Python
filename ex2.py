while True:
    letra = input("Digite uma letra (ou 'sair' para encerrar): ").lower()

    if letra == 'sair':
        print("Programa encerrado.")
        break

    if letra.isalpha() and len(letra) == 1:
        if letra in 'aeiou':
            print(f"A letra '{letra}' é uma vogal.")
        else:
            print(f"A letra '{letra}' é uma consoante.")
    else:
        print("Por favor, digite apenas uma letra.")