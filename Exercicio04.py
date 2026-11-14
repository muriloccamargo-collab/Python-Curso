import time

nome = input("Qual o seu nome? ")
peso = input("Qual o seu peso, em kilos(kg)? ")
rp = float(peso.replace(",","."))
altura = input("Qual a sua altura, em metros? ")
ra = float(altura.replace(",","."))

imc = rp / (ra*ra)

print(f"Senhor {nome} você está com o IMC de {imc:.2f}")
if(imc < 18.5):
    print("Está com o peso baixo até demais")
    exit()

if(imc < 24.9):
    print("Está com o peso normal")
    exit()

if(imc < 29.9):
    print("Está com sobrepeso")
    exit()

if(imc < 34.9):
    print("Está com Obesidade grau I")
    exit()

if(imc < 39.9):
    print("Está com Obesidade grau II")
    exit()

if(imc < 100):
    print("Está com Obesidade grau III")
    exit()


if(imc > 100):
    print(".")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Como você atingui esse estádio?")
    time.sleep(2)
    print("Mogo!?")   
