from hv import Personagem, Heroi, Vilao

print("Bem vindo ao jogo dos Heróis e Vilões! \n")
nome = input("Nome: ")
rank = input("Rank: ")


pessoa1 = Personagem (nome, rank)
pessoa1.receberDano(7)
pessoa1.verificarVida()
pessoa1.detalhes()

heroi1 = Heroi("Yuri Gabriel", "Avançado", 200, "Guardião Gláctico", 80)
heroi1.executarHabilidade("Controle do Tempo")
heroi1.recarregarEnergia()
heroi1.chamarAliado("Mestre das Correntes")
heroi1.receberDano(30)
heroi1.verificarVida()
heroi1.detalhes()

vilao1 = Vilao("Alana", "Avançado", 600)
vilao1.deferirGolpes("Manipulação das Sombras")
vilao1.planejarArmadilha("Roubo de incapaz")
vilao1.fugir("Chuva de Lâminas")
vilao1.receberDano(10)
vilao1.verificarVida()
vilao1.detalhes()