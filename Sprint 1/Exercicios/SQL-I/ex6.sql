-- Exercicío 6
-- Apresente a query para listar o autor com maior número de 
-- livros publicados. O resultado deve conter apenas as colunas 
-- codautor, nome, quantidade_publicacoes.
----------------------------------------------------------------

SELECT a.codautor, a.nome, count(*) AS quantidade_publicacoes FROM livro
INNER JOIN autor AS a
ON livro.autor = a.codautor
GROUP BY autor
ORDER BY quantidade_publicacoes DESC
LIMIT 1