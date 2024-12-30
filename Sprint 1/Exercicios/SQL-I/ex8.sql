-- Exercicío 8
-- Apresente a query para listar o código e o nome do vendedor
-- com maior número de vendas (contagem), e que estas vendas estejam 
-- com o status concluída.  As colunas presentes no resultado devem ser, 
-- portanto, cdvdd e nmvdd.
----------------------------------------------------------------

SELECT tbvdd.cdvdd, tbvdd.nmvdd  FROM tbvendas tbv
INNER JOIN tbvendedor tbvdd
ON tbv.cdvdd = tbvdd.cdvdd 
WHERE status LIKE 'Concluído'
GROUP BY tbvdd.nmvdd 
ORDER BY count(*) DESC
LIMIT 1
