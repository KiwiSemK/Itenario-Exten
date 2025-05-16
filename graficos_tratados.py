import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados
df = pd.read_csv('OCORRENCIAS_2025.csv', sep=';', encoding='latin1')

# Converter a coluna de data
df['DATA'] = pd.to_datetime(df['ANO_OCORRENCIA'].astype(str) + '-' + df['MES_OCORRENCIA'].astype(str).str.zfill(2) + '-01')

# Configurar o estilo dos gráficos
sns.set(style="whitegrid")
plt.rcParams.update({'figure.autolayout': True})  # Ajuste automático

# GRÁFICO 1 - Total de ocorrências por UF
ocorrencias_por_uf = df.groupby('UF')['TOTAL'].sum().sort_values(ascending=False)

plt.figure(figsize=(12, 6))
sns.barplot(x=ocorrencias_por_uf.index, y=ocorrencias_por_uf.values, palette='viridis')
plt.title('Total de Ocorrências por Estado (UF)')
plt.xlabel('UF')
plt.ylabel('Total de Ocorrências')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('grafico_ocorrencias_por_uf.png')
plt.show()

# GRÁFICO 2 - Ocorrências por tipo de ocorrência
ocorrencias_por_tipo = df.groupby('TIPO_OCORRENCIA')['TOTAL'].sum().sort_values(ascending=False)

plt.figure(figsize=(14, 8))
sns.barplot(x=ocorrencias_por_tipo.values, y=ocorrencias_por_tipo.index, palette='magma')
plt.title('Ocorrências por Tipo')
plt.xlabel('Total')
plt.ylabel('Tipo de Ocorrência')
plt.tight_layout()
plt.savefig('grafico_ocorrencias_por_tipo.png')
plt.show()

# GRÁFICO 3 - Linha do tempo mensal (Total de ocorrências por mês)
ocorrencias_mensal = df.groupby('DATA')['TOTAL'].sum()

plt.figure(figsize=(12, 5))
sns.lineplot(x=ocorrencias_mensal.index, y=ocorrencias_mensal.values, marker='o', color='dodgerblue')
plt.title('Ocorrências por Mês')
plt.xlabel('Data')
plt.ylabel('Total de Ocorrências')
plt.grid(True)
plt.tight_layout()
plt.savefig('grafico_linha_temporal.png')
plt.show()

#Esse gráfico só mostra os tipos com mais de 50 ocorrências, para evitar poluição visual. Pode ajustar isso.