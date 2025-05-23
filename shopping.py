
shopping_list = {
    "biedronka": ["chleb", "masło", "ser"],
    "lidl": ["mleko", "jajka", "sok"],
    "kaufland": ["ryż", "makaron", "oliwa"]
}

for shop, items in shopping_list.items():
    capitalized_items = [item.capitalize() for item in items]
    print(f"Idę do {shop.capitalize()} i kupuję tam {', '.join(capitalized_items)}.")