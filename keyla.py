class Node:
    def __init__(self, patient_id, color):
        self.patient_id = patient_id
        self.color = color
        self.next = None

class PatientQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def inserirSemPrioridade(self, node):
        if self.is_empty():
            self.head = node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = node

    def inserirComPrioridade(self, node):
        if self.is_empty():
            self.head = node
        else:
            prev = None
            current = self.head
            while current is not None and (current.color == 'A' and node.color == 'V'):
                prev = current
                current = current.next
            if prev is None:
                node.next = self.head
                self.head = node
            else:
                prev.next = node
                node.next = current

    def inserir(self):
        color = input("Digite a cor do cartão (A para amarelo, V para verde): ").upper()
        if color not in ['A', 'V']:
            print("Cor inválida. Por favor, insira 'A' para amarelo ou 'V' para verde.")
            return

        if color == 'A':
            patient_id = int(input("Digite o número do cartão amarelo (>= 201): "))
            if patient_id < 201:
                print("Número inválido para cartão amarelo. Deve ser >= 201.")
                return
        else:
            patient_id = int(input("Digite o número do cartão verde (>= 1): "))
            if patient_id < 1:
                print("Número inválido para cartão verde. Deve ser >= 1.")
                return

        new_node = Node(patient_id, color)
        if self.is_empty():
            self.head = new_node
        else:
            if color == 'V':
                self.inserirSemPrioridade(new_node)
            else:
                self.inserirComPrioridade(new_node)
        print(f"Paciente com ID {patient_id} e cartão {color} adicionado à fila.")

    def imprimirListaEspera(self):
        if self.is_empty():
            print("A fila está vazia.")
        else:
            current = self.head
            while current is not None:
                print(f"Paciente ID: {current.patient_id}, Cor: {current.color}")
                current = current.next

    def atenderPaciente(self):
        if self.is_empty():
            print("Nenhum paciente na fila para atendimento.")
        else:
            next_patient = self.head
            self.head = self.head.next
            print(f"Chamando paciente para atendimento: ID {next_patient.patient_id}, Cor {next_patient.color}")

    def display_queue(self):
        self.imprimirListaEspera()

def main():
    queue = PatientQueue()

    while True:
        print("\nMenu de opções:")
        print("1. Adicionar paciente")
        print("2. Mostrar pacientes na fila")
        print("3. Chamar paciente")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            queue.inserir()
        elif choice == '2':
            queue.imprimirListaEspera()
        elif choice == '3':
            queue.atenderPaciente()
        elif choice == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()

