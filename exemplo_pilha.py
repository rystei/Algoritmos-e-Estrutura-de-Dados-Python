pilha = [1, 1, 2, 3, 5]
print("pilha ", pilha)

pilha.append(8)
print("inserindo um elemento ", pilha)

pilha.append(13)
print("inserindo outro elemento ", pilha)

pilha.pop()
print(" removendo um elemento: ", pilha)

pilha.pop()
print(" removendo um elemento: ", pilha)

# acessando o topo da pilha
print("topo: ", pilha[len(pilha) - 1])
