a = int(input("������� ���� �������:"))

def ages(a):
  if a < 7:
  	return ("�� ������ � ������� ���")
  elif a < 18:
    	return ("�� ������� � �����")
  elif a < 22:
  	return ("�� ������� � ����")
  else:
  	return ("�� ���������")
  	
itog = ages(a)
print(itog)