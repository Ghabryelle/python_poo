from pessoa import Pessoa, Aluno, Professor

pessoa1 = Pessoa("Naikolaison", 93)
pessoa1.info()

aluno1 = Aluno("Jully",17, 2403923)
aluno1.info()
aluno1.estudar()

professor1 = Professor("Daniel", 20, "História")
professor1.info()
professor1.ensinar()