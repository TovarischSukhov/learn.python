"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
  try:
    while True:
      asc = input("Задайте вопрос:")
      slovar = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Гулять пойдем?" : "Вечером"}
      print(slovar.get(asc, "Мне нечего ответить"))        
  except KeyboardInterrupt:
    print("Пока!")

ask_user()
