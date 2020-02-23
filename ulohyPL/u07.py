# === Úloha 7===
# Napíšte program, ktorý vymení v postupnosti náhodne vygenerovaných reálnych čísel najmenšie a najväčšie číslo.

from random import randint

l = [ randint(0, 5) for i in range(5) ]
l_max = max(l)
l_min = min(l)

print(f"predtym: {l}")

for i in range(len(l)):
  if l[i] == l_max:
    l[i] = l_min
  elif l[i] == l_min:
    l[i] = l_max

print(f"potom: {l}")