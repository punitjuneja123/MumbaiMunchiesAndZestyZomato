class Dish:
    def __init__(self, dish_id, dish_name, price, availability):
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.price = price
        self.availability = availability

class ZomatoChronicles:
    def __init__(self):
        self.menu = []
        self.orders = {}
        self.next_order_id = 1

    def add_dish(self, dish_id, dish_name, price, availability):
        dish = Dish(dish_id, dish_name, price, availability)
        self.menu.append(dish)
        print(f"Added dish: {dish.dish_name}")

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                self.menu.remove(dish)
                print(f"Removed dish: {dish.dish_name}")
                break
        else:
            print("Dish not found!")

    def update_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                dish.availability = availability
                print(f"Updated availability for dish: {dish.dish_name}")
                break
        else:
            print("Dish not found!")

    def take_order(self, customer_name, dish_ids):
        order_items = []
        for dish_id in dish_ids:
            dish = self.find_dish(dish_id)
            if dish and dish.availability == 'yes':
                order_items.append(dish)
            else:
                print(f"Invalid dish ID or dish not available: {dish_id}")
        if order_items:
            order_id = self.next_order_id
            self.next_order_id += 1
            order = {
                'order_id': order_id,
                'customer_name': customer_name,
                'order_items': order_items,
                'status': 'received'
            }
            self.orders[order_id] = order
            print(f"Order placed successfully. Order ID: {order_id}")
        else:
            print("Order cannot be processed.")

    def update_order_status(self, order_id, status):
        order = self.orders.get(order_id)
        if order:
            order['status'] = status
            print(f"Updated order status. Order ID: {order_id}, Status: {status}")
        else:
            print("Order not found!")

    def review_orders(self):
        for order_id, order in self.orders.items():
            print(f"Order ID: {order_id}, Customer: {order['customer_name']}, Status: {order['status']}")

    def find_dish(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                return dish
        return None

    def display_menu(self):
        print("\nWelcome to Zomato Chronicles: The Great Food Fiasco!")
        print("1. Add a dish to the menu")
        print("2. Remove a dish from the menu")
        print("3. Update dish availability")
        print("4. Take a new order")
        print("5. Update order status")
        print("6. Review all orders")
        print("7. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")
            print()

            if choice == '1':
                dish_id = int(input("Enter the dish ID: "))
                dish_name = input("Enter the dish name: ")
                price = float(input("Enter the dish price: "))
                availability = input("Is the dish available? (yes/no): ")
                self.add_dish(dish_id, dish_name, price, availability)

            elif choice == '2':
                dish_id = int(input("Enter the dish ID to remove: "))
                self.remove_dish(dish_id)

            elif choice == '3':
                dish_id = int(input("Enter the dish ID to update availability: "))
                availability = input("Enter the new availability (yes/no): ")
                self.update_availability(dish_id, availability)

            elif choice == '4':
                customer_name = input("Enter customer name: ")
                dish_ids = input("Enter dish IDs (comma-separated): ").split(',')
                dish_ids = [int(dish_id.strip()) for dish_id in dish_ids]
                self.take_order(customer_name, dish_ids)

            elif choice == '5':
                order_id = int(input("Enter order ID to update status: "))
                status = input("Enter the new status: ")
                self.update_order_status(order_id, status)

            elif choice == '6':
                self.review_orders()

            elif choice == '7':
                print("Thank you for using Zomato Chronicles. Have a great day!")
                break

            else:
                print("Invalid choice. Please try again.")

# Run the application
zomato = ZomatoChronicles()
zomato.run()
