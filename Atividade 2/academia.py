class Aluno: 
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
        
    def exibirDados(self):
        print(f"Olá {self.nome}, você tem {self.idade} anos, possui {self.peso} Kg e tem {self.altura:.2f} de altura.")
        
    def calcularImc(self):    
        print(f"Seu índice de massa corporal é {self.peso/(self.altura*self.altura):.2f}\n")  
        
      