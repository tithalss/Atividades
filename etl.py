import pandas as pd
from sqlalchemy import create_engine

# Substitua 'seu_arquivo.csv' pelo caminho ou nome do seu arquivo CSV
caminho_arquivo_csv = 'data.csv'

# Use a função read_csv do Pandas para ler o arquivo CSV
df = pd.read_csv(caminho_arquivo_csv)

# Crie uma conexão com o banco de dados SQLite
# Se o arquivo do banco de dados não existir, ele será criado automaticamente
engine = create_engine('sqlite:///pepow_db.sql')

# Alimente o banco de dados com os dados do DataFrame
# Substitua 'nome_da_tabela' pelo nome desejado para a tabela no banco de dados
df.to_sql('nome_da_tabela', engine, index=False, if_exists='replace')

# Se if_exists='replace', a tabela será substituída se ela já existir
# Se if_exists='append', os dados serão adicionados à tabela existente

# Confirme a execução da operação
engine.dispose()
