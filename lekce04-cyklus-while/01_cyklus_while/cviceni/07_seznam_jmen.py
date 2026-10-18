# Cvičení 7 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se "Jméno: " a každé jméno vypiš. Když uživatel nic nenapíše
#    a jen zmáčkne Enter, přeskoč výpis příkazem continue.
#    Cyklus ukonči, když uživatel napíše "konec".
#    (Prázdná odpověď z inputu je prázdný text: "")


while True:
    word = input ("Jmeno:")
    print(word)
    if word == "":
        continue
    if word == "konec":
        break   
print("thats it")    