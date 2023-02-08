# Jednoduchá aplikaci pro zasílání SMS zpráv.
PHONE_NUMBER = input("Zadejte telefonní číslo, kam chceš zprávu poslat: ")

def number_validate(YOUR_NUMBER):
    if len(PHONE_NUMBER) == 9:
        return True
    elif len(PHONE_NUMBER) == 13 and PHONE_NUMBER[0:4] == "+420":
        return True
    else:
        return False
print(number_validate(PHONE_NUMBER))

def price_message(message):
    cost = 3 * (len(message) // 180 + 1)
    return cost

if number_validate(PHONE_NUMBER):
  message = input("Zadejte zprávu: ")
  cost = price_message(message)
  print(f"Cena za SMS je {cost} Kč.")
else:
  print("Chybné telefonní číslo!")
