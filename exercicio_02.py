# 2) Criar um programa onde o usuário digite dois valores e apareça a soma

# Recebendo os dois números e armazenando-os nas variáves "numero_1" e "numero_2"
numero_1 = int(input("Digite o primeiro numero: "))
numero_2 = int(input("Digite o segundo numero: "))

# Soma das variáveis "numero_1" e "numero_2", armazenando o resultado na variável "soma"
soma = numero_1 + numero_2

# Printando uma mensagem com o resultado da soma utilizando f-string
print(f"A soma dos números digitados é: {soma}")
