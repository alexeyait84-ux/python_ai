name = "Анна"
item = "тетрадь"
unit_price = 60
quantity = 4
delivery = 100
discount = 50
budget = 500

print("Заказ: ", name)
print("Товар: ", item)
print("Количество: ", quantity)
print("Стоимость товаров: ", unit_price*quantity)
print("Доставка: ", delivery)
print("Скидка: ", discount)
summary = ((unit_price * quantity) - discount) + delivery
print("Итого: ", summary)
print("Остаток бюджета: ", budget - summary)