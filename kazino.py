def casino_age_verification():
    print("=== ДОБРО ПОЖАЛОВАТЬ В КАЗИНО 'НЕ ОБМАН' ===")
    print("Для доступа к игре необходимо подтвердить возраст")
    try:
        age = int(input("Пожалуйста, введите ваш возраст: "))
        if age < 0:
            print("Ошибка: Возраст не может быть отрицательным!")
        elif age < 18:
            print("Доступ запрещён!")
            print("Извините, вы слишком молоды для доступа.")
            print("Возвращайтесь, когда вырастете")
        elif age > 100:
            print("Обнаружена плесень")
            print("Рекомендуем посетить сайт https://pensia.rf")
            print("Доступ ограничен")
        elif age == 18:
            print("Поздравляем с совершеннолетием!")
            print("Доступ разрешён. Добро пожаловать: https://nenaeb.com !")
        elif 19 <= age <= 25:
            print("Доступ разрешён")
            print("Добро пожаловать: https://nenaeb.com !")
        else:
            print("Доступ разрешён")
            print("Добро пожаловать: https://nenaeb.com !")
    except ValueError:
        print("Ошибка. Пожалуйста введите корректный возраст!")
def main():
    while True:
        casino_age_verification()
        print("\n" + "="*50)
        repeat = input("Хотите проверить другой возраст? (да/нет: ").lower()
        if repeat not in ['да','yes','y','д']:
            print("Спасибо за игру! До свидания!")
            break
        print()
        break





