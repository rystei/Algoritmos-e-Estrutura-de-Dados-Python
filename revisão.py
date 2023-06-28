class Pilha:
    def __init__(self):
        self.items = []

    def esta_vazia(self):
        return len(self.items) == 0

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if self.esta_vazia():
            return None
        return self.items.pop()

    def topo(self):
        if self.esta_vazia():
            return None
        return self.items [-1]

    def tamanho(self):
        return len(self.items)

pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

print(pilha.topo())

pilha.desempilhar()
print(pilha.topo())

print(pilha.esta_vazia())
print(pilha.tamanho())


