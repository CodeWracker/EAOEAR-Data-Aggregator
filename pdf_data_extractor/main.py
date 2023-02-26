# ira ler uma pasta com varios pdfs e extrair os dados das tabelas de cada um deles
# apenas o pdf de resultado
# sera considerado 2020 para cima apenas, pois antes disso não tinha diferenciação das especialidades

# o pdf possui as colunas
# INSC = numero de inscrição
# NOME = nome do candidato
# ESP = especialidade
# GIT = Grau da prova de gramatica e interpretação de texto
# CE = Grau da prova de conhecimentos específicos
# RED = Grau da prova de redação
# MF = Média final

import tabula
import pandas as pd
import numpy as np
import os


def convert_pdf_to_csv(pdf_path, year):
    print(f'convertendo pdf para csv - {pdf_path}')
    # get the number of pages
    pdfs = tabula.read_pdf(pdf_path, pages='all')

    # para cada pdf em pdfs, cria um df e depois junta tudo

    df = pd.DataFrame()

    for pdf in pdfs:
        df = df.append(pdf)

    # print(df["ESP"])
    # print(df["GIT"])
    # print(df["CE"])
    # print(df["RED"])
    # print(df["MF"])

    # lista as colunas
    cols = list(df.columns.values)

    # remove as colunas que não forem:  ESP, GIT, CE, RED, MF
    for col in cols:
        if col not in ['ESP', 'GIT', 'CE', 'RED', 'MF']:
            df = df.drop(col, axis=1)

    # remove linhas vazias
    df = df.dropna()

    # substtui "," por "." em todos os valores
    df = df.replace(',', '.', regex=True)

    # converte as colunas para float
    df['GIT'] = df['GIT'].astype(float)
    df['CE'] = df['CE'].astype(float)
    df['RED'] = df['RED'].astype(float)
    df['MF'] = df['MF'].astype(float)

    # ordena por ESP e MF
    df = df.sort_values(by=['ESP', 'MF'], ascending=False)

    # salva o df em um csv
    df.to_csv(
        f'data/extractions/{year}_resultado.csv', index=False)
    print(f'csv criado com sucesso! - {pdf_path}')


if __name__ == '__main__':
    # para cada arquivo de resultado de pdfs na pasta data/pdfs chamar a função convert_pdf_to_csv
    for file in os.listdir('data/pdfs'):
        if 'resultado' in file:
            # verifica se o ano é maior que 2019
            if int(file.split('_')[0]) > 2019:
                convert_pdf_to_csv(f'data/pdfs/{file}', file.split('_')[0])

    cursos = {
        "CGR": "Engenharia Cartográfica",
        "CIV": "Engenharia Civil",
        "CMP": "Engenharia de Computação",
        "ELN": "Engenharia Eletrônica",
        "ELT": "Engenharia Elétrica",
        "MEC": "Engenharia Mecânica",
        "QUI": "Engenharia Química",
        "TEL": "Engenharia de Telecomunicações",
        "MTL": "Engenharia Metalúrgica",
    }

    vagas_por_edital = [
        [
            # 2023
            {
                "Curso": "CGR",
                "Vagas": 1,
            },
            {
                "Curso": "CIV",
                "Vagas": 8,
            },
            {
                "Curso": "CMP",
                "Vagas": 6,
            },
            {
                "Curso": "ELN",
                "Vagas": 4,
            },
            {
                "Curso": "ELT",
                "Vagas": 5,
            },
            {
                "Curso": "MEC",
                "Vagas": 4,
            },
            {
                "Curso": "QUI",
                "Vagas": 1,
            },
            {
                "Curso": "TEL",
                "Vagas": 1,
            },
        ],
        [
            # 2022
            {
                "Curso": "CIV",
                "Vagas": 3,
            },
            {
                "Curso": "CMP",
                "Vagas": 4,
            },
            {
                "Curso": "ELN",
                "Vagas": 3,
            },
            {
                "Curso": "ELT",
                "Vagas": 3,
            },
            {
                "Curso": "MTL",
                "Vagas": 1,
            },
            {
                "Curso": "MEC",
                "Vagas": 3,
            },
            {
                "Curso": "QUI",
                "Vagas": 2,
            },
            {
                "Curso": "TEL",
                "Vagas": 1,
            }
        ],
        [
            # 2021
            {
                "Curso": "CIV",
                "Vagas": 4,
            },
            {
                "Curso": "CMP",
                "Vagas": 4,
            },
            {
                "Curso": "ELN",
                "Vagas": 2,
            },
            {
                "Curso": "ELT",
                "Vagas": 3,
            },
            {
                "Curso": "MEC",
                "Vagas": 4,
            },
            {
                "Curso": "QUI",
                "Vagas": 1,
            },
            {
                "Curso": "TEL",
                "Vagas": 2,
            }
        ],
        [
            # 2020
            {
                "Curso": "CIV",
                "Vagas": 3,
            },
            {
                "Curso": "CMP",
                "Vagas": 3,
            },
            {
                "Curso": "ELN",
                "Vagas": 3,
            },
            {
                "Curso": "ELT",
                "Vagas": 3,
            },
            {
                "Curso": "MTL",
                "Vagas": 1,
            },
            {
                "Curso": "MEC",
                "Vagas": 3,
            },
            {
                "Curso": "QUI",
                "Vagas": 1,
            },
            {
                "Curso": "TEL",
                "Vagas": 3,
            }
        ],

    ]

    # coloca isso em um csv e salvar em data/editais_vagas.csv
    df_editais = pd.DataFrame()
    # cada curso é uma coluna
    for curso in cursos:
        df_editais[curso] = np.array([])
    df_editais["Ano"] = np.array([])

    for i, vagas in enumerate(vagas_por_edital):
        cursos_list = {
            "CGR": {
                'found': False,
                'vagas': []
            },
            "CIV": {
                'found': False,
                'vagas': []
            },
            "CMP": {
                'found': False,
                'vagas': []
            },
            "ELN": {
                'found': False,
                'vagas': []
            },
            "ELT": {
                'found': False,
                'vagas': []
            },
            "MEC": {
                'found': False,
                'vagas': []
            },
            "QUI": {
                'found': False,
                'vagas': []
            },
            "TEL": {
                'found': False,
                'vagas': []
            },
            "MTL": {
                'found': False,
                'vagas': []
            },
        }
        anos_list = [2023, 2022, 2021, 2020]
        new_df = pd.DataFrame()
        # print(vagas)
        for vaga in vagas:
            # print(vaga)
            cursos_list[vaga["Curso"]]['found'] = True
            cursos_list[vaga["Curso"]]['vagas'].append(vaga["Vagas"])

        for curso in cursos_list:
            if (not cursos_list[curso]['found']):
                cursos_list[curso]['vagas'].append(0)

        for curso in cursos_list:
            new_df[curso] = cursos_list[curso]['vagas']
        new_df["Ano"] = anos_list[i]

        df_editais = df_editais.append(new_df)

        # converte resultados para int
        df_editais = df_editais.astype(int)

    df_editais.to_csv('data/extractions/editais_vagas.csv', index=False)
