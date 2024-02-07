''' Modulo contenedor de clase Nodo para listas ligadas'''
class Nodo:
    ''' Clase de Nodo'''
    def _init_(self, val:int):
        ''' iniciador de clase'''
        self.val = val 
        self.next = None
        def _str_(self)-> str:
            if self.val:
              return f'Valor del nodo = {self.val}'
        
        return f'El nodo no tiene valor'