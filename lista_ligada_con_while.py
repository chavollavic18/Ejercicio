class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.next = None

def llenar_lista_ligada(valores):
    if not valores:  
        return None

    head = Nodo(valores[0]) 
    curr = head 
    i = 1  

    while i < len(valores):
        curr.next = Nodo(valores[i]) 
        curr = curr.next 
        i += 1  

    return head  

valores = [1, 2, 3, 4, 5]

head = llenar_lista_ligada(valores)

curr = head
while curr:
    print(curr.valor, end=" -> ")
    curr = curr.next
print("No tiene valor")
