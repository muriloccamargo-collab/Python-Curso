cm = input("Quantos cm tem o objeto? ")
rcm = float(cm.replace(",","."))
polegada = rcm * 2.54

print(f"Sua medida de {cm:.2f}cm, em polegadas é {polegada:.2f} polegadas")