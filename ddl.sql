CREATE TABLE "Produtora" (
  "id_prod" varchar(30) PRIMARY KEY
  ,"nome_produtora" varchar(100)
  ,"CEO" varchar(100)
);

CREATE TABLE "Diretor" (
  "id_diretor" varchar(30) PRIMARY KEY
  ,"nome" varchar(100) UNIQUE
  ,"salario" float
  ,id_prod varchar(30)
  ,FOREIGN KEY ("id_prod") REFERENCES "Produtora" ("id_prod")
);

CREATE TABLE "Ator" (
  "id_ator" varchar(30) PRIMARY KEY
  ,"nome" varchar(100) UNIQUE
  ,"salario" float
  ,id_prod varchar(30)
  ,FOREIGN KEY ("id_prod") REFERENCES "Produtora" ("id_prod")
);

CREATE TABLE "Serie" (
  "id_serie" varchar(30) PRIMARY KEY
  ,"nome" varchar(100) UNIQUE
  ,"restricao_idade" integer
  ,genero varchar(100)
  ,id_prod varchar(30)
  ,id_diretor varchar(30)
  ,FOREIGN KEY ("id_prod") REFERENCES "Produtora" ("id_prod")
  ,FOREIGN KEY ("id_diretor") REFERENCES "Diretor" ("id_diretor")
);

CREATE TABLE "Temporada" (
  "id_temp" varchar(30) PRIMARY KEY
  ,qtd_ep integer
  ,nota_avaliacao float
  ,numero_temp integer
  ,id_serie varchar(30)
  ,id_ator varchar(30)
  ,FOREIGN KEY ("id_serie") REFERENCES "Serie" ("id_serie")
  ,FOREIGN KEY ("id_ator") REFERENCES "Ator" ("id_ator")
);

CREATE TABLE "Episodio" (
  "id_ep" varchar(30) PRIMARY KEY
  ,titulo varchar(100) UNIQUE 
  ,duracao integer
  ,nota_avaliacao float
  ,"id_temp" varchar(30)
  ,FOREIGN KEY ("id_temp") REFERENCES "Temporada" ("id_temp")
);
