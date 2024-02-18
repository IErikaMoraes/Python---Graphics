import matplotlib.pyplot as plt
import pandas as pd

# Ler o arquivo CSV
df = pd.read_csv('pedidos_clean.csv')  # Substitua 'pedidos_clean.csv' pelo nome real do seu arquivo

# Substituir valores nulos na coluna 'MTDEnvio' por 'Desconhecido'
df['MTDEnvio'] = df['MTDEnvio'].fillna('Desconhecido')

# Contar a frequência de cada método de envio
contagem_metodos_envio = df['MTDEnvio'].value_counts()

# Criar um gráfico de barras agrupadas
fig, ax = plt.subplots(figsize=(12, 8))
contagem_metodos_envio.plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)

# Adicionar rótulos e título
plt.xlabel('Método de Envio')
plt.ylabel('Quantidade de Pedidos')
plt.title('Quantidade de Pedidos por Método de Envio')

# Adicionar valores nas barras
for i, v in enumerate(contagem_metodos_envio):
    ax.text(i, v + 5, str(v), ha='center', va='bottom')

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
