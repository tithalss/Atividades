import sqlite3

class ContaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Valor de depósito inválido")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado. Saldo atual: R${self.saldo}")
        else:
            print("Saldo insuficiente")

def function_dml():
    try:
        # Conecta ao banco de dados
        conn = sqlite3.connect('clientes.sql')
        cursor = conn.cursor()
        
        # Executa o comando
        cursor.execute('''CREATE TABLE if not exists clientes (NUMERO_CONTA INTEGER PRIMARY KEY, NOME_COMPLETO VARCHAR(50) NOT NULL, DATA_NASCIMENTO DATE NOT NULL, CPF VARCHAR(11) UNIQUE NOT NULL, EMAIL VARCHAR(50) UNIQUE NOT NULL, SALDO DECIMAL(10, 2) DEFAULT 0.0, SENHA VARCHAR(50) NOT NULL)''')  
        conn.commit()
    
    except sqlite3.Error as error:
        print("Erro ao executar a query main:", error)

    #Fecha o cursor e a conexão
    cursor.close()
    conn.close()
   
def main():
    function_dml()
    conn = sqlite3.connect('clientes.sql')
    cursor = conn.cursor()
    
    try:
        while True:
            print("\nOpções:")
            print("1 - Login")
            print("2 - Cadastre-se")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                email = str(input("E-mail: "))
                senha = str(input("Senha: "))

                cursor.execute('''SELECT SENHA FROM clientes WHERE EMAIL = ?''', (email))
                senha_bd = cursor.fetchone()


                if senha_bd == senha:
                    cursor.execute('''SELECT SALDO FROM clientes WHERE EMAIL = ?''', (email))
                    saldo = cursor.fetchone()

                    print(f"Saldo disponível: {saldo}")

                    while True:
                        conta = ContaBancaria(saldo)

                        print("\nOpções:")
                        print("1 - Tranferir")
                        print("2 - Depositar")
                        print("3 - Sair")

                        op = input("Escolha uma opção: ")

                        if op == "1":
                            pass

                        elif op =="2":
                            valor = float(input("Valor:"))
                            conta.depositar(valor)

                        elif op =="3":
                            break
                        
                else:
                    print("Email ou senha inválidos")

            elif opcao == "2":
                nome = input("Nome completo: ")
                data = input("Data de nascimento: ")
                cpf = input("CPF: ")
                email = input("E-mail: ")
                senha = input("Senha: ")

                cursor.execute('''INSERT INTO clientes (NOME_COMPLETO, DATA_NASCIMENTO, CPF, EMAIL, SENHA) VALUES (?, ?, ?, ?, ?)''', (nome, data, cpf, email, senha))
                conn.commit()
                print('Cadastro realizado com sucesso.')
            
            elif opcao == "3":
                break
            
            else:
                print("Opção inválida. Tente novamente.")
    
    except sqlite3.Error as error:
        print("Erro ao executar a query:", error)
        
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()