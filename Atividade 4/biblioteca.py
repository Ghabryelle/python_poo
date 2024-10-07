class Biblioteca:
    def __init__(self, titulo, autor, anoPublicacao, numeroPagina):
        self._titulo = titulo
        self._autor = autor
        self._anoPublicacao = anoPublicacao
        self._numeroPagina = numeroPagina
        
    def detalhes(self):
        print(f"O título do item é {self._titulo}, autor {self._autor} e seu ano de publicação da obra é {self._anoPublicacao}.")
        
    def calcularIdadeItem(self):
        idade = 2024 - self._anoPublicacao
        
        if idade > 70:
            print(f"Esse item é antigo. O item indicado é {self._titulo}, seu ano de publicação é {self._anoPublicacao} e sua idade é de {idade} anos.\n")
            
        elif idade > 30 and idade < 70:
            print(f"Esse item é recente. O item indicado é {self._titulo}, seu ano de publicação é {self._anoPublicacao} e sua idade é de {idade} anos.\n")
            
        elif idade < 30:
            print(f"Esse item é comtemporâneo. O item indicado é {self._titulo}, seu ano de publicação é {self._anoPublicacao} e sua idade é de {idade} anos.\n")
        
class Livro(Biblioteca):
    def verificarTamanho(self):
        if self._numeroPagina > 300:
            print(f"O Livro {self._titulo}, é um livro longo, contendo {self._numeroPagina} páginas.")
        elif self._numeroPagina < 300:
            print(f"O Livro {self._titulo}, é um livro curto, contendo {self._numeroPagina} páginas.")
            
class Revista(Biblioteca):
    def verificarEdicao(self):
        if self._anoPublicacao <= 1998:
            print(f"A Revista {self._titulo} do ano {self._anoPublicacao} é uma edição especial.")
        elif self._anoPublicacao > 1998:
            print(f"A Revista {self._titulo} do ano {self._anoPublicacao} não é uma edição especial.")