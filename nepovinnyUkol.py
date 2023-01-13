celeJmeno = str(input("Zadejte prosím jméno a příjmení: "))
jmeno, prijmeni = celeJmeno.split(" ") # split rozděluje podle toho co je v uvozovkách v závorce za ním
inicialy = jmeno[0] + ". " + prijmeni[0] + "."
zkraceneJmeno = jmeno[0] + ". " + prijmeni.title()

print(celeJmeno.upper())
print(celeJmeno.lower())
print(celeJmeno.title())
print(f"{inicialy}")

if len(jmeno) > 5: # funkce len zjišťuje délku stringu - str
    print(f"{zkraceneJmeno}")

if len(jmeno) < 5:
    print(f"{celeJmeno.title()}")
