from faker import Faker
import string
import csv 
import os
import random

faker = Faker("pt-BR")
nums = string.digits

# /////////////////////
# intervalo dos dados
qtd_produtoras = 3
qtd_atores = 10
qtd_diretores = 5
qtd_series = 5
# /////////////////////

# utilizacao de sets globais
# para evitar a repeticao de elementos
# unicos

ID_PRODUTORAS = set()
ID_FUNCIONARIOS = set()
ID_SERIE = set()

NOMES_PRODUTORAS = set()
NOMES_FUNCIONARIOS = set()

# /////////////////////

# Listas que possuem dados estaticos
generos_series = [
    "Acao",
    "Aventura",
    "Comedia",
    "Drama",
    "Ficcao Cientifica",
    "Fantasia",
    "Misterio",
    "Suspense",
    "Terror",
    "Romance",
    "Policial",
    "Crime",
    "Documentario",
    "Animacao",
    "Musical",
    "Guerra",
    "Historico",
    "Esporte",
    "Super-heroi",
    "Reality Show"
]

restricao_idade = [
    "AL",
    "A10",
    "A12",
    "A14",
    "A16",
    "A18"
]

# /////////////////////

# funcao para gerar id
# somente para produtoras
def gerar_id_produtora():
    while 1:
        ID = faker.bothify("???###")

        if ID in ID_PRODUTORAS:
            continue

        ID_PRODUTORAS.add(ID)

        return ID

def gerar_nome_produtora():
    while 1:
        nome = faker.company()

        if nome in NOMES_PRODUTORAS:
            continue

        NOMES_PRODUTORAS.add(nome)

        return nome

# funcao para gerar id
# somente de funcionarios
def gerar_id_funcionario():
    while 1:
        ID = "".join(random.choices(nums, k=6))

        if ID in ID_FUNCIONARIOS:
                     continue
        ID_FUNCIONARIOS.add(ID)

        return ID;

# funcao para gerar 
# nomes de funcionarios
def gerar_nome_funcionario():
    while 1:
        nome = faker.name()

        if nome in NOMES_FUNCIONARIOS:
            continue
        
        NOMES_FUNCIONARIOS.add(nome)

        return nome

def gerar_salario():
    return round(random.uniform(1500, 20000), 2)

def gerar_genero():
    return faker.random_element(generos_series)

def gerar_restricao_idade():
    return faker.random_element(restricao_idade)

def gerar_produtoras():
    produtoras = []

    for i in range(qtd_produtoras):
        produtoras.append({
            "id_prod" : gerar_id_produtora(),
            "nome_produtora" : gerar_nome_produtora(),
            "CEO" : gerar_nome_funcionario()
            })
    return produtoras

def id_produtora_aleatoria(produtoras):
    ID = faker.random_element(produtoras)["id_prod"]
    return ID

def gerar_diretores(produtoras):
    diretores = []

    for i in range(qtd_diretores):
        diretores.append({
            "id_diretor" : gerar_id_funcionario(),
            "nome" : gerar_nome_funcionario(),
            "salario" : gerar_salario(),
            "id_prod" : id_produtora_aleatoria(produtoras)
            })
    return diretores
 
def gerar_atores(produtoras):
    atores = []

    for i in range(qtd_atores):
        atores.append({
            "id_ator" : gerar_id_funcionario(),
            "nome" : gerar_nome_funcionario(),
            "salario" : gerar_salario(),
            "id_prod" : id_produtora_aleatoria(produtoras)
            })
    return atores


if __name__ == "__main__":
    produtoras = gerar_produtoras()
    diretores = gerar_diretores(produtoras)
    atores = gerar_atores(produtoras)

    print(atores)
