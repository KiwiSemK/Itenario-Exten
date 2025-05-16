import pandas as pd

# Carregar o arquivo CSV com o separador correto e encoding
df = pd.read_csv('OCORRENCIAS_2025.csv', sep=';', encoding='latin1')

# Criar uma coluna de data só para referência (ano-mês-01)
df['DATA'] = pd.to_datetime(df['ANO_OCORRENCIA'].astype(str) + '-' + df['MES_OCORRENCIA'].astype(str).str.zfill(2) + '-01')

# 1 - Contagem de ocorrências por UF (estado)
ocorrencias_por_uf = df.groupby('UF')['TOTAL'].sum().sort_values(ascending=False)

# 2 - Contagem de ocorrências por tipo de ocorrência
ocorrencias_por_tipo = df.groupby('TIPO_OCORRENCIA')['TOTAL'].sum().sort_values(ascending=False)

# 3 - Total geral de ocorrências
total_ocorrencias = df['TOTAL'].sum()

# Mostrar os resultados formatados
print("Ocorrências por UF:")
print(ocorrencias_por_uf)

print("\nOcorrências por Tipo de Ocorrência:")
print(ocorrencias_por_tipo)

print(f"\nTotal geral de ocorrências: {total_ocorrencias}")
