-- Exercicío 12
-- Apresente a query para listar código, nome 
-- e data de nascimento dos dependentes do vendedor 
-- com menor valor total bruto em vendas (não sendo zero). 
-- As colunas presentes no resultado devem ser cddep,
-- nmdep, dtnasc e valor_total_vendas.
----------------------------------------------------------------

SELECT cddep, nmdep, dtnasc, sum(tv.qtd * tv.vrunt) AS valor_total_vendas FROM tbdependente tdp
LEFT JOIN tbvendedor tvdd
ON tdp.cdvdd = tvdd.cdvdd 
LEFT JOIN tbvendas tv 
ON tvdd.cdvdd = tv.cdvdd 
WHERE tv.status = 'Concluído'
GROUP BY tdp.cdvdd 
ORDER BY sum(tv.qtd * tv.vrunt)
LIMIT 1