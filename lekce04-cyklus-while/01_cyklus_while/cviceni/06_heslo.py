# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.


tries = 0
tries_left = 3
while True:
    heslo = input("Password:")
    tries = tries + 1
    tries_left -= 1
    if heslo == "pyladies":
        print("Hi!")
        break
    if tries == 3:
        print("Blocked")
        break
    print("u have " + str(tries_left) + " more attempts")

