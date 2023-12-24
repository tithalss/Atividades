class ContaBancaria:
    def __init__(self, nome, saldo_inicial, senha):
        self.nome = nome
        self.saldo = saldo_inicial
        self.senha = senha

    def cadastrar_cliente(self, nome, saldo_inicial, senha):
        self.nome = nome
        self.saldo = saldo_inicial
        self.senha = senha
        print(f"Cliente {self.nome} cadastrado com sucesso!")

    def depositar(self, valor, senha_digitada):
        if senha_digitada == self.senha:
            if valor > 0:
                self.saldo += valor
                print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
            else:
                print("Valor de depósito inválido")
        else:
            print("Senha incorreta")

    def sacar(self, valor, senha_digitada):
        if senha_digitada == self.senha:
            if valor > 0 and valor <= self.saldo:
                self.saldo -= valor
                print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
            else:
                print("Saldo insuficiente")
        else:
            print("Senha incorreta")

    def consultar_saldo(self):
        print(f"Saldo atual da conta de {self.nome}: R${self.saldo}")


if __name__ == '__main__':
    conta1 = ContaBancaria("Thales", 1000, "minhasenha")
    conta1.consultar_saldo()
    conta1.depositar(500, "minhasenha")
    conta1.sacar(200, "minhasenha")
    conta1.consultar_saldo()

    # Adicionando a funcionalidade de cadastrar cliente
    conta1.cadastrar_cliente("NovoCliente", 200, "novasenha")

    # Testando com o novo cliente
    conta1.depositar(100, "novasenha")
    conta1.sacar(50, "novasenha")
    conta1.consultar_saldo()
