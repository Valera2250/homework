class Product:
    def __init__(self, name, price, description, dimensions):
        self.name = name
        self.price = price
        self.description = description
        self.dimensions = dimensions

    def __str__(self):
        return f"{self.name} (Цена: {self.price} руб., Описание: {self.description}, Размеры: {self.dimensions})"


class Customer:
    def __init__(self, first_name, last_name, middle_name, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.phone = phone

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name}, Телефон: {self.phone}"


class Order:
    def __init__(self, customer):
        self.customer = customer
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def calculate_total(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def __str__(self):
        products_info = "\n".join(
            [f"{product.name} x{quantity} - {product.price * quantity} руб." for product, quantity in self.items]
        )
        total_cost = self.calculate_total()
        return (
            f"Заказ для {self.customer}\n" +
            f"Товары:\n{products_info}\n" +
            f"Итого: {total_cost} руб."
        )



product1 = Product("Ноутбук", 50000, "Игровой ноутбук", "35x25x2 см")
product2 = Product("Мышь", 1500, "Беспроводная мышь", "10x5x3 см")
product3 = Product("Клавиатура", 3000, "Механическая клавиатура", "45x15x3 см")


customer = Customer("Иван", "Иванов", "Иванович", "+79161234567")


order = Order(customer)
order.add_product(product1, 1)
order.add_product(product2, 2)
order.add_product(product3, 1)


print(order)
