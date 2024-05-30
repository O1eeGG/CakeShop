import sys
from database import init_db, add_cake, list_cakes, sell_cake, list_sales

def display_menu():
    print("\nУправление продажей тортов")
    print("1. Добавить торт")
    print("2. Показать все торты")
    print("3. Продать торт")
    print("4. Показать историю продаж")
    print("5. Выйти")

def main():
    init_db()
    while True:
        display_menu()
        choice = input("Выберите опцию: ")
        if choice == '1':
            name = input("Введите название торта: ")
            price = float(input("Введите цену торта: "))
            stock = int(input("Введите количество на складе: "))
            add_cake(name, price, stock)
            print("Торт добавлен!")
        elif choice == '2':
            cakes = list_cakes()
            print("\nСписок тортов:")
            for cake in cakes:
                print(f"{cake[0]}. {cake[1]} - {cake[2]} руб. ({cake[3]} шт. на складе)")
        elif choice == '3':
            cake_id = int(input("Введите ID торта для продажи: "))
            quantity = int(input("Введите количество для продажи: "))
            success, total_price = sell_cake(cake_id, quantity)
            if success:
                print(f"Продано на сумму {total_price} руб.")
            else:
                print("Недостаточно товара на складе или неверный ID торта.")
        elif choice == '4':
            sales = list_sales()
            print("\nИстория продаж:")
            for sale in sales:
                print(f"ID продажи: {sale[0]}, Торт: {sale[1]}, Количество: {sale[2]}, Общая стоимость: {sale[3]} руб., Дата: {sale[4]}")
        elif choice == '5':
            print("Выход из программы.")
            sys.exit()
        else:
            print("Неверный выбор, попробуйте еще раз.")

if __name__ == '__main__':
    main()
