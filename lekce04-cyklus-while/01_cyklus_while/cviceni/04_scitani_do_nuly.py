# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.

soucet = 0
cislo = int(input("Jake tvoje cislo?"))
while cislo != 0:
    if cislo < 0:
        print("zaporne cisla nepocitame")
    else:
        soucet = soucet + cislo
    cislo = int(input("Jake tvoje cislo?"))
print("Soucet =", soucet)
