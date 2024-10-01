from academia import Aluno


a1 = Aluno("Yuri",17,60,1.70)
a1.exibirDados()
a1.calcularImc()

nomeAluno = input("Informe seu nome: ")
idadeAluno = input("Informe sua idade: ")
pesoAluno = float(input("Informe seu peso: "))
alturaAluno = float(input("Informe sua altura: "))

a2 = Aluno(nomeAluno, idadeAluno, pesoAluno, alturaAluno)
a2.exibirDados()
a2.calcularImc()