class Queue:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.fila = []

    def add(self, elemento):
        if len(self.fila) < self.capacidade:
            self.fila.append(elemento)
            print("Elemento adicionado à fila: {}".format(elemento))
        else:
            print("A fila está cheia. Não é possível adicionar o elemento: {}".format(elemento))

    def pop(self):
        if not self.isEmpty():
            elemento_removido = self.fila.pop(0)
            print("Elemento removido da fila: {}".format(elemento_removido))
            return elemento_removido
        else:
            print("A fila está vazia. Não há elementos para remover.")
            return None

    def peek(self):
        if not self.isEmpty():
            primeiro_elemento = self.fila[0]
            print("Primeiro elemento da fila: {}".format(primeiro_elemento))
            return primeiro_elemento
        else:
            print("A fila está vazia. Não há elementos para visualizar.")
            return None

    def size(self):
        tamanho_fila = len(self.fila)
        print("Tamanho da fila: {}".format(tamanho_fila))
        return tamanho_fila

    def isEmpty(self):
        if len(self.fila) == 0:
            print("A fila está vazia.")
            return True
        else:
            print("A fila não está vazia.")
            return False

    def isFull(self):
        if len(self.fila) == self.capacidade:
            print("A fila está cheia.")
            return True
        else:
            print("A fila não está cheia.")
            return False
fila = Queue(5)
fila.isEmpty()

fila.add(10)
fila.add(20)
fila.add(30)
fila.add(40)
fila.add(50)
fila.add(60)

fila.isFull()
fila.isEmpty()

fila.peek()

fila.pop()
fila.pop()

fila.isEmpty()
fila.isFull()

fila.peek()

fila.size()
