from calculadora import Calculadora
    
num1Calculadora = int(input("Digite o 1º valor: "))
num2Calculadora = int(input("Digite o 2º valor: "))

a1 = Calculadora(num1Calculadora, num2Calculadora)
a1.somar()
a1.subtrair()
a1.multiplicar()
a1.dividir()
a1.potencia()

a1.verificarParImpar(200)