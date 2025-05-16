import pandas as pd

# Carregar o arquivo CSV com o separador correto e encoding
df = pd.read_csv('OCORRENCIAS_2025.csv', sep=';', encoding='latin1')

# Criar uma coluna de data só para referência (ano-mês-01)
df['DATA'] = pd.to_datetime(df['ANO_OCORRENCIA'].astype(str) + '-' + df['MES_OCORRENCIA'].astype(str).str.zfill(2) + '-01')

# Limpar espaços extras nas colunas categóricas para evitar duplicatas
df['TIPO_OCORRENCIA'] = df['TIPO_OCORRENCIA'].str.strip()
df['UF'] = df['UF'].str.strip()

# 1 - Contagem de ocorrências por UF (estado)
ocorrencias_por_uf = df.groupby('UF')['TOTAL'].sum().sort_values(ascending=False)

# 2 - Contagem de ocorrências por tipo de ocorrência
ocorrencias_por_tipo = df.groupby('TIPO_OCORRENCIA')['TOTAL'].sum().sort_values(ascending=False)

# 3 - Total geral de ocorrências
total_ocorrencias = df['TOTAL'].sum()

# 4 - Tabela cruzada (pivot) de ocorrências por UF e Tipo de Ocorrência
tabela_ocorrencias = df.pivot_table(
    index='UF',
    columns='TIPO_OCORRENCIA',
    values='TOTAL',
    aggfunc='sum',
    fill_value=0
)

# Mostrar os resultados formatados
print("Ocorrências por UF:")
print(ocorrencias_por_uf)

print("\nOcorrências por Tipo de Ocorrência:")
print(ocorrencias_por_tipo)

print(f"\nTotal geral de ocorrências: {total_ocorrencias}\n")

print("Tabela de ocorrências por UF e Tipo de Ocorrência:")
print(tabela_ocorrencias)
