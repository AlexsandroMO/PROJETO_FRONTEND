import requests
from bs4 import BeautifulSoup
from unicodedata import normalize
import pandas as pd
import openpyxl
import xlrd

def remover_acentos(txt):
  return normalize('NFKD', txt).encode('ASCII', 'ignore').decode('ASCII')

def search_vaga(url_href):
    searched_link = url_href
    headers_x = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    response_object_x = requests.get(searched_link, headers=headers_x)

    search_soup_x = BeautifulSoup(response_object_x.text, features='html.parser')
    product_elems_x = search_soup_x.select('p')

    return product_elems_x

def read_search(imput_vaga):
    x = imput_vaga.split()
    search = 'vagas-de-' + '-'.join(x)
    search = remover_acentos(search)

    search_url = 'https://www.vagas.com.br/' + search.lower()

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    response_object = requests.get(search_url, headers=headers)

    search_soup = BeautifulSoup(response_object.text, features='html.parser')

    product_elemt = search_soup.select('a.link-detalhes-vaga')

    product_list = []

    for product in product_elemt:
        product_soup = BeautifulSoup(str(product), features='html.parser')
        description_elem = product_soup.select_one('a.link-detalhes-vaga')
        #description = description_elem.text #Ler tudo que ta fora de tags
        description_text = description_elem.get('title')
        description_ID = description_elem.get('data-id-vaga')
        url_href = 'https://www.vagas.com.br/' + description_elem.get('href')
        #print('Title_Vaga: {} | ID_Vaga: {} | Link: {}'.format(description_text, description_ID, url_href))

        product_elems_x = search_vaga(url_href)

        description_list = []

        for product in product_elems_x:
            product_soup_x = BeautifulSoup(str(product), features='html.parser')
            description_elem_x = product_soup_x.select_one('p')
            description_x = description_elem_x.text
            description_list.append(description_x)

    product_list.append([description_text, description_ID, url_href, description_list])

    #df = pd.DataFrame(data=product_list, columns=['TITLE','ID','LINK','DESCRIPTION'])


    return product_list
