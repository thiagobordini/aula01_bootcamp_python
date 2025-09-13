# Questão: Cálculo de Bônus com Entrada do Usuário

# Escreva um programa em Python que solicita ao usuário para digitar seu nome, o
# valor do seu salário mensal e o valor do bônus que recebeu. O programa deve,
# então, imprimir uma mensagem saudando o usuário pelo nome e informando o valor
# do salário em comparação com o bônus recebido.

# Cálculo do KPI: 1000 + salário * bônus

# Recebendo o nome do usuário e armazenando-o na variável "nome_usuario"
nome_usuario = input("Digite o seu nome: ")

# Recebendo o salário mensal do usuário e armazenando-o na variável "salario_usuario"
salario_usuario = float(input("Digite o seu salário: "))

# Recebendo o bônus salarial do usuário e armazenando-o na variável "bonus_salarial"
bonus_salarial = float(input("Bônus salarial: "))

# Cálculo do bônus do usuário
bonus = int(1000 + (salario_usuario * bonus_salarial))

# Mensagem final com f-string
print(f"\nOlá {nome_usuario}, o seu bônus foi de {bonus}")
