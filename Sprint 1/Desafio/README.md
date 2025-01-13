# Resolução Desafio

Essa é a documentação do Desafio final, que tinha como objetivo a normalização do banco de dados concessionária, e a criação de um modelo lógico e físico relacional, e posteriormente a criação de um modelo lógico e físico dimensional.


## Etapa I

### Identificar os erros de normalização

Para resolução do desafio foi nos dado a tabela concessionaria, que está desnormalizada. O desafio é reorganizar as colunas em novas tabelas com novos relacionamentos, respeitando as **Formas Normais**.

![Colunas da tb_locacao](/Sprint%201/Evidencias/colunas_tbConces.png)

Como essa tabela se refere as locações, um dos primeiros problemas, são informações que não se relacionam com a locação, como, por exemplo, a marca do carro. Um carro pode ser alugado mais de uma vez, e podem existir dois carros em uma concessionária com a mesma marca, ou duas pessoas que alocaram um carro com a mesma marca, isso gera repetição de dados. Então se for necessário atualizar a marca de um veículo, tera que modificar todos os registros repetidos na tabela locação.

Para resolver isso, não só com carros, mas com outras colunas que contém o mesmo problema, como é o caso de:

- Cliente
- Vendedor
- Combustivel

Vamos criar novas tabelas com relações únicas, onde vinculado a chave, há ocorrência de uma informação por atributo, assim vamos respeitar a **Primeira Forma Normal**. Para a **Segunda Forma Normal**, devemos fazer com que todos os atributos dependam da **chave primaria (PK)**, e para a **Terceira Forma Normal**, eliminar as dependências transitivas, ou seja, retirar atributos que dependem indiretamente da chave primaria, por meio de outro atributo não-chave.


### Criando o Modelo Lógico

![Modelo logico Concessionaria Normalizada](/Sprint%201/Evidencias/ModelagemRelacional.png)

Para construir a tabela comecei separando as entidades identificadas e tabelas próprias, e após isso, relacionei as tabelas determinando as cardinalidades. Como exemplo tabela locação se relaciona de forma que toda a locação necessita de um cliente, vendedor e carro, porém um carro, cliente ou vendedor pode existir sem ter feito nenhuma locação. Com o diagrama pronto podemos construir o Modelo físico.


## Etapa II

[Modelo Fisico Relacional - Etapa II](/Sprint%201/Desafio/etapa-2/modeloRelacional.sql)

### Criando as Tabelas do Modelo Físico

Primeiramente, criei as tabelas que eram somente referenciadas, como, por exemplo, a tb_combustivel, tb_cliente e tb_vendedor, após isso, criei as tabelas que faziam as relações começando com a tb_carro e depois a principal tbN_locacao. OBS: Utilizei o 'N' para diferenciar da tb_locacao, 'N' para normalizada. 


- Código de criação da tabela tbN_locacao:
```sql
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
```
 - Código rodando:

![Codigo Criacao Rodando](/Sprint%201/Evidencias/CriacaoLocacao.png)

- Modelo lógico no DBeaver:

![Modelo logico Concessionaria Normalizada](/Sprint%201/Evidencias/MLconcessDB.png)

### Inserindo Dados na Tabela Normalizada
 
Para inserir os dados nas tabelas novas, primeiro construí uma tabela nova a partir do ```SELECT``` usando a tabela desnormalizada (tb_locacao) como base, mas filtrando repetições usando ```GROUP BY/DISTINCT```, e depois com a tabela filtrada fiz a população das novas tabelas usando o ```INSERT INTO```.


- Código para inserir dados na Tabela de Clientes:

```sql 
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
```

- Código rodando:

![Código Insercao Rodando](/Sprint%201/Evidencias/IsercaoClientes.png)


- SELECT na tabela Clientes

![Select Tabela Clientes](/Sprint%201/Evidencias/TabelaClientes.png)

- SELECT na tabela locação normalizada:
 
![Select Tabela locacao](/Sprint%201/Evidencias/TabelaLocacaoNor.png)

Aqui podemos ver somente foreign keys, para as colunas, cliente, carro, vendedor.

## Etapa III

### Criação do Modelo Dimensional

Para criar um modelo dimensional temos que ter em mente que ele visa a análise de dados. Usando o Star Schema como base, vamos criar uma tabela fato, nesse caso será a tabela locação, já que ela é o evento responsável por ligar as dimensões, que serão:

- dim_cliente
- dim_carro
- dim_vendedor
- dim_dtLocacao
- dim_dtEntrega

Nesse caso a tabela ficará desnormalizada, preço a ser pago para ter mais eficiência nas análises, mas poderíamos normalizar as tabelas, e ter um modelo Snowflake.

Diagrama da Modelagem Dimensional:

![Diagrama Modelagem Dimensional](/Sprint%201/Evidencias/ModelagemDimensional.png)

## Etapa IV

[Modelo Fisico Dimensional - Etapa IV](/Sprint%201/Desafio/etapa-4/modeloDimensional.sql)

Para criação do modelo Dimensional utilizei das views, criei uma view para cada dimensão, segue o exemplo da dim_carro:

```sql
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
 ```

Com esse modelo poderiamos fazer consultas de forma eficiente utilizando a tabela fato Locação.

Imagem da fato_locacao:

![Tabela Fato Locacao](/Sprint%201/Evidencias/tabelaFatoLocacao.png)

Esse é o fim do desafio, aprendi muito logo na primeira Sprint, principalmente sql e modelagem de dados, sobre a documentação também, acredito que posso melhorar muito com o markdown ainda, foi uma experiencia desafiadora, mas recompensadora.
