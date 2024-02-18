import pandas as pd

df = pd.read_csv('dados_pedidos.csv', sep=',')

# renomear a coluna
df = df.rename(columns={'País': 'Pais'})

# excluir linhas vazias
df= df.dropna(how='all') #apagar linhas completamente em braco/vazias

# excluir linhas duplicadas
#df= df.drop_duplicates()

# excluir espaços em branco no inicio e fim de cada coluna
df= df.rename(columns=lambda x: x.strip()) #strip: elimina espaços em branco

# converter dados para float
df['ValorTotal'] = df['ValorTotal'].astype(float)  # desconsidera . e , e converte o tipo de dado (.astype(float))

# criar e gravar novo ficheiro formatado/tratado
df.to_csv('pedidos_clean.csv', index=False)
