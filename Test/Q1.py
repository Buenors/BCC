seg = int(input()) 
min = int(seg/60)
hora = int(min/60)
seg = seg%60
min = min%60
print(f"{hora:02}:{min:02}:{seg:02}")