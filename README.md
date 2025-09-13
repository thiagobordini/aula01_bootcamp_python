
# Aula 01 - Bootcamp Python (Jornada de Dados)

## Método `print()`

O método `print()` no Python é uma função embutida usada para exibir informações na saída padrão (normalmente o terminal).  
Ele pode receber um ou mais valores e os converte em texto para exibição.

```python
print("Hello World!")
# saída: Hello World!
```

---

## Método `input()`

O método `input()` é usado para ler dados digitados pelo usuário no console.  
Quando chamado, ele exibe uma mensagem opcional (prompt) e espera o usuário digitar algum valor, finalizando com Enter.

> **Importante:** O `input()` sempre retorna uma **string**, mesmo que o usuário digite um número.  
> Para usar como número (inteiro ou decimal), é necessário fazer a conversão manual.

```python
nome = input("Digite seu nome: ")
```

---

## Variáveis e Tipos de Dados

Em Python, variáveis são usadas para armazenar valores e **não precisam ser declaradas com tipo específico**, pois a linguagem é dinamicamente tipada.

### Principais tipos de dados:

- `int`: números inteiros → `idade = 19`
- `float`: números decimais → `altura = 1.87`
- `str`: texto (string) → `nome = "Thiago"`
- `bool`: valores booleanos → `ativo = True`
- `list`, `tuple`, `set`, `dict`: estruturas para armazenar múltiplos valores

```python
nome = "Thiago"                      # str
idade = 19                           # int
altura = 1.87                        # float
ativo = True                         # bool
hobbies = ["musculação", "leitura", "programação"]  # list
```

---

## Desafio Final da Primeira Aula: Cálculo de Bônus

O objetivo do desafio é criar um programa que receba entradas do usuário e calcule um bônus salarial.

### Passos do programa:

1. Solicita ao usuário que digite seu nome, salário mensal e o valor do bônus.
2. Armazena essas informações em variáveis:
   - `nome_usuario`
   - `salario_usuario`
   - `bonus_salarial`
3. Calcula o bônus com a fórmula:

```python
bonus = 1000 + (salario_usuario * bonus_salarial)
```

4. Exibe uma mensagem personalizada com o valor final do bônus usando uma **f-string**.

### 💻 Exemplo de execução:

```
Digite o seu nome: Thiago  
Digite o seu salário: 5000  
Bônus salarial: 0.1  
```

```python
print(f"Olá {nome_usuario}, o seu bônus foi de {bonus}")
```

> Saída: `Olá Thiago, o seu bônus foi de 1500`
