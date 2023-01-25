soucastka = input("Zadejte číslo součástky prosím: ")

sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

if soucastka in sklad:
    mnozstvi = int(input("Zadejte požadované množství: "))
    if sklad[soucastka] <= mnozstvi:
        print(f'K prodeji je pouze {sklad[soucastka]} kusů.')
        sklad.pop(soucastka)
    elif sklad[soucastka] > mnozstvi:
        print("Vaše objednávka se vyřizuje.")
        sklad[soucastka] -= mnozstvi
else:
    print("Součástka není skladem.")

print(sklad.items())
