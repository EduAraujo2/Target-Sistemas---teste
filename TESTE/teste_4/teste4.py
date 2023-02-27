#valores dos faturamentos, para consulta
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

tFaturamento = sum(faturamento.values())

#para cada estado é calculado o percentual de representacoes e dividindo o valor total e multiplicado por 100
for estado, valor in faturamento.items():
    percentual = (valor / tFaturamento) * 100
    print(f"{estado} - {percentual:.2f}%")
