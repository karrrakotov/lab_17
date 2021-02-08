#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys

# Вариант 12.
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона; дата рождения (список из трех чисел).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту;
# вывод на экран информации о людях, чьи дни рождения приходятся на месяц, значение которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение.

if __name__ == '__main__':
    # Список людей.
    people = []
    # Организовать бесконечный цикл запроса команд.
    while True:
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

            if birthday[0] < 1 or birthday[0] > 31:
                print("Такого дня не существует!", file=sys.stderr)
                exit(1)

            if birthday[1] < 1 or birthday[1] > 12:
                print("Такого месяца не существует!", file=sys.stderr)
                exit(1)

            today = date.today()
            if birthday[2] > today.year:
                print(f"{birthday[2]} год ещё не наступил!", file=sys.stderr)
                exit(1)

            # Создать словарь.
            human = {
                'name': name,
                'phone_number': phone_number,
                'birthday': birthday,
            }

            # Добавить словарь в список.
            people.append(human)

            # Отсортировать список в случае необходимости.
            if len(people) > 1:
                people.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 8,
                '-' * 8,
                '-' * 8
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} |'.format(
                    "No",
                    "Ф.И.",
                    "Номер телефона",
                    "День",
                    "Месяц",
                    "Год"
                )
            )
            print(line)
            # Вывести данные о всех людях.
            for idx, human in enumerate(people, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>8} | {:>8} | {:>8} |'.format(
                        idx,
                        human.get('name', ''),
                        human.get('phone_number', ''),
                        human.get('birthday[0]', f'{birthday[0]}'),
                        human.get('birthday[1]', f'{birthday[1]}'),
                        human.get('birthday[2]', f'{birthday[2]}'),
                    )
                )
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)
            # Получить требуемый месяц.
            period = int(parts[1])
            # Инициализировать счетчик.
            count = 0
            # Проверить сведения людей из списка.
            for human in people:
                if birthday[1] == period:
                    count += 1
                    print(f'{count}. Имя: {human.get("name", "")}, Телефон: {human.get("phone_number", "")}, '
                          f'Дата рождения: {human.get("birthday", "")}')

            # Если счетчик равен 0, то нужные люди не найдены.
            if count == 0:
                print("Люди, родившиеся в данном месяце не найдены.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список всех людей;")
            print("select <Месяц рождения> - запросить данные о людях с введенным месяцем рождения;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
