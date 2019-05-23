"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main(ocenki):
  vseshkola = 0
  vesklass = 0
  kol = 0
  vsekol = 0
  p = ""
  for klass in ocenki:
    for bal in klass["scores"]:
        vesklass += bal
        vseshkola += bal
        kol += 1
        vsekol += 1
    p += "Средний балл "+ klass["school_class"] + " класса:" + str(vesklass/kol)+ "\n" 
    vesklass = 0
    kol = 0
  return(print(p + "Средний балл школы: " + str(vseshkola/vsekol)))
if __name__ == "__main__":
    ocenki = [{'school_class': '4a', 'scores': [3,4,4,5,2]},
    {'school_class': '3b', 'scores': [2,4,5,5,5]},
    {'school_class': '2c', 'scores': [2,2,3,3,3]}]
main(ocenki)