class Nodo:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeadaSimples:
    def __init__(self):
        self.head = None

    def inserirNoInicio(self, nodo):
        nodo.proximo = self.head
        self.head = nodo

    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return

        nodo_atual = self.head
        while nodo_atual.proximo is not None:
            nodo_atual = nodo_atual.proximo

        nodo_atual.proximo = nodo

    def deletar(self, dado):
        if self.head is None:
            raise Exception("A lista está vazia!")

        if self.head.dado == dado:
            self.head = self.head.proximo
            return

        nodo_anterior = self.head
        for nodo in self:
            if nodo.dado == dado:
                nodo_anterior.proximo = nodo.proximo
                return
            nodo_anterior = nodo

        raise Exception(f"Nó com o dado '{dado}' não foi encontrado.")

# Exemplo de uso:
Teste = ListaEncadeadaSimples()

Teste.inserirNoInicio(Nodo('40'))
Teste.inserirNoInicio(Nodo('4'))
Teste.inserirNoInicio(Nodo('15'))
Teste.inserirNoInicio(Nodo('7'))

Teste.inserirNoFinal(Nodo('12'))
Teste.inserirNoFinal(Nodo('24'))

for nodo in Teste:
    print(nodo.dado, end=' -> ')
print('None')

Teste.deletar('4')

for nodo in Teste:
    print(nodo.dado, end=' -> ')
print('None')
