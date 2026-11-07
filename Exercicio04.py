nome = input("Qual o seu nome? ")
peso = input("Qual o seu peso, em kilos(kg)? ")
rp = float(peso.replace(",","."))
altura = input("Qual a sua altura, em metros? ")
ra = float(altura.replace(",","."))

imc = rp / (ra*ra)

print(f"Senhor {nome} você está com o IMC de {imc:.2f}")