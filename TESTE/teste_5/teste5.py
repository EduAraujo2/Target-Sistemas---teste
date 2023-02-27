string = "Olá, Target Sistemas! Me proporcione essa oportunidade para que eu possa adquirir experiência :P"

# lista vazia para armazenar
invertida_string = []

# deixando de trás para frente
for i in range(len(string)-1, -1, -1):
    invertida_string.append(string[i])

# juntando os caracteres
invertida_string = ''.join(invertida_string)

# 
print("A string invertida é:", invertida_string)
