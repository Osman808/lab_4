#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    d = int(input("Введите день: "))
    m = int(input("Введите месяц: "))
    y = int(input("Введите год: "))
    if d < 31:
        if m < 12:
            print((m - 1) * 30 + d)
        else:
            print("Ты серьзно? Введи число до 12")
    else:
        print("Как правило в месяце в месяце 28-31 день")
