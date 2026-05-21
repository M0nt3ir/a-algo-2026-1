class Paciente:
    """
    Representa um paciente da fila de triagem.
    """

    def __init__(self, nome, nivel_dor):
        """
        Inicializa um paciente.

        Args:
            nome (str): Nome do paciente.
            nivel_dor (int): Nível de dor do paciente.
        """
        self.nome = nome
        self.nivel_dor = nivel_dor

    def __repr__(self):
        """
        Retorna representação textual do paciente.
        """
        return f"{self.nome} ({self.nivel_dor})"


class MaxHeap:
    """
    Implementa uma fila de prioridade utilizando Max-Heap.
    """

    def __init__(self):
        """
        Inicializa o heap vazio.
        """
        self.heap = []

    def pai(self, indice):
        """
        Retorna índice do pai.
        """
        return (indice - 1) // 2

    def filho_esquerda(self, indice):
        """
        Retorna índice do filho esquerdo.
        """
        return 2 * indice + 1

    def filho_direita(self, indice):
        """
        Retorna índice do filho direito.
        """
        return 2 * indice + 2

    def trocar(self, indice_a, indice_b):
        """
        Troca dois elementos do heap.
        """
        self.heap[indice_a], self.heap[indice_b] = (
            self.heap[indice_b],
            self.heap[indice_a]
        )

    def inserir(self, paciente):
        """
        Insere um paciente no heap.
        """
        self.heap.append(paciente)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, indice):
        """
        Move o elemento para cima no heap.
        """
        while (
            indice > 0 and
            self.heap[self.pai(indice)].nivel_dor <
            self.heap[indice].nivel_dor
        ):
            indice_pai = self.pai(indice)

            self.trocar(indice, indice_pai)

            indice = indice_pai

    def heapify_down(self, indice):
        """
        Move o elemento para baixo no heap.
        """
        maior = indice

        esquerda = self.filho_esquerda(indice)
        direita = self.filho_direita(indice)

        if (
            esquerda < len(self.heap) and
            self.heap[esquerda].nivel_dor >
            self.heap[maior].nivel_dor
        ):
            maior = esquerda

        if (
            direita < len(self.heap) and
            self.heap[direita].nivel_dor >
            self.heap[maior].nivel_dor
        ):
            maior = direita

        if maior != indice:
            self.trocar(indice, maior)

            self.heapify_down(maior)

    def atender_paciente(self):
        """
        Remove e retorna o paciente de maior prioridade.
        """
        if not self.heap:
            return None

        self.trocar(0, len(self.heap) - 1)

        paciente = self.heap.pop()

        if self.heap:
            self.heapify_down(0)

        return paciente

    def alterar_prioridade(self, indice, novo_nivel_dor):
        """
        Altera a prioridade de um paciente.

        Args:
            indice (int): Índice do paciente no heap.
            novo_nivel_dor (int): Novo nível de dor.
        """
        nivel_antigo = self.heap[indice].nivel_dor

        self.heap[indice].nivel_dor = novo_nivel_dor

        if novo_nivel_dor > nivel_antigo:
            self.heapify_up(indice)
        else:
            self.heapify_down(indice)

    def exibir_heap(self):
        """
        Exibe os elementos do heap.
        """
        print(self.heap)


def main():
    """
    Executa teste do sistema de triagem.
    """

    fila_prioridade = MaxHeap()

    fila_prioridade.inserir(Paciente("Mariana", 3))
    fila_prioridade.inserir(Paciente("Harry", 9))
    fila_prioridade.inserir(Paciente("Justin", 5))
    fila_prioridade.inserir(Paciente("Ariana", 7))

    print("Heap inicial:")
    fila_prioridade.exibir_heap()

    print("\nAlterando prioridade de Ariana para 10...")

    fila_prioridade.alterar_prioridade(3, 10)

    print("\nHeap atualizado:")
    fila_prioridade.exibir_heap()

    paciente_atendido = fila_prioridade.atender_paciente()

    print("\nPaciente atendido:")
    print(paciente_atendido)


if __name__ == "__main__":
    main()