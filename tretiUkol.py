import json

with open('tretiUkol/body.json', encoding='utf-8') as rating:
    body = json.load(rating)
print(body)

benefit = {}
for name in body:
    if body[name] >= 60:
       benefit[name] = "Pass"
    else:
        benefit[name] = "Fail"

with open('prospech.json', mode='w', encoding='utf-8') as file:
    json.dump(benefit, file, ensure_ascii=False, indent=4)