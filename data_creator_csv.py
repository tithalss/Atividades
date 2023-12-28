import csv

nome_arquivo = "data.csv"

cabecalho = ["Nome", "Idade", "Cidade", "Profissao", "Salario"]

dados = [
    ["Alice", 25, "Sao Paulo", "Engenheira", 5400],
    ["Carlos", 30, "Rio de Janeiro", "Professor", 2500],
    ["Carol", 21, "Salvador", "Estudante", 900],
    ["David", 18, "Porto Alegre", "Programador", 2890],
    ["Evellyn", 26, "Curitiba", "Advogada", 4100],
    ["Alicia", 80, "Sao Paulo", "Medica", 90250],
    ["Bob", 30, "Rio de Janeiro", "Mecanico", 8700],
    ["Roberta", 22, "Salvador", "Acompanhante", 50120],
    ["Davi", 55, "Porto Alegre", "Empresario", 542000],
    ["Fernanda", 36, "Curitiba", "Contador", 30201],
    ["Jonas", 41, "Brasilia", "Arquiteto", 9852]
]

with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)

    escritor_csv.writerow(cabecalho)

    escritor_csv.writerows(dados)
    
