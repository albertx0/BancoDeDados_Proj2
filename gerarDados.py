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
ID_SERIES = set()
ID_TEMPORADAS = set()
ID_EPISODIOS = set()

NOMES_PRODUTORAS = set()
NOMES_FUNCIONARIOS = set()
NOMES_SERIES = set()
NOMES_EPISODIOS = set()
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

# dicionario de lista para ter armazenado os atores 
# presentes em cada produtora
atores_por_prod = {

}

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

# funcao para gerar 
# nomes de series
def gerar_nome_serie():
    while 1:
        nome = faker.catch_phrase()

        if nome in NOMES_SERIES:
            continue

        NOMES_SERIES.add(nome)

        return nome

# funcao para gerar 
# nomes dos episodios 
def gerar_nome_episodio():
    while 1:
        nome = faker.catch_phrase()

        if nome in NOMES_EPISODIOS:
            continue

        NOMES_SERIES.add(nome)

        return nome

# funcao para gerar
# ids para series
def gerar_id_series():
    while 1:
        ID = faker.bothify("??###?")

        if ID in ID_SERIES:
            continue

        ID_SERIES.add(ID)

        return ID

def gerar_id_temporadas():
    while 1:
        ID = faker.bothify("??###")

        if ID in ID_TEMPORADAS:
            continue
        
        ID_TEMPORADAS.add(ID)

        return ID

def gerar_id_episodios():
    while 1:
        ID = faker.bothify("???##")

        if ID in ID_EPISODIOS:
            continue
        
        ID_EPISODIOS.add(ID)

        return ID

def gerar_salario():
    return round(random.uniform(1500, 20000), 2)

def gerar_genero():
    return faker.random_element(generos_series)

def gerar_restricao_idade():
    return faker.random_element(restricao_idade)

def gerar_produtoras():
    produtoras = []

    for i in range(qtd_produtoras):
        id_prod = gerar_id_produtora()

        produtoras.append({
            "id_prod" : id_prod,
            "nome_produtora" : gerar_nome_produtora(),
            "CEO" : gerar_nome_funcionario()
            })
        atores_por_prod[id_prod] = []
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
        id_prod = id_produtora_aleatoria(produtoras)
        id_ator = gerar_id_funcionario()

        atores.append({
            "id_ator" : id_ator,
            "nome" : gerar_nome_funcionario(),
            "salario" : gerar_salario(),
            "id_prod" : id_prod
            })
        
        atores_por_prod[id_prod].append(id_ator)
    return atores

def diretor_aleatorio(diretores):
    return faker.random_element(diretores)

def restricao_aleatoria():
    return faker.random_element(restricao_idade)

def genero_aleatorio():
    return faker.random_element(generos_series)

def gerar_series(diretores):
    series = []

    for i in range(qtd_series):
        diretor = diretor_aleatorio(diretores)

        series.append({
            "id_serie" : gerar_id_series(),
            "nome" : gerar_nome_serie(),
            "restricao_idade" : restricao_aleatoria(),
            "genero" : genero_aleatorio(),
            "qtd_temporadas" : random.randint(1, 5),
            "id_prod" : diretor["id_prod"],
            "id_diretor" : diretor["id_diretor"]
            })
    return series

def gerar_temporadas(series):
    temporadas = []

    for serie in series:
        
        for i in range(serie["qtd_temporadas"]): 
            ID = gerar_id_temporadas()
            id_prod = serie["id_prod"]

            temporadas.append({
                "id_temp" : ID,
                "qtd_ep" : random.randint(1, 12), 
                "nota_avaliacao" : round(random.uniform(0, 10), 2),
                "numero_temp" : i+1,
                "id_serie" : id_prod,
                "id_ator" : faker.random_element(atores_por_prod[id_prod])
                 })
    return temporadas

def gerar_episodios(temporadas):
    episodios = []

    for temporada in temporadas:
        id_temp = temporada["id_temp"]
        for i in range(temporada["qtd_ep"]):
            ID = gerar_id_episodios()
            titulo = gerar_nome_episodio()
        episodios.append({
            "id_ep" : ID, 
            "titulo" : titulo,
            "duracao" : random.randint(20, 100),
            "nota_avaliacao" : round(random.uniform(0, 10), 2),
            "id_temp" : id_temp
            })
    return episodios

def exportar_csv(nome_arquivo, lista_dicionarios):
    if not lista_dicionarios:
        print(f"[!] Lista vazia, não exportou: {nome_arquivo}")
        return

    os.makedirs("DadosCsv", exist_ok=True)

    caminho = os.path.join("DadosCsv", nome_arquivo)

    with open(caminho, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=lista_dicionarios[0].keys())
        writer.writeheader()
        writer.writerows(lista_dicionarios)
    print(f"[✓] Exportado: {nome_arquivo}")

if __name__ == "__main__":
    produtoras = gerar_produtoras()
    diretores = gerar_diretores(produtoras)
    atores = gerar_atores(produtoras)
    series = gerar_series(diretores)
    temporadas = gerar_temporadas(series)
    episodios = gerar_episodios(temporadas)
    
    exportar_csv("Produtora", produtoras)
    exportar_csv("Diretor", diretores)
    exportar_csv("Ator", atores)
    exportar_csv("Serie", series)
    exportar_csv("Temporada", temporadas)
    exportar_csv("Episodio", episodios)
