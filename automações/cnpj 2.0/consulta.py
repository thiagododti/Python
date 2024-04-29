import requests
import csv
import time
import pandas as pd
import os


field_names = ['#', 'razao_social', 'atualizado_em', 'natureza_juridica',
               'cnpj', 'nome_fantasia', 'situacao_cadastral',
               'data_inicio_atividade', 'logradouro', 'numero',
               'bairro', 'cidade', 'cep', 'estado',
               'ibge_id', 'ddd1', 'telefone1', 'ddd2', 'telefone2',
               'email', 'atividade_principal', 'inscricao_estadual',
               'ativo', 'estado_ie', 'atualizado_em_ie']
inscricao = []
contador = 0

# Ler o Excel


def lerExcel():

    # Ler a lista do arquivo Excel
    df = pd.read_excel('cnpj.xlsx', sheet_name='cnpj')

    # Armazenar a coluna desejada em uma variavel lista
    cnpjs = df['cnpj'].tolist()

    # faz a leitura item por item para completar cnpj
    # excel exclui 0 a esquerda então aqui ele completa
    # a quantidade de 0 necessárias para que o cnpj tenha
    # os 14 numeros
    for i in range(len(cnpjs)):
        cnpjs[i] = str(cnpjs[i])

        cnpjs[i] = cnpjs[i].zfill(14)

    return cnpjs


cnpjs = lerExcel()

# Função para consultar o CNPJ


def consultaCnpj(cnpjParaConsulta):
    consulta = requests.get(f"https://publica.cnpj.ws/cnpj/{cnpjParaConsulta}")
    consulta = consulta.json()

    if 'status' in consulta:
        consulta = False

    return consulta

# Função para gravar a inscrição no excel


def gravaExcel(cnpjTratado):
    with open('cnpjconsultado/cnpjs-consultados.csv', 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerows(cnpjTratado)
    return print(f"{contador} / {len(cnpjs)} cnpj verificado ")


# Carrega a lista com os dados


def carregaDados(cnpjConsultado):
    global inscricao
    global contador

    if len(cnpjConsultado['estabelecimento']['inscricoes_estaduais']) > 0:
        inscricao = []
        for x in range(len(cnpjConsultado['estabelecimento']['inscricoes_estaduais'])):
            inscricao.append({
                "#": contador,
                "cnpj": cnpjConsultado['estabelecimento']['cnpj'],
                "razao_social": cnpjConsultado['razao_social'],
                "atualizado_em": cnpjConsultado['atualizado_em'],
                "natureza_juridica": cnpjConsultado['natureza_juridica']['descricao'],
                "nome_fantasia": cnpjConsultado['estabelecimento']['nome_fantasia'],
                "situacao_cadastral": cnpjConsultado['estabelecimento']['situacao_cadastral'],
                "data_inicio_atividade": cnpjConsultado['estabelecimento']['data_inicio_atividade'],
                "logradouro": cnpjConsultado['estabelecimento']['logradouro'],
                "numero": cnpjConsultado['estabelecimento']['numero'],
                "bairro": cnpjConsultado['estabelecimento']['bairro'],
                "cep": cnpjConsultado['estabelecimento']['cep'],
                "estado": cnpjConsultado['estabelecimento']['estado']['sigla'],
                "cidade": cnpjConsultado['estabelecimento']['cidade']['nome'],
                "ibge_id": cnpjConsultado['estabelecimento']['cidade']['ibge_id'],
                "ddd1": cnpjConsultado['estabelecimento']['ddd1'],
                "telefone1": cnpjConsultado['estabelecimento']['telefone1'],
                "ddd2": cnpjConsultado['estabelecimento']['ddd2'],
                "telefone2": cnpjConsultado['estabelecimento']['telefone2'],
                "email": cnpjConsultado['estabelecimento']['email'],
                "atividade_principal": cnpjConsultado['estabelecimento']['atividade_principal']['descricao'],
                "inscricao_estadual": cnpjConsultado['estabelecimento']['inscricoes_estaduais'][x]['inscricao_estadual'],
                "ativo": cnpjConsultado['estabelecimento']['inscricoes_estaduais'][x]['ativo'],
                "estado_ie": cnpjConsultado['estabelecimento']['inscricoes_estaduais'][x]['estado']['sigla'],
                "atualizado_em_ie": cnpjConsultado['estabelecimento']['inscricoes_estaduais'][x]['atualizado_em']
            })
            contador = contador + 1
    else:
        inscricao = []
        inscricao.append({
            "#": contador,
            "cnpj": cnpjConsultado['estabelecimento']['cnpj'],
            "razao_social": cnpjConsultado['razao_social'],
            "atualizado_em": cnpjConsultado['atualizado_em'],
            "natureza_juridica": cnpjConsultado['natureza_juridica']['descricao'],
            "nome_fantasia": cnpjConsultado['estabelecimento']['nome_fantasia'],
            "situacao_cadastral": cnpjConsultado['estabelecimento']['situacao_cadastral'],
            "data_inicio_atividade": cnpjConsultado['estabelecimento']['data_inicio_atividade'],
            "logradouro": cnpjConsultado['estabelecimento']['logradouro'],
            "numero": cnpjConsultado['estabelecimento']['numero'],
            "bairro": cnpjConsultado['estabelecimento']['bairro'],
            "cep": cnpjConsultado['estabelecimento']['cep'],
            "estado": cnpjConsultado['estabelecimento']['estado']['sigla'],
            "cidade": cnpjConsultado['estabelecimento']['cidade']['nome'],
            "ibge_id": cnpjConsultado['estabelecimento']['cidade']['ibge_id'],
            "ddd1": cnpjConsultado['estabelecimento']['ddd1'],
            "telefone1": cnpjConsultado['estabelecimento']['telefone1'],
            "ddd2": cnpjConsultado['estabelecimento']['ddd2'],
            "telefone2": cnpjConsultado['estabelecimento']['telefone2'],
            "email": cnpjConsultado['estabelecimento']['email'],
            "atividade_principal": cnpjConsultado['estabelecimento']['atividade_principal']['descricao'],
            "inscricao_estadual": "vazio",
            "ativo": "vazio",
            "estado_ie": "vazio",
            "atualizado_em_ie": "vazio"
        })
        contador = contador + 1


# Execução


for cnpj in cnpjs:
    consulta = consultaCnpj(cnpj)
    if consulta:
        carregaDados(consulta)
    if not os.path.exists('cnpjconsultado/cnpjs-consultados.csv'):
        with open('cnpjconsultado/cnpjs-consultados.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
    gravaExcel(inscricao)
    time.sleep(20)
