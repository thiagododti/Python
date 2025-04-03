# Instale as dependências necessárias com o comando abaixo
# pip install requests pandas openpyxl

# Após instalar as dependências, execute o código abaixo para ele criar o arquivo Excel para inserir os cnpjs na coluna cnpj

# Após listar os cnpjs que vão ser consultados no arquivo cnpj.xlsx basta executar o código novamente para ele fazer
# a consulta no site https://publica.cnpj.ws/ e gerar o arquivo cnpjs-consultados.csv com os dados consultados.

import requests
import csv
import time
import pandas as pd
import os
import sys

field_names = ['#', 'razao_social', 'atualizado_em', 'natureza_juridica',
               'cnpj', 'nome_fantasia', 'situacao_cadastral',
               'data_inicio_atividade', 'logradouro', 'numero',
               'bairro', 'cidade', 'cep', 'estado',
               'ibge_id', 'ddd1', 'telefone1', 'ddd2', 'telefone2',
               'email', 'cnae', 'atividade_principal', 'inscricao_estadual',
               'ativo', 'estado_ie', 'atualizado_em_ie']
inscricao = []
contador = 0

# Ler o Excel


def progress_bar(total, progress):
    bar_length = 40  # comprimento da barra de progresso
    block = int(round(bar_length * progress / total))
    text = f"\rProgress: [{'#' * block + '-' *
                           (bar_length - block)}] {progress}/{total}"
    sys.stdout.write(text)
    sys.stdout.flush()


# Exemplo de
def count(total):

    for i in range(total + 1):
        progress_bar(total, i)
        time.sleep(1)  # Simula o tempo de processamento


def lerExcel():
    # Verificar se o arquivo existe
    if not os.path.exists('cnpj.xlsx'):
        # Criar o arquivo e adicionar a coluna 'cnpj' caso não exista
        df = pd.DataFrame(columns=['cnpj'])
        df.to_excel('cnpj.xlsx', index=False)
        print("Arquivo 'cnpj.xlsx' criado com a coluna 'cnpj'.")

    # Ler a lista do arquivo Excel
    df = pd.read_excel('cnpj.xlsx')

    # Armazenar a coluna desejada em uma variável lista
    cnpjs = df['cnpj'].tolist()

    # Faz a leitura item por item para completar o CNPJ
    # Excel exclui 0 à esquerda, então aqui ele completa
    # a quantidade de 0 necessárias para que o CNPJ tenha
    # os 14 números
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
    # Usar o modo 'a' com newline='' para evitar linhas extras
    with open('cnpjconsultado/cnpjs-consultados.csv', 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)

        # Adiciona o cabeçalho apenas se o arquivo estiver vazio
        if csvfile.tell() == 0:
            writer.writeheader()

        writer.writerows(cnpjTratado)

    print(f"{contador} / {len(cnpjs)} cnpj verificado ")


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
                "cnae": cnpjConsultado['estabelecimento']['atividade_principal']['id'],
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
            "cnae": cnpjConsultado['estabelecimento']['atividade_principal']['id'],
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

    # Verifica se o diretório 'cnpjconsultado' existe, se não, cria
    if not os.path.exists('cnpjconsultado'):
        os.makedirs('cnpjconsultado')

    # Verifica se o arquivo 'cnpjs-consultados.csv' existe, se não, cria
    if not os.path.exists('cnpjconsultado/cnpjs-consultados.csv'):
        with open('cnpjconsultado/cnpjs-consultados.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=field_names)
            writer.writeheader()
    os.system('cls' if os.name == 'nt' else 'clear')
    gravaExcel(inscricao)
    count(25)
