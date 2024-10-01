class Livro: 
    def __init__(self, titulo, autor, anoPublicacao):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        
    def exibirInformacao(self):
        print(f"O título do livro é {self.titulo}, o(a) autor(a) é {self.autor} e o ano de publicação é {self.anoPublicacao}.")
        
    def verificarIdadeLivro(self):
        if self.anoPublicacao < 1974:
            print("Esse livro é um clássico.")
        else:
            print("Ainda não é considerado um clássico")
