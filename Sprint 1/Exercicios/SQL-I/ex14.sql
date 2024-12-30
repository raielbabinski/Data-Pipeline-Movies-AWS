-- Exercicío 14
-- Apresente a query para listar o gasto médio por 
-- estado da federação. As colunas presentes no 
-- resultado devem ser estado e gastomedio. Considere 
-- apresentar a coluna gastomedio arredondada na segunda 
-- casa decimal e ordenado de forma decrescente.
----------------------------------------------------------------

SELECT estado, ROUND(avg(qtd * tbvendas.vrunt), 2) AS gastomedio FROM tbvendas 
WHERE status = 'Concluído'
GROUP BY estado
ORDER BY gastomedio DESC