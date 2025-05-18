# Projeto 2 -> Banco de dados

## Integrantes do Grupo

| Nome                                  | RA             |
|---------------------------------------|----------------|
| Gabriel Albertini Pinheiro           | 22.124.094-8   |
| Alexandre Domiciano Pierri           | 22.125.061-6   |
| Kawan Mark Gerononimo da Silva       | 22.222.010-5   |

---

## Descrição do Projeto

Banco de dados relacional para gestão de séries, com:

- Cadastro completo de produtoras, diretores e elenco
- Organização hierárquica de séries, temporadas e episódios
- Controle salarial e de avaliações
- 
---

## Como Executar

### Pré-requisitos

- PostgreSQL 
- Python 

### Configuração

1. Criar banco de dados:
```sql
CREATE DATABASE series_db;
```

2. Executar DDL:
```bash
psql -U [user] -d series_db -f schema.sql
```

3. Popular Dados:
```bash
python gerarDados.py
```





# Modelo Entidade-Relacionamento (MER)



# Modelo Relacional (MR)






