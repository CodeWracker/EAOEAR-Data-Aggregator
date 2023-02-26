import os
import sys
import time
import requests
import pandas as pd
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# configura o selenium para não abrir o navegador
options = webdriver.ChromeOptions()
options.add_argument('headless')


base_link = 'https://www2.fab.mil.br/ciaar/index.php/admissao-e-selecao#exames-anteriores'

# usando seleniu abre todos os links que contenham a palavra EAOEAR


def get_years_links():
    driver = webdriver.Chrome()
    driver.get(base_link)
    # time.sleep(5)
    link_containers = driver.find_elements(
        By.CLASS_NAME, 'active')
    link_container = None
    for container in link_containers:
        if 'Exames Anteriores' in container.text:
            link_container = container
            break

        # faz um loop por todos os links do container e verifica se o texto dele possui a palavra EAOEAR
        # se sim, adiciona o link a uma lista
    links = []
    anos = []
    for link in link_container.find_elements(By.TAG_NAME, 'a'):
        # print(link.text)
        if 'Exame de Admissão ao Estágio de Adaptação de Oficiais Engenheiros da Aeronáutica' in link.text:
            links.append(link.get_attribute('href'))

    for ano in link_container.find_elements(By.TAG_NAME, 'strong'):
        if 'EAOEAR' in ano.text:
            # print(ano.text.split('EAOEAR')[1])
            anos.append(ano.text.split('EAOEAR ')[1])

    return links, anos


# def get_pdf_link(year_link):
# Relação nominal de candidatos com os resultados finais

def get_year_edital(year_link):
    driver = webdriver.Chrome()
    driver.get(year_link)

    container = driver.find_element(By.CLASS_NAME, 'item-page')

    for link in container.find_elements(By.TAG_NAME, 'a'):
        if 'Conheça o edital' in link.text or 'Edital' in link.text or 'CONHEÇA O EDITAL' in link.text or 'Conheça o Edita' in link.text:
            return link.get_attribute('href')


def save_pdf_by_year_and_type(pdf_link, year, type):
    # types: edital, resultaod
    # year: YYYY

    # Salva no estilo: data/pdfs/<year>_<type>.pdf
    # Exemplo: data/pdfs/2020_edital.pdf

    # Cria a pasta data/pdfs caso ela não exista
    if not os.path.exists('data/pdfs'):
        os.makedirs('data/pdfs')

    # Faz o download do pdf
    pdf = requests.get(pdf_link)

    # Salva o pdf
    with open(f'data/pdfs/{year}_{type}.pdf', 'wb') as f:
        f.write(pdf.content)

    # Retorna o caminho do pdf salvo
    return f'data/pdfs/{year}_{type}.pdf'


def get_year_result(year_link=None):
    # cara eu não consegui achar um padrão no site então, ate que eu faça isso de forma mais generica isso aqui vai estar com os links hard coded
    return


if __name__ == '__main__':
    links, anos = get_years_links()
    # for i in range(len(links)):
    #     print(f' {anos[i]} - {links[i]} ')
    # links_editais = []
    # for link in links:
    #     links_editais.append(get_year_edital(link))

    # for i in range(len(links_editais)):
    #     save_pdf_by_year_and_type(links_editais[i], anos[i], 'edital')
    # print(links_editais)

    results_pdf_links = [
        "https://www2.fab.mil.br/ciaar/images/ingresso/EAOEAR2023/12_vf_notas_finais_EAOEAR2023.pdf",
        "https://www2.fab.mil.br/ciaar/images/ingresso/EAOEAR2022/clas_EAOEAR2022.pdf",
        "https://www2.fab.mil.br/ciaar/images/ingresso/EAOEAR2021/mf_complementar_EAOEAR2021.pdf",
        "https://www2.fab.mil.br/ciaar/images/ingresso/EAOEAR2020/resultadosprovasescritaseaoear20_2.pdf",
        "https://www2.fab.mil.br/ciaar/images/ingresso/eaoear2016/16mediafinaleaoear19.pdf",
        "https://www2.fab.mil.br/ciaar/images/concursos/eaoear2018/18mediasfinaiseaoear18.pdf",
        "https://www2.fab.mil.br/ciaar/images/concursos/eaoear2017/09mediasfinaiseaoear17.pdf",
    ]

    for i in range(len(results_pdf_links)):
        save_pdf_by_year_and_type(results_pdf_links[i], anos[i], 'resultado')
