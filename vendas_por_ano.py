import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Supondo que seus dados estejam em um arquivo CSV chamado "dados.csv"
dados = pd.read_csv("pedidos_clean.csv", parse_dates=['Data'])

# Criar uma coluna 'Ano' para armazenar o ano da venda
dados['Ano'] = dados['Data'].dt.year

# Filtrar os dados para incluir apenas os anos de 2023 e 2024
dados_filtrados = dados[dados['Ano'].isin([2023, 2024])]

# Agrupar por ano e calcular a soma das vendas
vendas_por_ano = dados_filtrados.groupby(['Ano', 'Mes'])['ValorTotal'].sum().unstack().fillna(0)

# Criar uma figura 3D
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Cores para cada mês
cores = ['r', 'g', 'b', 'c', 'm', 'y', 'k', 'orange', 'purple', 'pink', 'brown', 'olive']

# Coordenadas das barras
anos = vendas_por_ano.index
meses = vendas_por_ano.columns
valores = [vendas_por_ano.loc[ano].values for ano in anos]

# Adicionar barras 3D agrupadas
for i, (ano, valor, cor) in enumerate(zip(anos, valores, cores)):
    ax.bar(meses, valor, zs=i, zdir='y', color=cor, alpha=0.7, label=str(ano))

# Configurar rótulos e título
ax.set_xlabel('Mês')
ax.set_ylabel('Ano')
ax.set_zlabel('Total de Vendas (€)')
ax.set_title('Total de Vendas por Mês e Ano - Gráfico 3D Agrupado')

# Adicionar legenda
ax.legend()

# Exibir o gráfico
plt.show()
