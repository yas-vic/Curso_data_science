# Crie um exemplo de herança multinível: SerVivo → Animal → Gato
# Cada classe deve ter pelo menos um método diferente.

class SerVivo:
    def __init__(self, especie):
        self.especie = especie

class Animal (SerVivo):
    def respirar (self):
        print(f'{self.especie} está respirando')

class Gato (Animal):
    def brincar (self):
        print(f'{self.especie} está brincando')

animal_vivo = Animal("cachoro")
animal_vivo.respirar()

gato_vivo = Gato("Gato")
gato_vivo.respirar()
gato_vivo.brincar()
