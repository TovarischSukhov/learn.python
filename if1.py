a = int(input("Введите свой возраст:"))

def ages(a):
  if a < 7:
  	return ("Ты ходишь в детский сад")
  elif a < 18:
    	return ("Ты учишься в школе")
  elif a < 22:
  	return ("Ты учишься в ВУЗе")
  else:
  	return ("Ты работаешь")
  	
itog = ages(a)
print(itog)