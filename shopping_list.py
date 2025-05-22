

shopping={
    "biedronka":["mleko","chleb","masło"],
    "lidl":["jajka","ser","szynka"],
    "kaufland":["cola","chipsy","ciastka"]
}

total_items=0

for sklep, produkty in shopping.items():
    sklep_cap = sklep.capitalize()
    produkty_cap = [produkt.capitalize() for produkt in produkty]
    print(f"Idę do {sklep_cap} i kupuję tam {", ".join(produkty_cap)}.")
    
    total_items += len(produkty)
print(f"W sumie kupuję {total_items} produktów.")





