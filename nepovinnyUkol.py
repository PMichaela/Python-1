celeJmeno = str(input("Zadejte prosím jméno a příjmení: "))
jmeno, prijmeni = celeJmeno.split(" ") # split rozděluje podle toho co je v uvozovkách v závorce za ním
inicialy = jmeno[0] + ". " + prijmeni[0] + "."
zkraceneJmeno = jmeno[0] + ". " + prijmeni.title()

print(celeJmeno.upper()) # Všechno velkými písmeny
print(celeJmeno.lower()) # Všechno malými písmeny
print(celeJmeno.title()) # První písmeno velké, zbytek malé
print(f"{inicialy}") 

# Křestní jméno zkrácené na první písmeno a příjmení, pokud je křestní jméno delší než 5 znaků. 
# Jinak vypíše standardní variantu, tj. první písmeno velké, další malá

if len(jmeno) > 5: # funkce len zjišťuje délku stringu - str
    print(f"{zkraceneJmeno}")
else:
    print(f"{celeJmeno.title()}")

