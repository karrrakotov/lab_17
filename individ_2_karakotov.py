#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from fincalc import Bankomat

#   Выполнить индивидуальное задание 1 лабораторной работы 12, максимально задействовав
#   имеющиеся в Python средства перегрузки операторов.

#   Вариант 11.


if __name__ == '__main__':
    r1 = Bankomat(start_sum=150, new_sum=200, final_sum=350)
    print(f"r1 = {r1}")

    r2 = Bankomat(start_sum=200, new_sum=288, final_sum=488)
    print(f"r2 = {r2}")

    print(f"Sum_1 < Sum2: {r1 < r2}")
    print(f"Sum1 > Sum2: {r1 > r2}")
    print(f"Sum1 <= Sum2: {r1 <= r2}")
    print(f"Sum1 >= Sum2: {r1 >= r2}")
    print(f"Sum1 = Sum2: {r1 == r2}")
    print(f"Sum1 != Sum2: {r1 != r2}")

    print(f"Sum1 + Sum2: {r1 + r2}")
    print(f"Sum1 - Sum2: {r1 - r2}")
    print(f"Sum1 * Sum2: {r1 * r2}")
    print(f"Sum1 / Sum2: {r1 / r2}")