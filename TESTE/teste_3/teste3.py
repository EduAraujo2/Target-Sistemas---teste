import json

# leitura do arquivo json
#obs: caso o arquivo json nao possa ser aberto será necessário inserir todo o caminho até a pasta
with open('dados.json') as file:
    faturamento = json.load(file)

# aqui comeca a verificar as variaveis de maior e menor valor
menor_valor = faturamento[0]['valor']
maior_valor = faturamento[0]['valor']

# calculo da media mensal
tFaturamento = 0
diasFaturamento = 0

# fazendo a varredura do vetor
for dia in faturamento:
    valor = dia['valor']

# altera o valor das variaveis
    if valor < menor_valor:
        menor_valor = valor
    if valor > maior_valor:
        maior_valor = valor

# calculando a media mensal sem faturamento
    if valor > 0:
        tFaturamento += valor
        diasFaturamento += 1

# calculando a media mensal
media_mensal = tFaturamento / diasFaturamento

# calculando os dias diario que a media mensal foi maior
dias_acima_da_media = 0
for dia in faturamento:
    if dia['valor'] > media_mensal:
        dias_acima_da_media += 1


print('O menor valor de faturamento ocorrido em um dia do mês:', menor_valor)
print('O maior valor de faturamento ocorrido em um dia do mês:', maior_valor)
print('Número de dias no mês em que o valor de faturamento diário foi superior à média mensal:', dias_acima_da_media)
