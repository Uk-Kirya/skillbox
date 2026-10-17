greeting_text = (
    "Приложение MyProfile\n"
    "Сохраняй информацию о себе и выводи ее в разных форматах"
)


def separator_gen() -> str:
    """Создает разделитель."""
    return "-" * 42


def main_menu() -> int:
    """Выводит главное меню."""
    title = "\nГлавное меню\n"
    point_1 = "1 - Ввести или обновить информацию\n"
    point_2 = "2 - Вывести информацию\n"
    point_0 = "0 - Завершить работу\n"
    action = "Введите номер пункта меню: "

    return int(input(
        separator_gen() + title.upper() + point_1 + point_2 + point_0 + action
    ))


def input_information() -> int:
    """Выводит меню ввода информации."""
    title = "\nВвести или обновить информацию\n"
    point_1 = "1 - Личная информация\n"
    point_2 = "2 - Информация о предпринимателе\n"
    point_0 = "0 - Назад\n"
    action = "Введите номер пункта меню: "

    return int(input(
        separator_gen() + title.upper() + point_1 + point_2 + point_0 + action
    ))


def output_information() -> int:
    """Выводит меню отображения информации."""
    title = "\nВывести информацию\n"
    point_1 = "1 - Личная информация\n"
    point_2 = "2 - Вся информация\n"
    point_0 = "0 - Назад\n"
    action = "Введите номер пункта меню: "

    return int(input(
        separator_gen() + title.upper() + point_1 + point_2 + point_0 + action
    ))


def input_age() -> int:
    """Запрашивает неотрицательный возраст."""
    while True:
        age = int(input("Возраст: "))

        if age >= 0:
            return age

        print("Возраст не может быть отрицательным. Повторите ввод.")


def input_ogrnip() -> int:
    """Запрашивает ОГРНИП из 15 цифр."""
    while True:
        ogrnip = int(input("ОГРНИП: "))

        if len(str(ogrnip)) == 15:
            return ogrnip

        print("ОГРНИП должен содержать 15 цифр. Повторите ввод.")


def input_account() -> int:
    """Запрашивает расчетный счет из 20 цифр."""
    while True:
        account = int(input("Расчётный счёт: "))

        if len(str(account)) == 20:
            return account

        print("Расчётный счёт должен содержать 20 цифр. Повторите ввод.")


def input_personal_data() -> None:
    """Вводит или обновляет личную информацию."""
    print("\n" + separator_gen())
    print("ЛИЧНАЯ ИНФОРМАЦИЯ")
    print(separator_gen())

    personal_data["Имя"] = input("Имя: ")
    personal_data["Возраст"] = input_age()
    personal_data["Телефон"] = input("Телефон: ")
    personal_data["Электронная почта"] = input("Электронная почта: ")

    postal_index = input("Индекс: ")
    personal_data["Индекс"] = "".join(
        symbol for symbol in postal_index if symbol.isdigit()
    )

    personal_data["Почтовый адрес"] = input("Почтовый адрес: ")
    personal_data["Дополнительная информация"] = input(
        "Дополнительная информация: "
    )

    print("\nЛичная информация сохранена.")


def input_business_data() -> None:
    """Вводит или обновляет информацию о предпринимателе."""
    print("\n" + separator_gen())
    print("ИНФОРМАЦИЯ О ПРЕДПРИНИМАТЕЛЕ")
    print(separator_gen())

    business_data["ОГРНИП"] = input_ogrnip()
    business_data["ИНН"] = int(input("ИНН: "))
    business_data["Расчётный счёт"] = input_account()
    business_data["Название банка"] = input("Название банка: ")
    business_data["БИК"] = int(input("БИК: "))
    business_data["Корреспондентский счёт"] = int(input("Корреспондентский счёт: "))

    print("\nИнформация о предпринимателе сохранена.")


def print_data(data: dict) -> None:
    """Выводит сохраненную информацию."""
    for field, value in data.items():
        print(f"{field}: {value}")


def show_personal_data() -> None:
    """Выводит личную информацию."""
    print("\n" + separator_gen())
    print("ЛИЧНАЯ ИНФОРМАЦИЯ")
    print(separator_gen())

    print_data(personal_data)


def show_all_data() -> None:
    """Выводит всю сохраненную информацию."""
    print("\n" + separator_gen())
    print("ВСЯ ИНФОРМАЦИЯ")
    print(separator_gen())

    print_data(personal_data)
    print_data(business_data)


def input_menu_handler() -> None:
    """Обрабатывает меню ввода информации."""
    while True:
        try:
            action = input_information()
        except ValueError:
            print("Введён некорректный пункт меню.")
            continue

        if action == 1:
            input_personal_data()
        elif action == 2:
            input_business_data()
        elif action == 0:
            break
        else:
            print("Введён некорректный пункт меню.")


def output_menu_handler() -> None:
    """Обрабатывает меню вывода информации."""
    while True:
        try:
            action = output_information()
        except ValueError:
            print("Введён некорректный пункт меню.")
            continue

        if action == 1:
            show_personal_data()
        elif action == 2:
            show_all_data()
        elif action == 0:
            break
        else:
            print("Введён некорректный пункт меню.")


def main() -> None:
    """Запускает приложение MyProfile."""
    print(greeting_text)

    while True:
        try:
            action = main_menu()
        except ValueError:
            print("Введён некорректный пункт меню.")
            continue

        if action == 1:
            input_menu_handler()
        elif action == 2:
            output_menu_handler()
        elif action == 0:
            print("Работа приложения завершена.")
            break
        else:
            print("Введён некорректный пункт меню.")


personal_data = {
    "Имя": "",
    "Возраст": "",
    "Телефон": "",
    "Электронная почта": "",
    "Индекс": "",
    "Почтовый адрес": "",
    "Дополнительная информация": "",
}

business_data = {
    "ОГРНИП": "",
    "ИНН": "",
    "Расчётный счёт": "",
    "Название банка": "",
    "БИК": "",
    "Корреспондентский счёт": "",
}


if __name__ == "__main__":
    main()
