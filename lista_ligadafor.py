class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.next = None

def llenar_lista_ligada(valores):
    if not valores:  # Verificar si la lista está vacía
        return None

    head = Nodo(valores[0])  # Crear el nodo inicial con el primer valor de la lista
    curr = head  # Establecer el nodo actual al inicio de la lista ligada

    for valor in valores[1:]:
        curr.next = Nodo(valor)  # Crear un nuevo nodo con el valor actual
        curr = curr.next  # Mover el puntero actual al siguiente nodo

    return head  # Devolver el nodo inicial de la lista ligada

# Lista de entrada
valores = [1, 2, 3, 4, 5]

# Crear la lista ligada a partir de la lista de entrada
head = llenar_lista_ligada(valores)

# Imprimir la lista ligada
curr = head
while curr:
    print(curr.valor, end=" -> ")
    curr = curr.next
print("None")
