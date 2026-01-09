# 🎬 AWS Movie Analytics Pipeline
### Engenharia de Dados End-to-End: Da Ingestão ao Insight

Este projeto simula um ambiente de produção real para o processamento de grandes volumes de dados cinematográficos. O foco foi construir uma arquitetura escalável e de baixo custo utilizando serviços **AWS** e processamento distribuído com **PySpark**.

---

## 🏗️ Arquitetura do Sistema
O pipeline segue o padrão de arquitetura de **Data Lake** em camadas para garantir a qualidade e organização dos dados.

![Arquitetura do Projeto](./Sprint%208/Evidencias/pipeline.jpeg)

1. **Ingestão (Serverless):** Utilização de **AWS Lambda** para busca de dados em APIs externas, gerenciando a extração inicial para o ambiente cloud.
2. **Storage (S3):** Organização dos dados no **Amazon S3** seguindo o modelo de Data Lake:
    * **Bronze:** Dados brutos em formato original (JSON/CSV).
    * **Silver:** Dados limpos e padronizados com Spark.
    * **Gold:** Dados agregados e otimizados para consulta (formato **Parquet**).
3. **Processamento (Big Data):** Construção de pipelines ETL utilizando **Spark** e **AWS Glue** para transformações, limpeza e particionamento dos dados.
4. **Consumo e BI:** Criação de tabelas e consultas no **Amazon Athena** para análise de dados, com visualização final de insights em dashboards no **QuickSight**.

---

## 🛠️ Tecnologias e Ferramentas
* **Linguagem:** Python.
* **Processamento Distribuído:** Spark / AWS Glue.
* **Nuvem:** AWS (S3, Lambda, Athena, QuickSight).
* **Ferramentas:** Docker e Git/GitHub.
* **Metodologia:** Participação em sprints ágeis (Scrum).

---

## 🚀 Principais Aprendizados e Diferenciais Técnicos

* **Otimização de Custos:** Implementação de armazenamento em **Parquet** com particionamento, reduzindo o volume de dados escaneados e melhorando a performance de consulta.
* **Resiliência:** Tratamento de dados brutos para garantir a integridade das informações antes da carga no Data Lake.
* **Modelagem de Dados:** Aplicação de conceitos de modelagem para transformar dados de fontes diversas em informações prontas para análise de negócio.

---

## 📊 Visualização dos Resultados
O dashboard final permite analisar métricas de performance e tendências do setor cinematográfico.

![Dashboard Preview](./Sprint%208/Evidencias/Dashboard.png)

---

## 📁 Acesso Direto aos Códigos
* [**Script de Processamento (PySpark)**](./Sprint%207/Desafio/jobRef.py)
* [**Scripts de Ingestão (Lambda)**](./Sprint%205/Desafio/etapa-II/ingestao.py)