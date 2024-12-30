-- Criação das Tabelas

-- TABELA COMBUSTÍVEL -----------------------------

CREATE TABLE tb_combustivel (
	idCombustivel INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	tipoCombustivel VARCHAR(100) NOT NULL
)

-- TABELA CARRO -----------------------------

CREATE TABLE tb_carro (
	idCarro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	combustivel INT NOT NULL,
	kmCarro INT, 
	classiCarro VARCHAR(100) NOT NULL,
	marcaCarro VARCHAR(100) NOT NULL,
	modeloCarro VARCHAR(100) NOT NULL,
	anoCarro INT NOT NULL,
	FOREIGN KEY (combustivel) REFERENCES tb_combustivel (idCombustivel)
)

-- TABELA VENDEDOR -----------------------------

CREATE TABLE tb_vendedor(
	idVendedor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	nomeVendedor VARCHAR(100) NOT NULL,
	sexoVendedor VARCHAR(20) NOT NULL,
	estadoVendedor VARCHAR(100) NOT NULL
)	

-- TABELA CLIENTE -----------------------------

CREATE TABLE tb_cliente (
	idCliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	nomeCliente VARCHAR(100) NOT NULL,
	cidadeCliente VARCHAR(100) NOT NULL,
	estadoCliente VARCHAR(100) NOT NULL,
	paisCliente VARCHAR(100) NOT NULL
)

-- TABELA LOCACÃO -----------------------------

CREATE TABLE tbN_locacao (
	idLocacao INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	cliente INT NOT NULL,
	carro INT NOT NULL,
	vendedor INT NOT NULL,
	dataLocacao DATE NOT NULL,
	horaLocacao TIME NOT NULL,
	qtdDiaria INT NOT NULL,
	vlrDiaria INT NOT NULL,
	dataEntrega DATE NOT NULL,
	horaEntrega TIME NOT NULL,
	FOREIGN KEY(cliente) REFERENCES tb_cliente(idCliente),
	FOREIGN KEY(carro) REFERENCES tb_carro(idCarro),
	FOREIGN KEY(vendedor) REFERENCES tb_vendedor(idVendedor)
)


-- INSERSÃO DE DADOS --------------------------------------

-- INSERE DADOS COMBUSTÍVEL

INSERT INTO tb_combustivel (
	idCombustivel, 
	tipoCombustivel
)
SELECT DISTINCT 
	idCombustivel, 
	tipoCombustivel 
FROM tb_locacao 

-- INSERE DADOS DOS CARROS

INSERT INTO tb_carro (
	idCarro, 
	combustivel, 
	kmCarro, 
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro 
)
SELECT 
	idCarro, 
	idcombustivel, 
	kmCarro, 
	classiCarro,
	marcaCarro,
	modeloCarro,
	anoCarro 
FROM tb_locacao tl 
GROUP BY idCarro 

-- INSERE DADOS DOS VENDEDORES

INSERT INTO tb_vendedor (
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
)
SELECT 
	idVendedor,
	nomeVendedor, 
	sexoVendedor,
	estadoVendedor 
FROM tb_locacao tl 
GROUP BY idVendedor 

-- INSERE DADOS DOS CLIENTES

INSERT INTO tb_cliente (
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente
)
SELECT DISTINCT 
	idCliente,
	nomeCliente,
	cidadeCliente,
	estadoCliente,
	paisCliente 
FROM tb_locacao tl 

-- INSERE AS LOCAÇÕES

INSERT INTO tbN_locacao 
SELECT 
	idLocacao, 
	idCliente, 
	idCarro,
	idVendedor,
	dataLocacao,
	horaLocacao,
	qtdDiaria,
	vlrDiaria,
	dataEntrega,
	horaEntrega 
FROM tb_locacao tl 

----------------------------------------------------------------------------------------

-- Visualização das tabelas

select * from tbN_locacao tnl 

select * from tb_cliente tc 

select * from tb_vendedor tv 

select * from tb_carro tc 

select * from tb_combustivel tc 

select * from tb_locacao tl 