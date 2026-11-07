nome = input("Qual o seu nome? ")
cargo = input("Qual o seu cargo? ")
salário = input("Qual o seu salário? ")
n = float(salário.replace(",","."))
ns = n * 1.10

print(f"Senho {nome}, com o cargo de {cargo}, seu salario de R${salário} teve um aumento de 10%, estando agora com um salário de R${ns:.2f}")