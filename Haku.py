#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
import logging

# Вариант 12.
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона; дата рождения (список из трех чисел).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту;
# вывод на экран информации о людях, чьи дни рождения приходятся на месяц, значение которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение.

# Выполнить индивидуальное задание, добавив возможность работы с исключениями и логгирование.


class IllegalMarksError(Exception):

    def __init__(self, birthday, message="Illegal year number"):
        self.birthday = birthday
        self.message = message
        super(IllegalMarksError, self).__init__(message)

    def __str__(self):
        return f"{self.birthday} -> {self.message}"


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):

    def __init__(self, command, message="Неизвестная команда."):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='people.log',
        level=logging.INFO
    )
    # Список людей.
    people = []
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
                logging.info("Отображен список людей.")
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
                    if birthday:
                        if birthday[1] == period:
                            count += 1
                            print(f'{count}. Имя: {human.get("name", "")}, Телефон: {human.get("phone_number", "")}, '
                                  f'Дата рождения: {human.get("birthday", "")}')
                            logging.info(
                                f"Найдено {len(parts[1])} людей с "
                                f"введенным месяцем рождения {birthday[1]}."
                            )

                # Если счетчик равен 0, то нужные люди не найдены.
                if count == 0:
                    print("Люди, родившиеся в данном месяце не найдены.")
                    logging.warning(
                        f"Люди родившиеся в {birthday[1]} месяце не найдены."
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
                raise UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
