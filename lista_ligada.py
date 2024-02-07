class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.next = None

def lista_a_lista_ligada(e):
    if not e: 
        return None

    head = Nodo(e[0])  
    curr = head  
    i = 1  
    while i < len(e):
        curr.next = Nodo(e[i]) 
        curr = curr.next 
        i += 1 

    return head  

e = [1, 2, 3, 4, 5]

head = lista_a_lista_ligada(e)

curr = head
while curr:
    print(curr.valor, end=" -> ")
    curr = curr.next
print("None")
