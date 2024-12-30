-- Dimensão Data Locacao ---------------------

CREATE VIEW dim_dtLocacao AS
SELECT DISTINCT 
	dataLocacao,
	substr(dataLocacao, 1, 4) as anoLocacao,
	substr(dataLocacao, 5, 2) as mesLocacao,
	substr(dataLocacao, 7, 2) as diaLocacao,
	horaLocacao
FROM tbN_locacao tnl 

-- Dimensão Data Entrega ---------------------

CREATE VIEW dim_dtEntrega AS
SELECT DISTINCT 
	dataEntrega,
	substr(dataEntrega, 1, 4) as anoEntrega,
	substr(dataEntrega, 5, 2) as mesEntrega,
	substr(dataEntrega, 7, 2) as diaEntrega,
	horaEntrega
FROM tbN_locacao tnl 

-- Dimensão Carro ---------------------

CREATE VIEW dim_carro AS
SELECT DISTINCT 
	idCarro,
	kmCarro,
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro,
	tc2.tipoCombustivel
FROM tb_carro tc 
JOIN tb_combustivel tc2 
ON tc.combustivel = tc2.idCombustivel

-- Dimensão Vendedor ---------------------

CREATE VIEW dim_vendedor AS
SELECT DISTINCT 
	*
FROM tb_vendedor tv 

-- Dimensão Cliente  ---------------------

CREATE VIEW dim_cliente AS
SELECT DISTINCT 
	*
FROM tb_cliente tc 

-- Tabela fato Locação ---------------------

CREATE VIEW fato_locacao AS
SELECT 
	idLocacao,
	cliente,	
	carro,
	vendedor,
	dataLocacao,
	dataEntrega,
	qtdDiaria,
	vlrDiaria

FROM tbN_locacao tl 


-- view ---------------------

select * from dim_dtLocacao

select * from dim_dtEntrega 

select * from dim_carro

select * from dim_vendedor

select * from dim_cliente

select * from fato_locacao 