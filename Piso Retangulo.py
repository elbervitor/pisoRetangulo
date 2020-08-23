''' Classe Retangulo
Atributos: Lado A, Lado B
Metodos:   Mudar Lado A, Mudar Lado B, Retornar Lados, Calcular Area e Perimentro

Programa:  Utilize classe Retangulo. Usuario informa medida de local, e dps cria objeto
com medidas e calcular quantos pisos serão necessarios '''



class Piso_retangulo:
    def __init__ (self, altura, largura):
        self.ladoA = altura
        self.ladoB = largura
        self.area = self.ladoA * self.ladoB
        self.perimetro = (self.ladoA*2) + (self.ladoB*2)
        print('Construtor criado')

    def mudaAltura (self, nova_altura):
        self.ladoA = nova_altura

    def mudalargura (self, nova_largura):
        self.ladoB = nova_largura

    def  calcArea (self):
        self.area = self.ladoA * self.ladoB
        print (self.area)

    def calcPerimetro (self):
        self.perimetro = (self.ladoA*2) + (self.ladoB*2)
        print (self.perimetro)

    def getArea (self):
        return self.area
print ('''
        Primeiro, vamos pegar as medidas de um piso retangulo
        Segundo, calcular quantos precisamos pra uma area que você via indicar!
''')
print ("Quais as medidas do piso?")
pAltura = int(input("Altura: "))
pLargura = int(input("Largura: "))

piso = Piso_retangulo(pAltura,pLargura)
piso.calcPerimetro()
piso.calcArea()
pArea = piso.getArea()
print ("Quais as medidas locais?")

tAltura = int(input("Altura: "))
tLargura = int(input("Largura: "))

qtd = (tAltura*tLargura) /  pArea
print ("Serão necessarios ",qtd,"pisos")
                 
