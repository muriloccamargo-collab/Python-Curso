polegadas = input("Quantas polegadas tem o objeto? ")
rp = float(polegadas.replace(",","."))
cm = rp / 2.54

print(f"Sua medida de {polegadas:.2f} polegadas, em centimetros é {cm:.2f}cm")