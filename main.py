class Store:
    def __init__(self, name: str, address: str, items=None):
        self.name = name
        self.address = address
        self.items = items if items is not None else {}

    def add_good(self, good: str, price: float):
        self.items[good] = price
        print(f"Товар '{good}' добавлен с ценой {price} за кг.")

    def delete_good(self, good: str):
        if good in self.items:
            del self.items[good]
            print(f"Товар '{good}' удален из ассортимента.")
        else:
            print(f"Товар '{good}' не найден в ассортименте.")

    def get_price(self, good: str):
        return self.items.get(good)

    def update_price(self, good: str, new_price: float):
        if good in self.items:
            old_price = self.items[good]
            self.items[good] = new_price
            print(f"Цена товара '{good}' обновлена с {old_price} на {new_price} за кг.")
        else:
            print(f"Товар '{good}' не найден в ассортименте.")

    def __str__(self):
        items_str = ', '.join([f"{k}: {v}" for k, v in self.items.items()])
        return f"Магазин '{self.name}' по адресу '{self.address}' имеет следующие товары: {items_str}"

# Создаем магазины
my_store = Store("Фруктовый магаз", "ул. Пушкина, д. 1")
my_store_2 = Store("Хлебный магаз", "ул. Лермонтова, д. 2")
my_store_3 = Store("Овощной магаз", "ул. Маяковского, д. 3")
my_store_4 = Store("Барахолка", "ул. Толстого, д. 4")

# Добавляем товары
my_store.add_good("яблоки", 100.5)
my_store.add_good("бананы", 220.75)
my_store_2.add_good("булка", 20.10)
my_store_3.add_good("перец", 300.70)
my_store_3.add_good("тыква", 1050.10)
my_store_4.add_good("носки", 50.40)
my_store_4.add_good("шнурки", 60.90)

# Получаем цену товара
price = my_store.get_price("яблоки")
price_2 = my_store_2.get_price("булка")
price_3 = my_store_3.get_price("тыква")
price_4 = my_store_4.get_price("носки")
print(f"Цена яблок: {price}")
print(f"Цена булки: {price_2}")
print(f"Цена тыквы: {price_3}")
print(f"Цена носков: {price_4}")


# Обновляем цену товара
my_store.update_price("бананы", 230.80)
my_store_4.update_price("шнурки", 70.80)

# Удаляем товар
my_store.delete_good("яблоки")
my_store_3.delete_good("тыква")

# Выводим информацию о магазине
print(my_store)
print(my_store_2)
print(my_store_3)
print(my_store_4)


