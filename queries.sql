
-- Pelo menos 10 queries em SQL que retornem informações interessantes


--1. Listar todas as séries feitas por um diretor específico

SELECT s.nome AS serie, d.nome AS diretor
FROM "Serie" s
JOIN "Diretor" d ON s.id_diretor = d.id_diretor
WHERE d.nome = 'Sarah Moura';

--2. Listar todas as temporadas de uma série e suas informações
SELECT s.nome, t.numero_temp AS temporada, t.qtd_ep AS episodios, t.nota_avaliacao AS nota
FROM "Temporada" t
JOIN "Serie" s ON t.id_serie = s.id_serie
WHERE s.nome = 'A certeza de evoluir mais rapidamente'
ORDER BY t.numero_temp;

--3. Listar séries de um gênero específico
SELECT nome, qtd_temporadas, restricao_idade
FROM "Serie"
WHERE genero = 'Romance'
ORDER BY nome;

-- 4. Atores que trabalham em séries de uma produtora específica
SELECT a.nome AS ator, s.nome AS serie
FROM "Ator" a
JOIN "Temporada" t ON a.id_ator = t.id_ator
JOIN "Serie" s ON t.id_serie = s.id_serie
JOIN "Produtora" p ON s.id_prod = p.id_prod
WHERE p.nome_produtora = 'Cardoso'
ORDER BY a.nome;

--5. Séries com melhor avaliação média
SELECT s.nome AS serie, ROUND(AVG(t.nota_avaliacao):: numeric, 2) AS media_avaliacao
FROM "Serie" s
JOIN "Temporada" t ON s.id_serie = t.id_serie
GROUP BY s.nome
ORDER BY media_avaliacao DESC
LIMIT 10;

--6. Diretores e o número de séries que dirigem
SELECT d.nome AS diretor, 
       CASE 
           WHEN COUNT(s.id_serie) = 0 THEN 'Nenhuma' 
           ELSE COUNT(s.id_serie)::TEXT 
       END AS qtd_series
FROM "Diretor" d
LEFT JOIN "Serie" s ON d.id_diretor = s.id_diretor
GROUP BY d.nome
ORDER BY qtd_series ASC;


--7. Episódios com melhor avaliação de uma série específica
SELECT e.titulo, e.nota_avaliacao, t.numero_temp AS temporada
FROM "Episodio" e
JOIN "Temporada" t ON e.id_temp = t.id_temp
JOIN "Serie" s ON t.id_serie = s.id_serie
WHERE s.nome = 'A certeza de evoluir mais rapidamente'
ORDER BY e.nota_avaliacao DESC
LIMIT 5;

--8. Produtoras e o total de séries que produziram
SELECT p.nome_produtora AS Produtora,
       CASE 
           WHEN COUNT(s.id_serie) = 0 THEN 'Nenhuma' 
           ELSE COUNT(s.id_serie)::TEXT 
       END AS total_series
FROM "Produtora" p
LEFT JOIN "Serie" s ON p.id_prod = s.id_prod
GROUP BY p.nome_produtora
ORDER BY total_series ASC;

--9. Atores que aparecem em mais temporadas de séries diferentes
SELECT a.nome AS ator, COUNT(DISTINCT t.id_serie) AS qtd_series
FROM "Ator" a
JOIN "Temporada" t ON a.id_ator = t.id_ator
GROUP BY a.nome
ORDER BY qtd_series DESC
LIMIT 10;

--10. Média de duração dos episódios por temporada de uma série
SELECT s.nome AS serie, t.numero_temp AS temporada, 
       ROUND(AVG(e.duracao):: numeric, 2) AS Media_Minutos_Medio
FROM "Episodio" e
JOIN "Temporada" t ON e.id_temp = t.id_temp
JOIN "Serie" s ON t.id_serie = s.id_serie
WHERE s.nome = 'A certeza de evoluir mais rapidamente'
GROUP BY s.nome, t.numero_temp
ORDER BY t.numero_temp;
