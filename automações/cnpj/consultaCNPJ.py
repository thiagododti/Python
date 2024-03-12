# Codigo para consulta de CNPJ em api publica limitada a 3 cnpjs por minuto.
# O Codigo busca os cnpjs na API e grava em um arquivo em Excel podendo ter a possibilidade de gravar
# em banco de dados se modificar o codigo para a conectar com um banco de dados.

# Necessário remover a pasta do local caso use o codigo novamente pois ele apaga todos os dados e começa novamente a gravação dos dados

import requests
import csv
import time

field_names = ['#', 'razao_social', 'atualizado_em', 'natureza_juridica', 'cnpj', 'nome_fantasia', 'situacao_cadastral',
               'data_inicio_atividade', 'logradouro', 'numero', 'complemento', 'bairro', 'cidade', 'cep', 'estado',
               'ibge_id', 'ddd1', 'telefone1', 'ddd2', 'telefone2', 'email', 'atividade_principal',
               'inscricao_estadual', 'ativo', 'estado_ie', 'atualizado_em_ie']
inscricao = []
contador = 0
cnpjs = ["cnpj_aqui"]


# Função para consultar o CNPJ


def consultaCnpj(cnpjParaConsulta):
    consulta = requests.get(f"https://publica.cnpj.ws/cnpj/{cnpjParaConsulta}")
    consulta = consulta.json()

    if 'status' in consulta:
        consulta = False

    return consulta


# Verifica se cnpj estar válido


# Função para gravar a inscrição no excel


def gravaExcel(cnpjTratado):
    with open('Names.csv', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(cnpjTratado)
    return print(f"{contador} cnpj verificado ")


# Carrega a lista com os dados


def carregaDados(cnpjConsultado):
    global inscricao
    global contador

    if len(cnpjConsultado['estabelecimento']['inscricoes_estaduais']) > 0:
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
                "complemento": cnpjConsultado['estabelecimento']['complemento'],
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
            "complemento": cnpjConsultado['estabelecimento']['complemento'],
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

    gravaExcel(inscricao)
    time.sleep(20)
