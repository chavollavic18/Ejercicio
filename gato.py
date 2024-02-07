from objetos import amimal
class gato(amimal):
    def _int_(self, nombre):
        super()._int_(nombre)

        def maullar():
            print('miau')

            if __name__ == '_main_':

                gato = gato('michi')
                print(gato)
                gato.maullar
