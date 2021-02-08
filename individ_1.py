#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from dataclasses import dataclass, field
import logging
import sys
from typing import List
import xml.etree.ElementTree as ET

#   Выполнить индивидуальное задание 2 лабораторной работы 13, добавив возможность работы с
#   исключениями и логгирование.


class IllegalMarksError(Exception):

    def __init__(self, marks, message="Illegal year number"):
        self.marks = marks
        self.message = message
        super(IllegalMarksError, self).__init__(message)

    def __str__(self):
        return f"{self.marks} -> {self.message}"


# Класс пользовательского исключения в случае, если введенная
# команда является недопустимой.
class UnknownCommandError(Exception):

    def __init__(self, command, message="Unknown command"):
        self.command = command
        self.message = message
        super(UnknownCommandError, self).__init__(message)

    def __str__(self):
        return f"{self.command} -> {self.message}"


@dataclass(frozen=True)
class Person:
    name: str
    group: str
    marks: list[int]


@dataclass
class Staff:
    students: List[Person] = field(default_factory=lambda: [])

    def add(self, name, group, marks):
        self.students.append(
            Person(
                name=name,
                group=group,
                marks=marks
            )
        )
        self.students.sort(key=lambda person: person.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 8,
            '-' * 11
        )
        table.append(line)
        table.append(
            '| {:^3} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} | {:^8} | {:^8} |'.format(
                "№",
                "Ф.И.О.",
                "Группа",
                "1-ая оценка",
                "2-ая оценка",
                "3-ая оценка",
                "4-ая оценка",
                "5-ая оценка"
            )
        )
        table.append(line)

        # Вывести данные о всех оценках ученика.
        for idx, person in enumerate(self.students, 1):
            table.append(
                '| {:>3} | {:<30} | {:<20} | {:>11} | {:>11} | {:>11} | {:>11} | {:>11} |'.format(
                    idx,
                    person.name,
                    person.group,
                    person.marks[0],
                    person.marks[1],
                    person.marks[2],
                    person.marks[3],
                    person.marks[4]
                )
            )
        table.append(line)

        return '\n'.join(table)

    def __repr__(self):
        return self.__str__()

    def select(self, period):
        # Получить данные студентов, которые получили оценку 2.
        parts = command.split(' ', maxsplit=2)
        period = int(parts[1])
        result = []
        count = 0
        for person in self.students:
            if 2 in person.marks:
                count += 1
                result.append(person)
        return result

    def load(self, filename):
        with open(filename, 'r', encoding='utf8') as fin:
            xml = fin.read()
        parser = ET.XMLParser(encoding="utf8")
        tree = ET.fromstring(xml, parser=parser)
        self.students = []

        for person_element in tree:
            name, group, marks = None, None, None

            for element in person_element:
                if element.tag == 'name':
                    name = element.text
                elif element.tag == 'group':
                    group = element.text
                elif element.tag == 'marks':
                    marks = element.text

                if name is not None and group is not None \
                        and marks is not None:
                    self.students.append(
                        Person(
                            name=name,
                            group=group,
                            marks=marks
                        )
                    )

    def save(self, filename):
        root = ET.Element('students')
        for person in self.students:
            person_element = ET.Element('person')

            name_element = ET.SubElement(person_element, 'name')
            name_element.text = person.name

            group_element = ET.SubElement(person_element, 'group')
            group_element.text = person.group

            marks_element = ET.SubElement(person_element, 'marks')
            mark = ''.join(str(i) for i in marks)
            marks_element.text = str(mark)

            root.append(person_element)

        tree = ET.ElementTree(root)
        with open(filename, 'wb') as fout:
            tree.write(fout, encoding='utf8', xml_declaration=True)


if __name__ == '__main__':
    # Выполнить настройку логгера.
    logging.basicConfig(
        filename='students_1_individ.log',
        level=logging.INFO
    )
    # Список учеников.
    staff = Staff()

    # Организовать бесконечный цикл запроса команд.
    while True:
        try:
            # Запросить команду из терминала.
            command = input(">>> ").lower()

            # Выполнить действие в соответствие с командой.
            if command == 'exit':
                break

            elif command == 'add':
                # Запросить данные об учениках.
                n = 5
                name = input("Введите фамилию и имя: ")
                group = input("Введите группу: ")
                marks = list(map(int, input("Введите пять оценок студента, в формате - x y z: ").split(None, n)[:n]))
                # Добавить учеников.
                staff.add(name, group, marks)
                logging.info(
                    f"Добавлен студент: {name}, {group}, "
                    f"получивший оценки {marks} "
                )

            elif command == 'list':
                # Вывести список.
                print(staff)
                logging.info("Отображен список студентов.")

            elif command.startswith('select '):
                parts = command.split(maxsplit=1)
                # Запросить учеников.
                selected = staff.select(parts[1])
                # Вывести результаты запроса.
                if selected:
                    for count, person in enumerate(selected, 1):
                        print(
                            '{:>4}: {}'.format(count, person.name)
                        )
                    logging.info(
                        f"Найдено {len(selected)} студентов с "
                        f"оценкой {parts[1]}."
                    )
                else:
                    print("Нет студентов, которые получили оценку - 2.")
                logging.warning(
                    f"Студенты получившие оценку {parts[1]} не найдены."
                )

            elif command.startswith('load '):
                # Разбить команду на части для имени файла.
                parts = command.split(maxsplit=1)
                # Загрузить данные из файла.
                staff.load(parts[1])
                logging.info(f"Загружены данные из файла {parts[1]}.")

            elif command.startswith('save '):
                # Разбить команду на части для имени файла.
                parts = command.split(maxsplit=1)
                # Сохранить данные в файл.
                staff.save(parts[1])
                logging.info(f"Сохранены данные в файл {parts[1]}.")

            elif command == 'help':
                # Вывести справку о работе с программой.
                print("Список команд:\n")
                print("add - добавить студента;")
                print("list - вывести список студентов;")
                print("load <имя файла> - загрузить данные из файла;")
                print("save <имя файла> - сохранить данные в файл;")
                print("select <оценка> - найти студентов которые получили такую оценку;")
                print("help - отобразить справку;")
                print("exit - завершить работу с программой.")
            else:
                raise UnknownCommandError(command)
        except Exception as exc:
            logging.error(f"Ошибка: {exc}")
            print(exc, file=sys.stderr)