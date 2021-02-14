#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
import sys
import logging
from mymodulefirst import *

# Вариант 12.
# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона; дата рождения (список из трех чисел).
# Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть размещены по алфавиту;
# вывод на экран информации о людях, чьи дни рождения приходятся на месяц, значение которого введено с клавиатуры;
# если таких нет, выдать на дисплей соответствующее сообщение.

# Выполнить индивидуальное задание, добавив возможность работы с исключениями и логгирование.


# class IllegalMarksError(Exception):
#
#     def __init__(self, birthday, message="Illegal year number"):
#         self.birthday = birthday
#         self.message = message
#         super(IllegalMarksError, self).__init__(message)
#
#     def __str__(self):
#         return f"{self.birthday} -> {self.message}"
#
#
# # Класс пользовательского исключения в случае, если введенная
# # команда является недопустимой.
# class UnknownCommandError(Exception):
#
#     def __init__(self, command, message="Неизвестная команда."):
#         self.command = command
#         self.message = message
#         super(UnknownCommandError, self).__init__(message)
#
#     def __str__(self):
#         return f"{self.command} -> {self.message}"
#
#
# @dataclass(frozen=True)
# class People:
#     name: str
#     phone_number: int
#     birthday: list[int]
#
#
# @dataclass
# class Man:
#     soul: List[People] = field(default_factory=lambda: [])
#
#     def add(self, name, phone_number, birthday):
#         self.soul.append(
#             People(
#                 name=name,
#                 phone_number=phone_number,
#                 birthday=birthday
#             )
#         )
#         self.soul.sort(key=lambda people: people.name)
#
#     def __str__(self):
#         # Заголовок таблицы.
#         table = []
#         line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
#             '-' * 4,
#             '-' * 30,
#             '-' * 20,
#             '-' * 8,
#             '-' * 8,
#             '-' * 8,
#             '-' * 8,
#             '-' * 8,
#             '-' * 11
#         )
#         table.append(line)
#         table.append(
#             '| {:^4} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} |'.format(
#                 "No",
#                 "Ф.И.",
#                 "Номер телефона",
#                 "День",
#                 "Месяц",
#                 "Год"
#             )
#         )
#         table.append(line)
#
#         # Вывести данные о всех оценках ученика.
#         for idx, people in enumerate(self.soul, 1):
#             table.append(
#                 '| {:>4} | {:<30} | {:<20} | {:>8} | {:>8} | {:>8} |'.format(
#                     idx,
#                     people.name,
#                     people.phone_number,
#                     people.birthday[0],
#                     people.birthday[1],
#                     people.birthday[2],
#                 )
#             )
#         table.append(line)
#
#         return '\n'.join(table)
#
#     def __repr__(self):
#         return self.__str__()
#
#     def select(self, period):
#         # Проверить сведения людей из списка.
#         parts = command.split(' ', maxsplit=2)
#         period = int(parts[1])
#         result = []
#         count = 0
#         for people in self.soul:
#             if birthday:
#                 if birthday[1] == period:
#                     count += 1
#                     result.append(people)
#         return result


if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='people.log',
        level=logging.INFO
    )
    # Список людей.
    man = Man()

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
                raise UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)
