-- Exercicío 4
-- Apresente a query para listar a quantidade de livros publicada 
-- por cada autor. Ordenar as linhas pela coluna nome (autor), 
-- em ordem crescente. Além desta, apresentar as colunas codautor, 
-- nascimento e quantidade (total de livros de sua autoria).
--------------------------------------------------------------------------------

SELECT a.nome, a.codautor, a.nascimento, COUNT(l.titulo) AS quantidade FROM autor AS a
LEFT JOIN livro AS l
ON a.codautor = l.autor
GROUP BY a.nome
ORDER BY a.nome