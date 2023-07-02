class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability

    def __str__(self):
        return f"ID: {self.snack_id}, Name: {self.name}, Price: {self.price}, Availability: {self.availability}"


class Canteen:
    def __init__(self):
        self.snacks = []
        self.sales_records = []

    def add_snack(self, snack):
        self.snacks.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                self.snacks.remove(snack)
                break

    def update_snack_availability(self, snack_id, availability):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                snack.availability = availability
                break

    def sell_snack(self, snack_id):
        for snack in self.snacks:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    self.sales_records.append(snack)
                    print(f"Snack '{snack.name}' sold successfully.")
                else:
                    print(f"Snack '{snack.name}' is not available.")
                break
        else:
            print("Snack not found.")

    def display_snacks(self):
        for snack in self.snacks:
            print(snack)

    def display_sales_records(self):
        for snack in self.sales_records:
            print(snack)


def display_menu():
    print("===== Canteen Inventory Management =====")
    print("1. Add Snack")
    print("2. Remove Snack")
    print("3. Update Snack Availability")
    print("4. Sell Snack")
    print("5. Display Snacks")
    print("6. Display Sales Records")
    print("0. Exit")


def get_menu_choice():
    while True:
        choice = input("Enter your choice (0-6): ")
        if choice.isdigit() and 0 <= int(choice) <= 6:
            return int(choice)
        print("Invalid input. Please try again.")


def add_snack(canteen):
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = input("Enter snack price: ")
    availability = input("Enter snack availability (yes/no): ")
    snack = Snack(snack_id, name, price, availability)
    canteen.add_snack(snack)
    print("Snack added successfully.")


def remove_snack(canteen):
    snack_id = input("Enter snack ID to remove: ")
    canteen.remove_snack(snack_id)
    print("Snack removed successfully.")


def update_snack_availability(canteen):
    snack_id = input("Enter snack ID to update availability: ")
    availability = input("Enter new availability (yes/no): ")
    canteen.update_snack_availability(snack_id, availability)
    print("Snack availability updated successfully.")


def sell_snack(canteen):
    snack_id = input("Enter snack ID to sell: ")
    canteen.sell_snack(snack_id)


def main():
    canteen = Canteen()

    while True:
        display_menu()
        choice = get_menu_choice()

        if choice == 0:
            print("Exiting the program.")
            break
        elif choice == 1:
            add_snack(canteen)
        elif choice == 2:
            remove_snack(canteen)
        elif choice == 3:
            update_snack_availability(canteen)
        elif choice == 4:
            sell_snack(canteen)
        elif choice == 5:
            canteen.display_snacks()
        elif choice == 6:
            canteen.display_sales_records()
        print()

if __name__ == "__main__":
    main()