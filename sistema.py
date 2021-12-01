from interface import *
from time import sleep
import requests
from bs4 import BeautifulSoup
import json
from requests.auth import HTTPBasicAuth
import pandas as pd
import collections

while True:
    resposta = menu(['AZTRAGENICA','PFIZER','CORONAVAC','JANSSEN', 'Sair do Sistema'])
    if resposta == 1:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = json.dumps({
            "size": 10000
        })
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json',
            'Cookie': 'ELASTIC-PROD=1636059148.429.5691.789359'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        vacina = response.json()
        df = pd.json_normalize(vacina['hits']['hits'])
        teste = df['_source.vacina_nome']
        # print(teste)
        def myFunc(x):
            if x == 'COVID-19 ASTRAZENECA/FIOCRUZ - COVISHIELD':
                return True
            else:
                return False
        teste2 = filter(myFunc, teste)
        astrazeneca = []
        for x in teste2:
            astrazeneca.append(x)
        print(collections.Counter(astrazeneca))


    elif resposta == 2:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = json.dumps({
            "size": 10000
        })
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json',
            'Cookie': 'ELASTIC-PROD=1636059148.429.5691.789359'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        vacina = response.json()
        df = pd.json_normalize(vacina['hits']['hits'])
        teste = df['_source.vacina_nome']


        # print(teste)
        def myFunc2(x):
            if x == 'COVID-19 PFIZER - COMIRNATY':
                return True
            else:
                return False
        teste2 = filter(myFunc2, teste)
        pfizer = []
        for x in teste2:
            pfizer.append(x)

        print(collections.Counter(pfizer))




    elif resposta == 3:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = json.dumps({
            "size": 10000
        })
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json',
            'Cookie': 'ELASTIC-PROD=1636059148.429.5691.789359'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        vacina = response.json()
        df = pd.json_normalize(vacina['hits']['hits'])
        teste = df['_source.vacina_nome']


        # print(teste)
        def myFunc2(x):
            if x == 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC':
                return True
            else:
                return False
        teste2 = filter(myFunc2, teste)
        coronavac = []
        for x in teste2:
            coronavac.append(x)
        print(collections.Counter(coronavac))

    elif resposta == 4:
        url = "https://imunizacao-es.saude.gov.br/_search"
        payload = json.dumps({
            "size": 10000
        })
        headers = {
            'Authorization': 'Basic aW11bml6YWNhb19wdWJsaWM6cWx0bzV0JjdyX0ArI1Rsc3RpZ2k=',
            'Content-Type': 'application/json',
            'Cookie': 'ELASTIC-PROD=1636059148.429.5691.789359'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        vacina = response.json()
        df = pd.json_normalize(vacina['hits']['hits'])
        teste = df['_source.vacina_nome']


        # print(teste)
        def myFunc2(x):
            if x == 'COVID-19 SINOVAC/BUTANTAN - CORONAVAC':
                return True
            else:
                return False


        teste2 = filter(myFunc2, teste)
        janssen = []
        for x in teste2:
            janssen.append(x)
        print(collections.Counter(janssen))

    elif resposta == 5:
        print('\033[31mSaindo do Sistema ...\033[m')
        break
    else:
        print('\033[31mERRO! Digite uma Opção Válida !\033[m')
    sleep(2)
