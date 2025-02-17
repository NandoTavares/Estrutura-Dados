class Lista:
    def __init__(self, max_size=100):
        self.max_size = max_size
        self.elementos = []

    def esta_vazia(self):
        return len(self.elementos) == 0

    def esta_cheia(self):
        return len(self.elementos) == self.max_size

    def obter_tamanho(self):
        return len(self.elementos)

    def obter_elemento(self, pos):
        if pos < 0 or pos >= len(self.elementos):
            raise IndexError("Posicao invalida")
        return self.elementos[pos]

    def modificar_elemento(self, pos, valor):
        if pos < 0 or pos >= len(self.elementos):
            raise IndexError("Posicao invalida")
        self.elementos[pos] = valor

    def inserir(self, pos, valor):
        if self.esta_cheia():
            raise OverflowError("Lista cheia")
        if pos < 0 or pos > len(self.elementos):
            raise IndexError("Posicao invalida")
        self.elementos.insert(pos, valor)

    def remover(self, pos):
        if self.esta_vazia():
            raise ValueError("Lista vazia")
        if pos < 0 or pos >= len(self.elementos):
            raise IndexError("Posicao invalida")
        self.elementos.pop(pos)

if __name__ == "__main__":
    lista = Lista()
    lista.inserir(0, 10)
    lista.inserir(1, 20)
    lista.inserir(2, 30)
    
    print("Elemento na posicao 1:", lista.obter_elemento(1))
    lista.modificar_elemento(1, 25)
    print("Novo elemento na posicao 1:", lista.obter_elemento(1))
    
    lista.remover(1)
    print("Elemento na posicao 1 apos remocao:", lista.obter_elemento(1))
