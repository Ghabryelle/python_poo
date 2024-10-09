import sqlite3

#Passo1 - Conexão com o banco 
conexao = sqlite3.connect("departamento.db")

#Passo2 - Verificar de a tabela existe ou não
tabela = """
CREATE TABLE IF NOT EXISTS funcionario(
    codigo INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VACHAR(100),
    salario FLOAT,
    cargo VACHAR(100)    
);
"""
#Passo3 - Acessar o objeto cursor da biblioteca squilite3, para manipular dados do banco
consulta = conexao.cursor()

#Passo4 - Executar o comando de criação da tabela
consulta.execute(tabela)

#Passo5 - Criando comando SQL para consultar os dados na tabela
sql = "SELECT * FROM funcionario"

#Passo6 - Executar o comando sql
consulta.execute(sql)

#Passo7 - Exibir dados da tabela
resultado = consulta.fetchall() #Fetchall irá trazer todos os registros que existem na tabela do banco de dados

for itens in resultado:
    print(f"Código: {itens[0]}, Nome: {itens[1]}")

#Passo8 - Encerrar conexão
conexao.close()