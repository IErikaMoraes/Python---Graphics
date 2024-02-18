import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Carrega o arquivo (variavel que lê o arquivo csv, atraves da biblioteca pandas)
df = pd.read_csv('pedidos_clean.csv')

# Agrupa por mês e calcula o total de vendas (agrupa por mês e soma a coluna Valor Total e para nao ter erros é retirada a coluna do index)
vendas_por_mes = df.groupby('Mes')['ValorTotal'].sum().reset_index()

# Mapeia e atribui o número do mês para o nome do mês (opcional)
vendas_por_mes['Mes'] = vendas_por_mes['Mes'].map({
    1: 'Janeiro', 2: 'Fevereiro', 3: 'Março',
    4: 'Abril', 5: 'Maio', 6: 'Junho',
    7: 'Julho', 8: 'Agosto', 9: 'Setembro',
    10: 'Outubro', 11: 'Novembro', 12: 'Dezembro'
})

# Ordena os dados por mês
vendas_por_mes = vendas_por_mes.sort_values(by='ValorTotal', ascending=False)

# Formatação do valor com o símbolo de euro e duas casas decimais (def é como uma Função)
def formatar_valor_euro(valor, _):
    return f'€ {valor:.2f}'

# Criar uma paleta de cores Set3
cores = plt.cm.Set3(range(len(vendas_por_mes)))  #plt.cm: módulo de mapas de cores (colormaps), biblioteca matplotlib.
                                                 #Set3: Este é um dos mapas de cores disponíveis de cores.
                                                 #range(len(vendas_por_mes)): Gera uma sequência de números que varia de 0 a len(vendas_por_mes) - 1. Isso é usado para associar uma cor única a cada valor em vendas_por_mes.
#cores= está criando uma lista chamada cores que contém cores correspondentes aos valores em vendas_por_mes. 
#Cada valor em vendas_por_mes será associado a uma cor única do mapa de cores Set3. 

# Gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(vendas_por_mes['Mes'], vendas_por_mes['ValorTotal'], color=cores)

plt.xlabel('Mês')
plt.ylabel('Total de Vendas (€)')
plt.title('Total de Vendas por Mês entre 2022-2024')

# Aplica a formatação ao eixo y
plt.gca().yaxis.set_major_formatter(FuncFormatter(formatar_valor_euro))

#plt.gca(): gca é uma abreviação de "get current axis" (obter eixo atual) e é uma função do módulo pyplot da biblioteca matplotlib. 
#Ela retorna o objeto Axes que representa o eixo atual no gráfico. Cria eixos

#.yaxis: Isso acessa o objeto que representa o eixo vertical (eixo y) do gráfico.

#.set_major_formatter(FuncFormatter(formatar_valor_euro)): configurando um formatador para os rótulos do eixo y. 
#FuncFormatter é uma classe em matplotlib.ticker que permite formatar os valores dos rótulos usando uma função definida pelo usuário.

#axis=1 qd deseja que o pc leia a linha, axis=0 lê por coluna(padrão)

plt.show()
