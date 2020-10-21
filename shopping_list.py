shop_list = {
    'meblowy':['kanapa', 'stoł', 'krzesło'],
    'mięsny':['jagnięcina', 'krakowska sucha', 'skrzydełka'],
    'kiosk':['gazeta', 'baterie', 'zapałki']
}
for item in shop_list:
    print(f"Idę do {item.capitalize()} i kupuję {', '.join([c.capitalize() for c in shop_list[item]])}.")