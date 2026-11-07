anoNascimento = int(input("Qual a sua idade de nascimento? "))
anoAtual = int(input("Qual é o ano atual? "))
idade = anoAtual - anoNascimento
idadeSemana = ((idade * 12 ) * 4.34524)

print(f"Idade: {idade}")
print(f"Semanas: {idadeSemana:.2f}")