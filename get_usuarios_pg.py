import pandas as pd

# Carregando o arquivo Excel
nome_arquivo = f'/mnt/c/Users/caiom/OneDrive/Documentos/Curso SQL/Turma 4/usuarios_postgre.xlsx'
planilha_nome = 'Sheet1'  # Nome da planilha dentro do arquivo

# Lendo o arquivo Excel e transformando em um DataFrame
df = pd.read_excel(nome_arquivo, sheet_name=planilha_nome)

# Convertendo o DataFrame em uma lista de dicionários
lista_dicionarios = df.to_dict(orient='records')

# Exibindo a lista de dicionários
for dicionario in lista_dicionarios:
    print(dicionario)
