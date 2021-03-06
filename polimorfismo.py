
class Persona():

    def __init__(self, nombre):
        self.nombre = nombre

    def avanzar(self):
        print('Caminando')
    
class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanzar(self):
        print('Cicleando equis de')

def main():
    persona = Persona('Daniel')
    persona.avanzar()

    ciclista = Ciclista('Thomás')
    ciclista.avanzar()

if __name__ == '__main__':
    main()
