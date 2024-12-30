-- Exercicío 10
-- A comissão de um vendedor é definida a
--  partir de um percentual sobre o total 
-- de vendas (quantidade * valor unitário) 
-- por ele realizado. O percentual de comissão 
-- de cada vendedor está armazenado na coluna 
-- perccomissao, tabela tbvendedor. 

-- Com base em tais informações, calcule 
-- a comissão de todos os vendedores, considerando
-- todas as vendas armazenadas na base de dados
-- com status concluído.

-- As colunas presentes no resultado devem 
-- ser vendedor, valor_total_vendas e comissao.
-- O valor de comissão deve ser apresentado 
-- em ordem decrescente arredondado na segunda
-- casa decimal.
--------------------------------------

SELECT  tvd.nmvdd AS vendedor, 
        sum(qtd* tv.vrunt) AS valor_total_vendas, 
        round((sum(qtd* tv.vrunt)*tvd.perccomissao/100), 2) AS comissao 
FROM tbvendas tv
INNER JOIN tbvendedor tvd 
ON tv.cdvdd = tvd.cdvdd 
WHERE status = 'Concluído'
GROUP BY tv.cdvdd  
ORDER BY comissao DESC