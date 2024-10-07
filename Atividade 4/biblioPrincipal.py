from biblioteca import Biblioteca, Livro, Revista

m1 = Biblioteca("Dom Casmurro","Machado de Assis",1899, 400)
m1.detalhes()
m1.calcularIdadeItem()

n1 = Livro("O Pequeno Príncipe","Antoine de Saint-Exupéry",1945, 200)
n1.verificarTamanho()
n1.detalhes()
n1.calcularIdadeItem()

a1 = Revista("Veja","Noah", 1997, 0)
a1.verificarEdicao()
a1.detalhes()
a1.calcularIdadeItem()