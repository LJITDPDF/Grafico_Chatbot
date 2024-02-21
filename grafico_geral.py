import csv
from collections import defaultdict
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

import limpa_dados

limpa_dados.limpa_dados()

# Função para criar o gráfico mensal com base no mês e ano selecionados
def criar_grafico_mensal(mes_desejado=None, ano_desejado=None):
    # Lê o arquivo CSV
    with open("dados.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pule o cabeçalho

        # Dicionário para armazenar o número de acessos por data e ID (dados_recebidos)
        acessos_por_data_id = defaultdict(lambda: defaultdict(int))

        for linha in leitor:
            if len(linha) >= 4:  # Verifique se há pelo menos quatro colunas na linha
                data_str = linha[1].split()[0]  # Obtém a data da segunda coluna
                id_acessado = linha[3]  # Obtém o ID (dados_recebidos) na quarta colunaN

                # Converta a string da data para um objeto datetime
                data = datetime.strptime(data_str, '%Y-%m-%d')

                # Se um mês e ano específicos forem fornecidos, verifique se correspondem
                if (mes_desejado is None or data.month == int(mes_desejado)) and \
                   (ano_desejado is None or data.year == int(ano_desejado)):
                    acessos_por_data_id[data_str][id_acessado] += 1

    # Verifique se há dados para o mês/ano especificados
    if not acessos_por_data_id:
        if mes_desejado is not None and ano_desejado is not None:
            messagebox.showinfo("Informação", f"Nao ha dados para o mes {mes_desejado} do ano {ano_desejado}.")
        elif mes_desejado is not None:
            messagebox.showinfo("Informação", f"Nao ha dados para o mes {mes_desejado}.")
        elif ano_desejado is not None:
            messagebox.showinfo("Informação", f"Nao ha dados para o ano {ano_desejado}.")
        else:
            messagebox.showinfo("Informação", "Nao ha dados para o mes/ano especificado.")
    else:
        # Crie um DataFrame do Pandas com os dados
        data = []
        for date, data_dict in acessos_por_data_id.items():
            total_acessos = sum(data_dict.values())  # Calcula o número total de acessos diários
            for id, count in data_dict.items():
                data.append([date, id, count, total_acessos])

        df = pd.DataFrame(data, columns=['Data', 'ID', 'Acessos', 'Total_Acessos'])

        # Formate a coluna de data no formato "dd/mm/yyyy"
        df['Data'] = pd.to_datetime(df['Data'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')

        # Crie uma categoria ordenada para a coluna de datas
        df['Data'] = pd.Categorical(df['Data'], categories=df['Data'].unique(), ordered=True)

        # Restante do código para criar o gráfico...
        # (o código que você já tinha)

        # Crie um gráfico interativo com o Plotly
        fig = px.bar(df, x='Data', y='Acessos', color='ID', title='Acessos por Data e ID', 
                     labels={'Acessos': 'Acessos Diários'})

        # Adicione uma legenda
        fig.update_xaxes(categoryorder='array', categoryarray=df['Data'].unique(), title_text='Data', type='category')

        # Adicione rótulos de texto no topo de cada barra com a soma dos acessos diários
        for date in df['Data'].unique():
            total_acessos = df[df['Data'] == date]['Total_Acessos'].values[0]
            fig.add_annotation(text=str(total_acessos), x=date, y=total_acessos, showarrow=False)

        data_atual = datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"grafico_mensal_interativo_{data_atual}.html"
        fig.write_html(nome_arquivo)
        import webbrowser
        webbrowser.open(nome_arquivo)

# Função para criar o gráfico anual com base no ano selecionado
def criar_grafico_anual(ano_desejado=None):
    # Lê o arquivo CSV
    with open("dados.csv", "r") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)  # Pule o cabeçalho

        # Dicionário para armazenar o número de acessos por mês e ID (dados_recebidos)
        acessos_por_mes_id = defaultdict(lambda: defaultdict(int))

        for linha in leitor:
            if len(linha) >= 4:  # Verifique se há pelo menos quatro colunas na linha
                data_str = linha[1].split()[0]  # Obtém a data da segunda coluna
                id_acessado = linha[3]  # Obtém o ID (dados_recebidos) na quarta colunaN

                # Converta a string da data para um objeto datetime
                data = datetime.strptime(data_str, '%Y-%m-%d')

                # Se um ano específico for fornecido, verifique se corresponde
                if ano_desejado is None or data.year == int(ano_desejado):
                    acessos_por_mes_id[data.month][id_acessado] += 1

    # Verifique se há dados para o ano especificado
    if not acessos_por_mes_id:
        if ano_desejado is not None:
            messagebox.showinfo("Informação", f"Nao ha dados para o ano {ano_desejado}.")
        else:
            messagebox.showinfo("Informação", "Nao ha dados para o ano especificado.")
    else:
        # Crie um DataFrame do Pandas com os dados
        data = []
        for month, data_dict in acessos_por_mes_id.items():
            total_acessos = sum(data_dict.values())  # Calcula o número total de acessos mensais
            for id, count in data_dict.items():
                data.append([month, id, count, total_acessos])

        df = pd.DataFrame(data, columns=['Mes', 'ID', 'Acessos', 'Total_Acessos'])

        # Restante do código para criar o gráfico...
        # (o código que você já tinha)

        # Crie um gráfico interativo com o Plotly
        fig = px.bar(df, x='Mes', y='Acessos', color='ID', title='Acessos por Mês e ID', 
                     labels={'Acessos': 'Acessos Mensais'})

        # Atualize os rótulos dos eixos X para representar os meses
        fig.update_layout(
            xaxis = dict(
                tickmode = 'array',
                tickvals = list(range(1, 13)),
                ticktext = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
                            'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
            )
        )

        # Adicione rótulos de texto no topo de cada barra com a soma dos acessos mensais
        for month in df['Mes'].unique():
            total_acessos = df[df['Mes'] == month]['Total_Acessos'].values[0]
            fig.add_annotation(text=str(total_acessos), x=month, y=total_acessos, showarrow=False)

        data_atual = datetime.now().strftime("%Y-%m-%d")
        nome_arquivo = f"grafico_anual_interativo_{data_atual}.html"
        fig.write_html(nome_arquivo)
        import webbrowser
        webbrowser.open(nome_arquivo)

# Função chamada quando o botão mensal é clicado
def gerar_grafico_mensal():
    mes_selecionado = combo_meses.get()
    ano_selecionado = combo_anos.get()
    criar_grafico_mensal(mes_selecionado, ano_selecionado)

# Função chamada quando o botão anual é clicado
def gerar_grafico_anual():
    ano_selecionado = combo_anos.get()
    criar_grafico_anual(ano_selecionado)

# Crie a janela principal
janela = tk.Tk()
janela.title("Selecione o Mês e o Ano")
janela.minsize(400, 200)  # Defina a largura e altura mínimas da janela

# Crie uma lista de meses para o campo de seleção
meses = [str(i).zfill(2) for i in range(1, 13)]  # Adiciona zero à esquerda para garantir dois dígitos

# Crie o campo de seleção para os meses
combo_meses = ttk.Combobox(janela, values=meses, state="readonly")
combo_meses.set(meses[0])  # Defina o valor padrão

# Crie uma lista de anos para o campo de seleção
anos = [str(i) for i in range(2023, 2031)]  # Inicia a lista de anos em 2023

# Crie o campo de seleção para os anos
combo_anos = ttk.Combobox(janela, values=anos, state="readonly")
combo_anos.set(anos[0])  # Defina o valor padrão

# Crie os botões para gerar os gráficos
botao_gerar_mensal = tk.Button(janela, text="Gerar Gráfico Mensal", command=gerar_grafico_mensal)
botao_gerar_anual = tk.Button(janela, text="Gerar Gráfico Anual", command=gerar_grafico_anual)

# Posicione os elementos na janela
combo_meses.pack(pady=5)
combo_anos.pack(pady=5)
botao_gerar_mensal.pack(pady=5)
botao_gerar_anual.pack(pady=5)

# Inicie o loop da interface gráfica
janela.mainloop()
