"""
Cenário - A Solicitação do Gestor
O gestor de uma rede de lojas, Carlos, está preocupado com a performance de vendas de diferentes produtos 
nas cinco regiões onde a empresa atua. 
Ele quer compreender melhor os dados de vendas para tomar decisões estratégicas. 

Carlos faz as seguintes solicitações:

Resumo Geral: 

"Preciso entender o desempenho geral das vendas ao longo do tempo. 
Por favor, gere um gráfico que mostre as quantidades vendidas ao longo dos dias para 
identificarmos tendências de vendas."

Vendas por Produto: 

"Gostaria de ver a quantidade total vendida por cada produto. 
Um gráfico de barras seria ótimo para visualizar isso."

Distribuição Regional: 

"Como estão as vendas por região? Um gráfico de pizza poderia mostrar qual região está contribuindo mais."

Detalhes por Categoria e Região: 

"Consigo ver a relação entre categorias de produtos e regiões? Um heatmap seria ideal para isso."

Acompanhamento de Produtos Populares: 

"Quais produtos têm um desempenho consistente ao longo do tempo? 
Um gráfico de linha detalhado por produto pode ajudar."

"""
import pandas as pd
import plotly.express as px

df = pd.read_csv("visualizacao_de_vendas/dados_vendas_dashboard.csv")

print(df.head())
