#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
import logging
import mymodulefirst


# Вариант 12.
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона; дата рождения (список из трех чисел).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту;
# вывод на экран информации о людях, чьи дни рождения приходятся на месяц, значение которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение.

# Выполнить индивидуальное задание, добавив возможность работы с исключениями и логгирование.


if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='people.log',
        level=logging.INFO
    )
    # Список людей.
    man = mymodulefirst.Man()

    # Организовать бесконечный цикл запроса команд.
    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                # Запросить данные о человеке.
                name = input("Введите имя и фамилию: ")
                phone_number = int(input("Введите номер телефона: "))
                birthday = list(map(int, input("Введите дату рождения в формате - дд.мм.гггг: ").split(".")))

                # Добавить данные о людях.
                logging.info(
                    f"Добавлен человек: Имя: {name}, Телефон: {phone_number}, "
                    f"родившийся в {birthday[1]} месяце, Дата рождения: {birthday} "
                )

                if birthday[0] < 1 or birthday[0] > 31:
                    print("Такого дня не существует!", file=sys.stderr)
                    logging.warning(
                        f"{birthday[0]} дня не существует!"
                    )
                    exit(1)

                if birthday[1] < 1 or birthday[1] > 12:
                    print("Такого месяца не существует!", file=sys.stderr)
                    logging.warning(
                        f"{birthday[1]} месяца не существует!"
                    )
                    exit(1)

                today = date.today()
                if birthday[2] > today.year:
                    print(f"{birthday[2]} год ещё не наступил!", file=sys.stderr)
                    logging.warning(
                        f"{birthday[2]} год ещё не наступил!"
                    )
                    exit(1)
                # Добавить словарь в список.
                man.add(name, phone_number, birthday)

            elif command == 'list':
                # Вывести список.
                print(man)
                logging.info("Отображен список людей.")

            elif command.startswith('select '):
                parts = command.split(' ', maxsplit=2)
                period = int(parts[1])
                # Получить требуемый месяц.
                selected = man.select(period)
                # Инициализировать счетчик.
                count = 0
                # Проверить сведения людей из списка.
                if selected:
                    for count, people in enumerate(selected, 1):
                        print(f'{count}. Имя: {people.name}, Телефон: {people.phone_number}, '
                              f'Дата рождения: {people.birthday}')
                    logging.info(
                        f"Найдено {len(selected)} людей с "
                        f"введенным месяцем рождения {parts[1]}."
                    )
                # Если счетчик равен 0, то нужные люди не найдены.
                else:
                    print("Люди, родившиеся в данном месяце не найдены.")
                    logging.warning(
                        f"Люди родившиеся в {parts[1]} месяце не найдены."
                    )

            elif command == 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить человека;")
                print("list - вывести список всех людей;")
                print("select <Месяц рождения> - запросить данные о людях с введенным месяцем рождения;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            else:
                raise mymodulefirst.UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
