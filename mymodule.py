#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import date
from dataclasses import dataclass, field
from typing import List
import sys
import logging


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


@dataclass(frozen=True)
class People:
    name: str
    phone_number: int
    birthday: list[int]


@dataclass
class Man:
    soul: List[People] = field(default_factory=lambda: [])

    def add(self, name, phone_number, birthday):
        self.soul.append(
            People(
                name=name,
                phone_number=phone_number,
                birthday=birthday
            )
        )
        self.soul.sort(key=lambda people: people.name)

    def __str__(self):
        # Заголовок таблицы.
        table = []
        line = '+-{}-+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
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
            '| {:^4} | {:^30} | {:^20} | {:^8} | {:^8} | {:^8} |'.format(
                "No",
                "Ф.И.",
                "Номер телефона",
                "День",
                "Месяц",
                "Год"
            )
        )
        table.append(line)

        # Вывести данные о всех оценках ученика.
        for idx, people in enumerate(self.soul, 1):
            table.append(
                '| {:>4} | {:<30} | {:<20} | {:>8} | {:>8} | {:>8} |'.format(
                    idx,
                    people.name,
                    people.phone_number,
                    people.birthday[0],
                    people.birthday[1],
                    people.birthday[2],
                )
            )
        table.append(line)

        return '\n'.join(table)

    def __repr__(self):
        return self.__str__()

    def select(self, period):
        # # Проверить сведения людей из списка
        parts = command.split(' ', maxsplit=2)
        period = int(parts[1])
        result = []
        count = 0
        for people in self.soul:
            if people.birthday:
                if people.birthday[1] == period:
                    count += 1
                    result.append(people)
        return result
