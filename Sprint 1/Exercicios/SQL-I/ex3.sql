-- Exercicío 3
-- Apresente a query para listar as 5 editoras com mais 
-- livros na biblioteca. O resultado deve conter apenas as 
-- colunas quantidade, nome, estado e cidade. Ordenar as 
-- linhas pela coluna que representa a quantidade de livros em ordem decrescente.
--------------------------------------------------------------------------------

SELECT COUNT(*) AS quantidade , e.nome, ed.estado, ed.cidade
FROM livro AS l
LEFT JOIN editora AS e
ON l.editora = e.codeditora
LEFT JOIN endereco AS ed
ON e.endereco = ed.codendereco
GROUP BY editora
order by quantidade DESC