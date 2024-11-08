def show_menu():
    print("Выберите задачу:")
    print("1. Задание 1")
    print("2. Задание 2")
    print("3. Задание 3")
    print("q. Выход")

def select_task():
    while True:
        show_menu()
        choice = input("Введите номер задачи (или 'q' для выхода): ")
        
        if choice == '1':
            print("Вы выбрали Задание 1")
        elif choice == '2':
            print("Вы выбрали Задание 2")
        elif choice == '3':
            print("Вы выбрали Задание 3")
        elif choice == 'q':
            print("Выход из программы...")
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    select_task()
    