shop_list = {
    'meblowy':['kanapa', 'stoł', 'krzesło'],
    'mięsny':['jagnięcina', 'kabanosy', 'skrzydełka'],
    'kiosk':['gazeta', 'baterie', 'zapałki']
}
for item in shop_list:
    print(f"Idę do {item.capitalize()} i kupuję {', '.join([c.capitalize() for c in shop_list[item]])}.")
print(f"W sumie kupuję {sum([len(value) for value in shop_list.values()])} produktów.")
