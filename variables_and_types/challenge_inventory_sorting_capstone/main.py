# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"
catergory1=categories[0:10]
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
candy1 = items[0:9]
candy2 = items[11:20]
dry_goods=items[22:]
print(f"{items},{categories},{bubblegum_price},{chocolate_price},{pasta_price}")
print(f"We have {candy1} for {bubblegum_price} in the {categories}")
print(f"We have {candy2} for {chocolate_price} in the {categories}")
print(f"We have {dry_goods} for {pasta_price} in the {categories}")
print(f"we have pasta for {pasta_price} in the pasta aisle")