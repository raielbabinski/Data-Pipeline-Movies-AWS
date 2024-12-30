-- Exercicío 5
-- Apresente a query para listar o nome dos autores que 
-- publicaram livros através de editoras NÃO situadas 
-- na região sul do Brasil. Ordene o resultado pela coluna 
-- nome, em ordem crescente. Não podem haver nomes repetidos em seu retorno.
----------------------------------------------------------------

SELECT a.nome FROM autor AS a
INNER JOIN livro AS l
ON a.codautor = l.autor
INNER JOIN editora AS e
ON l.editora = e.codeditora
INNER JOIN endereco AS ed
ON e.endereco = ed.codendereco
WHERE ed.estado NOT IN ('RIO GRANDE DO SUL', 'SANTA CATARINA', 'PARANÁ')
GROUP BY a.nome
ORDER BY a.nome