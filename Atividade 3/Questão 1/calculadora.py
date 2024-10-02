class Calculadora:
    def __init__(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
        
    def Construtor(self):
        print(f"\nValor 1 é {self.__num1} e o valor 2 é {self.__num2}.\n")
        
    def somar(self):
        print(f"A soma de {self.__num1} e {self.__num2} = {self.__num1+self.__num2}\n")
        
    def subtrair(self):
        print(f"A subtração de {self.__num1} e {self.__num2} = {self.__num1-self.__num2}\n")
        
    def multiplicar(self):
        print(f"A multiplicação de {self.__num1} e {self.__num2} = {self.__num1*self.__num2}\n")
        
    def dividir(self):
        if self.__num2 != 0:
            print(f"A divisão de {self.__num1} e {self.__num2} = {self.__num1/self.__num2:.2f}\n")
        else:
            print("O valor não pode ser igual a 0")
    
    def potencia(self):
        if self.__num1 > 0 and self.__num2 >= 0:
            print(f"A potencia de {self.__num1} e {self.__num2} = {self.__num1**self.__num2}\n")
            
    def verificarParImpar(self, valor):
        if valor % 2 == 0:
            print("O valor escolhido é par\n")
        else:
            print("O valor escolhido é ímpar\n")