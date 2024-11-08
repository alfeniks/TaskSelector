# Запрашиваем у пользователя силу и ускорение
force = float(input("Введите силу в ньютонах: "))
acceleration = float(input("Введите ускорение в метрах на секунду в квадрате: "))

# Проверяем, что ускорение не равно нулю, чтобы избежать деления на ноль
if acceleration != 0:
    # Рассчитываем массу
    mass = force / acceleration
    print(f"Масса: {mass} кг")
else:
    print("Ошибка: ускорение не может быть равно нулю.")