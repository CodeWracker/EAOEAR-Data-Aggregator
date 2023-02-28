from sklearn.linear_model import LinearRegression
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# regressor = LinearRegression()
# regressor.fit(X,y)

# y_pred = regressor.predict(X_next)

# para cada csv de stats na pasta de extractions faz uma regressão linear para as colunas Media, Min e Max

for i, file in enumerate(os.listdir('data/extractions')):
    # verifica se o arquivo começa com stats
    if file.startswith('stats'):
        df = pd.read_csv('data/extractions/' + file)
        # pega a esperecialidade
        esp = file.split('_')[1].split(".")[0]

        # faz a regressão linear para cada coluna
        media = None
        minimo = None
        maximo = None

        for col in ['Media', 'Min', 'Max']:
            # pega os valores de X e y
            X = df['Ano'].values
            y = df[col].values

            # cria um novo regressor
            regressor = LinearRegression()
            # treina o regressor
            regressor.fit(X.reshape(-1, 1), y)

            # pega o valor de X para o próximo ano
            X_next = np.array([2024])
            # faz a predição
            y_pred = regressor.predict(X_next.reshape(-1, 1))
            # printa o resultado
            print(f'{esp} {col} {y_pred[0]}')
            if col == 'Media':
                media = y_pred[0]
            elif col == 'Min':
                minimo = y_pred[0]
            elif col == 'Max':
                maximo = y_pred[0]

                # inclui a predição no dataframe
        new_row = {'Ano': 2024, "Media": media, "Min": minimo, "Max": maximo}
        df = df.append(new_row, ignore_index=True)
        # salva o dataframe
        df.to_csv('data/extractions/regression_stats_' +
                  esp + ".csv", index=False)

        df['Ano'] = df['Ano'].astype(int)
        df.plot(x='Ano', y=['Media', 'Max', 'Min'])

        #  faz o passo do eixo x ser 1
        plt.xticks(np.arange(df['Ano'].min(), df['Ano'].max()+1, 1.0))

        plt.savefig(f"data/charts/regression_{esp}.png")

        plt.clf()
