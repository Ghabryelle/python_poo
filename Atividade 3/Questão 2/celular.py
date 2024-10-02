class Celular: 
    def __init__(self, numero, saldo, plano, valorMinuto=1.50):
        self.__numero = numero
        self.__saldo = saldo
        self.__plano = plano
        self.__valorMinuto = valorMinuto
        
    def Construtor(self):
        print(f"Olá, seu número atual é {self.__numero}, seu plano é {self.__plano} e o seu saldo é {self.__saldo}.")
        
    @property
    def plano(self):
        return self.__plano
    
    @plano.setter
    def plano(self, valor):
        if valor == "pós-pago":
            self.__plano = valor
        else:
            print("Você não alterou o plano!")
    
    def recarregar(self, valor):
        self.__saldo += valor
        print("Você adionou créditos ao saldo")
        
    def fazerChamada(self,duração):
        if self.__saldo > self.__valorMinuto:
            duração * self.__valorMinuto
        else:
            print("Você não possui saldo suficiente")
    
    def exibir_dados(self):
        print(f"Olá novamente, seu número atual é {self.__numero}, seu plano é {self.__plano} e o seu saldo é {self.__saldo}.")