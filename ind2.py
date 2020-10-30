#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a1 = int(input("Введите a1: "))
    a2 = int(input("Введите a2: "))
    r = int(input("Введите R: "))

    if a1**2 + a2**2 < r**2 or a1**2 + a2**2 == r**2:
        print("Точка попадет в окружность")
    else:
        print("Точка не попадет в окружность")
