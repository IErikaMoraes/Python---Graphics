import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ler o arquivo CSV
df = pd.read_csv('pedidos_clean.csv', sep=',', encoding='latin1')

# Remover as linhas onde o método de pagamento é "Teste"
df = df[df['MTDPagamento'] != 'Teste']

# Contar a frequência de cada método de pagamento
frequencia_pagamentos = df['MTDPagamento'].value_counts()

# Criar uma paleta de cores para os segmentos do gráfico
cores = plt.cm.tab10.colors

# Criar uma figura com o tamanho desejado e adicionar subplots para mais flexibilidade
fig, ax = plt.subplots(figsize=(10, 6))

# Criar o gráfico de pizza com uma paleta de cores
wedges, texts, autotexts = ax.pie(frequencia_pagamentos, labels=None, autopct='%1.1f%%',
                                  textprops=dict(color="w"), colors=cores, startangle=90, wedgeprops=dict(width=0.3))

# Adicionar as legendas ao lado com as cores correspondentes
for i, (wedge, texto, autotext, cor) in enumerate(zip(wedges, texts, autotexts, cores)):
    ang = (wedge.theta2 - wedge.theta1) / 2. + wedge.theta1
    y = np.sin(np.deg2rad(ang))
    x = np.cos(np.deg2rad(ang))
    horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
    ax.text(1.35 * np.sign(x), 1.4 * y,
            f"{frequencia_pagamentos.index[i]} - {frequencia_pagamentos.iloc[i]}",
            ha=horizontalalignment, va='center', color=cor)

# Adicionar título
plt.title('Gráfico - Métodos de Pagamento')

# Exibir o gráfico
plt.show()
