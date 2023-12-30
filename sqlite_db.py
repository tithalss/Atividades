import sqlite3

def function_dml(db, sql):
    try:
        # Conecta ao banco de dados
        arq = db + '.sql'
        conn = sqlite3.connect(arq)
        cursor = conn.cursor()
        
        # Executa e comita o comando
        cursor.execute(sql)  
        conn.commit()
    
        # Extrai a primeira palavra do comando
        fw = sql.strip().split()[0].lower()
    
        # Condiciona a menseagem a partir da variável "fw"
        if fw == 'insert':
            print("Registros inseridos.")
        elif fw == 'update':
            print("Tabela atualizada.")
        elif fw == 'delete':
            print("Registros removidos.")
        elif fw == 'create':
            print("Tabela criada")
        elif fw == 'alter':
            print("Tabela alterada")
        elif fw == 'select':
            #Transforma a tupla em uma lista e retorna os valores consultados
            linhas = cursor.fetchall()
            for linha in linhas:
                print(linha)
        else:
            print("Comando não reconhecido.")

    except sqlite3.Error as error:
        print("Erro ao executar a query:", error)

    #Fecha o cursor e a conexão
    cursor.close()
    conn.close()

if __name__ =='__main__':
    database = input('Escolha o banco de dados: ')
    
    while True:
        op = input('1 - Registrar Campeão\n2 - Operações SQL\n3 - Sair\n-:')
        
        if op == "1":
            nome = input('Nome: ')
            raca = input('Raça: ')
            regiao = input('Região: ')
            funcao = input('Função: ')
            poder = int(input('Poder: '))
            comando = f'''INSERT INTO campeoes (nome, raca, regiao, funcao, poder) VALUES ('{nome}', '{raca}', '{regiao}', '{funcao}', '{poder}')'''
            function_dml(database, comando)
            
        elif op == "2":
            sql = input("SQL: ")
            function_dml(database, sql)
            
        elif op == "3":
            break
        
        else:
            print('Opção inválida')
    