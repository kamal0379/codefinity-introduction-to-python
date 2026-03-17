vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
if "carrots" not in vegetables:
        vegetables.append("carrots")
elif "carrots" in vegetables:
        print("Carrots are already in the list.")
else:
    print(f"Updated Vegetable Inventory: {vegetables}")
if "cucumbers" not in vegetables:   
      vegetables.append("cucumbers")
elif "cucumbers" in vegetables:
        print("cucumbers are already in the list.")
else:
        print(f"Updated Vegetable Inventory: {vegetables}")
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)


