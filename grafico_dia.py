import pandas as pd
import matplotlib.pyplot as plt
import locale
import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# axes= eixos

# Definir a localidade para formatar os valores em euros
locale.setlocale(locale.LC_ALL, 'pt_PT.utf-8')

# seus dados estejam em um arquivo CSV chamado "dados.csv"
# lê dados de um arquivo CSV chamado "pedidos_clean.csv" e armazená-los em um DataFrame chamado dados
dados = pd.read_csv("pedidos_clean.csv", parse_dates=['Data'])

# Criar uma coluna 'DiaDaSemana' para armazenar o dia da semana da venda
dados['DiaDaSemana'] = dados['Data'].dt.day_name()

    #.dt: Este é o acessador que permite acessar componentes específicos da data e hora.
    #day_name(): Este método é aplicado ao acessador .dt e retorna o nome do dia da semana 
    #para cada valor na coluna 'Data'. Cria uma nova coluna chamada 'DiaDaSemana' no DataFrame dados e a preenche 

# Criar uma coluna 'AnoMes' para armazenar o ano e mês da venda
dados['AnoMes'] = dados['Data'].dt.to_period('M')


# Função para plotar o gráfico com base no ano e mês selecionados
def plotar_grafico():
    ano_selecionado = int(ano_combobox.get())
    mes_selecionado = mes_combobox.get()

    dados_selecionados = dados[
        (dados['Data'].dt.year == ano_selecionado) & (dados['Data'].dt.strftime('%b') == mes_selecionado)]

    vendas_por_dia_da_semana = dados_selecionados.groupby('DiaDaSemana')['ValorTotal'].sum()

    # Ordenar os dias da semana na ordem desejada
    dias_da_semana_ordem = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    vendas_por_dia_da_semana = vendas_por_dia_da_semana.reindex(dias_da_semana_ordem)

    # Cores diferentes para cada barra
    cores = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'gray']

    # Limpar a figura anterior antes de plotar uma nova
    plt.clf()

    # Plotar o gráfico de barras com formatação em euros e cores personalizadas
    plt.bar(vendas_por_dia_da_semana.index, vendas_por_dia_da_semana, color=cores)
    plt.xlabel('Dia da Semana')
    plt.ylabel('Valor Total de Vendas (€)')
    plt.title(f'Valor Total de Vendas por Dia da Semana em {mes_selecionado} de {ano_selecionado}')

    # Adicionar o símbolo do euro aos valores no eixo y
    plt.gca().yaxis.set_major_formatter(locale.currency)

    # Atualizar a tela
    canvas.draw()


# Criar a janela principal
janela = tk.Tk()
janela.title("Análise de Vendas por Dia da Semana")

# Adicionar uma combobox para selecionar o ano
anos_disponiveis = sorted(dados['Data'].dt.year.unique())
ano_combobox = ttk.Combobox(janela, values=anos_disponiveis)
ano_combobox.set(anos_disponiveis[-1])   #ano_combobox seja um objeto representando um ComboBox e anos_disponiveis seja uma lista de anos disponíveis. #anos_disponiveis[-1]: Isso acessa o último elemento da lista anos_disponiveis. 
ano_combobox.pack(pady=10)

# Adicionar uma combobox para selecionar o mês
meses_disponiveis = sorted(dados['Data'].dt.strftime('%b').unique())
mes_combobox = ttk.Combobox(janela, values=meses_disponiveis)
mes_combobox.set(meses_disponiveis[-1])
mes_combobox.pack(pady=10)

# Adicionar um botão para plotar o gráfico
botao_plotar = ttk.Button(janela, text="Plotar Gráfico", command=plotar_grafico)
botao_plotar.pack(pady=10)

# Adicionar uma área de desenho para o gráfico
figura, ax = plt.subplots()
canvas = FigureCanvasTkAgg(figura, master=janela)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack()

# Iniciar o loop da interface gráfica
janela.mainloop()
