class Calculadora:
    def adicionar(self, a, b):
        # Graziele Fagundes Martins
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        #Otávio Rocha
        return a * b

    def dividir(self, a, b):
        # Miguel Rodrigues Botelho
        if b == 0:
            return "Não é possível dividir por zero"
        return a / b

