import pandas as pd
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('pedidos_clean.csv')  # Substitua 'pedidos_clean.csv' pelo nome real do seu arquivo

# Converter a coluna 'Data' para o tipo datetime
df['Data'] = pd.to_datetime(df['Data'])

# Extrair o ano da coluna 'Data'
df['Ano'] = df['Data'].dt.year

# Agrupar por país e calcular o total de vendas
total_vendas_por_pais = df.groupby(['Pais', 'Ano'])['ValorTotal'].sum().reset_index()

# Criar gráfico de barras animado com Matplotlib
fig, ax = plt.subplots(figsize=(10, 6))

for ano in total_vendas_por_pais['Ano'].unique():
    dados_ano = total_vendas_por_pais[total_vendas_por_pais['Ano'] == ano]
    ax.bar(dados_ano['Pais'], dados_ano['ValorTotal'], label=str(ano))

# Adicionar rótulos e título
ax.set_xlabel('País')
ax.set_ylabel('Total de Vendas (€)')
ax.set_title('Total de Vendas por País ao Longo do Tempo')

# Adicionar legenda
ax.legend()

# Ajustar layout para melhor visualização do texto
plt.tight_layout()

# Exibir o gráfico
plt.show()