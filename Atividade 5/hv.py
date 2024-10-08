class Personagem:
    def __init__(self, nome, rank, vida=100):
        self._nome = nome
        self._vida = vida
        self._rank = rank
        
    def receberDano(self, dano):
        self._vida -= dano
        print(f"Você tomou {dano} de dano.")
        
    def verificarVida(self):
        if self._vida == 0:
            print("Você está morto.")
        else:
            print("Você está vivo.")
    
    def detalhes(self):
        print(f"Nome: {self._nome} \nVida: {self._vida}\n")
        
class Heroi(Personagem):
        def __init__(self, nome, rank, vida, identidadeSecreta, energia=50):
            super().__init__(nome, rank, vida)
            self._identidadeSecreta = identidadeSecreta
            self._energia = energia
            
        def executarHabilidade(self, tipoHabilidade):
            pe = 10
            print(f"Olá {self._identidadeSecreta}, sua habilidade é {tipoHabilidade}. Você tinha um total de {self._energia}, você consumiu {pe} de energia.")
        
        def recarregarEnergia(self):
            re = 5
            self._energia -= 10
            print(f"Você passou a ter {self._energia} e você aumentou sua energia para {self._energia + re}.\n")
            
        def chamarAliado(self, nomeAliado):
            print(f"O aliado {nomeAliado} foi convocado, com sua habilidade impressionante de lançar correntes elétricas que atordoam e causam dano em todos os inimigos ao redor.\n")
            
class Vilao(Personagem):
        def __init__(self, nome, rank, vida, malicia = 70):
            super().__init__(nome, rank, vida)
            self._malicia = malicia
        
        def deferirGolpes(self, tipoGolpe):
            print(f"Você usou o golpe {tipoGolpe}, que foi potencialiado pela malícia. \nUtilizou: {self._malicia} malícia \nRestando apenas {70 - self._malicia} malícia.")
        
        def planejarArmadilha(self, tipoArmadilha):
            print(f"O vilão está planejando uma armadilha! A armadilha é {tipoArmadilha}.\n")
            
        def fugir(self, tipoFulga):
            print(f"O vilão conseguiu escapar usando o método {tipoFulga}, convocando uma tempestade de lâminas ou espinhos que cria uma barreira de defesa enquanto ele escapa para longe.\n")