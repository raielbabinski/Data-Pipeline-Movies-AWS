-- Exercicío 7
-- Apresente a query para listar o nome dos autores com 
-- nenhuma publicação. Apresentá-los em ordem crescente.
----------------------------------------------------------------

SELECT nome FROM autor AS a
LEFT JOIN livro AS l
ON a.codautor = l.autor
WHERE l.autor IS NULL
ORDER BY nome