def encontrar_posicoes(lista, elemento):
    posicoes = []
    for i in range(len(lista)):
        if lista[i] == elemento:
            posicoes.append(i)
    return posicoes

L = [1, 2, 3, 1, 1, 2, 1, 0, 0, 2]

elementos_unicos = set(L)  # Obter os elementos únicos da lista

for elemento in elementos_unicos:
    posicoes = encontrar_posicoes(L, elemento)
    print(f'O elemento {elemento} aparece nas posições: {posicoes}')
