from conta import Conta

minhaConta = Conta(321, "Epamenondas Soares", 2000)

minhaConta.relatorio()

#minhaConta.limite = 9000

#minhaConta.relatorio()
minhaConta.setLimite(8000)
minhaConta.relatorio()

print(f"O seu limíte atual é {minhaConta.getLimite()}")

minhaConta.depositor(200)
minhaConta.relatorio()

minhaConta.sacar(150)
minhaConta.relatorio()