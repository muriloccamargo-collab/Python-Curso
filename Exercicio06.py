polegadas = input("Quantas polegadas tem o objeto? ")
rp = float(polegadas.replace(",","."))
cm = rp / 2.54

print(f"Sua medida de {polegadas} polegadas, em centimetros é {cm:.2f}cm")