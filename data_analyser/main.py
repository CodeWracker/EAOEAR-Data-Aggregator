import pandas as pd
import numpy as np

# importa matplotlib
import matplotlib.pyplot as plt

import os
from pprint import pprint


def get_list_of_non_zero_values(df, column):
    # faz um loop em cada linha do df
    # se o valor da linha for diferente de zero adiciona em uma lista
    # retorna a lista
    non_zero_values = []
    for index, row in df.iterrows():
        if row[column] != 0:
            non_zero_values.append(row[column])
    return np.array(non_zero_values)


vagas_df = pd.read_csv('data/extractions/editais_vagas.csv')

results_dfs = []
# para cada arquivo de resultado na pasta extractions, coloca em um dataframe na lista results_dfs
for i, file in enumerate(os.listdir('data/extractions')):
    if file.endswith('resultado.csv'):
        results_dfs.append([file.split("_")[0], pd.read_csv(
            "data/extractions/" + file, index_col=False)])

chart_data = {
    'Ano': [],
    'ESP': [],
    'Vagas': [],
    'Inscritos': [],
    'Aprovados': [],
    'Media': [],
    'Max': [],
    'Min': [],
    'Desvio Padrao': []
}
for year_df in results_dfs:
    year, df = year_df
    print(year)
    # printa o edita desse ano

    # for ed_col in vagas_df.columns:
    #     if ed_col != 'Ano':
    #         print(
    #             f"   {ed_col}: {vagas_df.loc[vagas_df['Ano'] == int(year), ed_col].values[0]}")

    # cria um df novo para cada ESP diferente que tiver no df
    esp_dfs = []
    for esp in df['ESP'].unique():
        # cria um novo df e adiciona na lista
        esp_dfs.append([esp, df.loc[df['ESP'] == esp]])

    # para cada df de esp
    for esp_df in esp_dfs:
        foi = False
        for col in esp_df:
            # printa o nome da esp
            if (not foi):
                inscritos = len(esp_df[1])
                # pega os primeiros (vaga * 5) valores do df
                vagas = vagas_df.loc[vagas_df['Ano'] ==
                                     int(year), esp_df[0]].values[0] * 5
                # para cada cada esp, pega os primeiros (vaga * 5) valores do df
                esp_df[1] = esp_df[1].head(vagas)

                print(
                    f"   {esp_df[0]} -> Vagas: {vagas_df.loc[vagas_df['Ano'] == int(year), esp_df[0]].values[0]}, Inscritos:{inscritos}, Maximo de Aprovados: {len(esp_df[1])} -> Média: {esp_df[1]['MF'].mean():.4f} | Max: {esp_df[1]['MF'].max():.4f} | Min: {esp_df[1]['MF'].min():.4f} | Desvio Padrão: {esp_df[1]['MF'].std():.4f}")
                chart_data['Ano'].append(year)
                chart_data['ESP'].append(esp_df[0])
                chart_data['Vagas'].append(vagas_df.loc[vagas_df['Ano'] ==
                                                        int(year), esp_df[0]].values[0])
                chart_data['Inscritos'].append(inscritos)
                chart_data['Aprovados'].append(len(esp_df[1]))
                chart_data['Media'].append(esp_df[1]['MF'].mean())
                chart_data['Max'].append(esp_df[1]['MF'].max())
                chart_data['Min'].append(esp_df[1]['MF'].min())
                chart_data['Desvio Padrao'].append(esp_df[1]['MF'].std())
                foi = True

# cria um df com os dados
chart_data_df = pd.DataFrame(chart_data)
print(chart_data_df)

# filtrando por ESP, cria um grafico de linhas com a media, max e min de cada ano e salva no formato ESP.png
for esp in chart_data_df['ESP'].unique():
    esp_df = chart_data_df.loc[chart_data_df['ESP'] == esp]
    # transforma a coluna de Ano para inteiro
    esp_df['Ano'] = esp_df['Ano'].astype(int)
    esp_df.plot(x='Ano', y=['Media', 'Max', 'Min'])

    #  faz o passo do eixo x ser 1
    plt.xticks(np.arange(esp_df['Ano'].min(), esp_df['Ano'].max()+1, 1.0))

    plt.savefig(f"data/charts/stats_{esp}.png")

    #  salva o df em extractions como ESP_stats.csv
    esp_df.to_csv(f"data/extractions/stats_{esp}.csv", index=False)

    plt.clf()
