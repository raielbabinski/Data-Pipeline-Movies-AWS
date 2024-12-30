-- Exercicío 11
-- Apresente a query para listar o código e nome 
-- cliente com maior gasto na loja. As colunas 
-- presentes no resultado devem ser cdcli, nmcli 
-- e gasto, esta última representando o somatório das 
-- vendas (concluídas) atribuídas ao cliente.
----------------------------------------------------------------

SELECT cdcli, nmcli, sum(qtd * vrunt) AS gasto FROM tbvendas
GROUP BY nmcli 
ORDER BY sum(qtd * vrunt) DESC
LIMIT 1