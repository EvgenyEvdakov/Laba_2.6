#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Создаем пустой список для хранения словарей
    routes = []

    # Запускаем бесконечный цикл для добавления маршрутов
    while True:
        # Вводим данные о маршруте с клавиатуры
        start = input("Введите начальный пункт маршрута: ")
        end = input("Введите конечный пункт маршрута: ")
        number = input("Введите номер маршрута: ")

        # Создаем словарь с данными о маршруте
        route = {
            "start": start,
            "end": end,
            "number": number
        }
        # Добавляем словарь в список

        routes.append(route)

        # Сортируем список маршрутов по номерам маршрутов
        routes = sorted(routes, key=lambda x: x["number"])

        # Спрашиваем пользователя, хочет ли он добавить еще один маршрут
        choice = input("Хотите добавить еще один маршрут? (y/n): ")
        if choice.lower() == "n":
            break

    # Выводим на экран информацию о маршруте по номеру
    number = input("Введите номер маршрута для поиска: ")
    found = False
    for route in routes:
        if route["number"] == number:
            print("Начальный пункт маршрута:", route["start"])
            print("Конечный пункт маршрута:", route["end"])
            found = True
            break

    else:
        print("Маршрут с таким номером не найден.")