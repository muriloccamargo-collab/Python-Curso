# Variaveis - armazena, os dados temporariamente
# na memória do computador

# Variávei = valor(números, texto ou booleanos true/false)

# Entrada
# nome = input("Qual é o seu nome?")
# sobrenome = input("Qual é o seu sobrenome?")


n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

# Processamento
if(input("Quer somar? (n/y)") == "y"):
    R = n1 + n2
    # Saida
    print(f"O resultado é: {R}")
    exit()
    
if(input("Quer subtrair? (n/y)") == "y"):
    R = n1 - n2
    # Saida
    print(f"O resultado é: {R}")
    exit()

if(input("Quer dividir? (n/y)") == "y"):
    if( n1 < n2):
        R = n1 / n2
        # Saida
        print(f"O resultado é: {R}")
        exit()

if(input("Quer multiplicar? (n/y)") == "y"):
    R = n1 * n2
    # Saida
    print(f"O resultado é: {R}")
    exit()


