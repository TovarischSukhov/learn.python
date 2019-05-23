"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(a,b):
    if type(a) == str and type(b) == str:
        if a == b:
            return 1
        elif a != b and len(a) > len(b):
            return 2
        elif a != b and b =="learn":
            return 3   
    else:
        return 0    
if __name__ == "__main__":
    print(main(444,"gfgf"))
    print(main("444","444"))
    print(main("444","44"))
    print(main("444","learn"))