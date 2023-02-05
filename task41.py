# Вычислить значение выражения:
# Уровень 1:
# 1 действие
# 2 аргумента 12 + 15
# Уровень 2:
# Количество действий произвольное
# 12 + 15 - 4
#Уровень 3:
# Действия имеют приоритет
# 12 - 4*2 +6/3


n = '12 + 15'
m = n.split()
m2 = []
print(m)

def calc(a, b, c):
    if c == '+':
      return a + b
    elif c == '-':   
      return a - b   
    elif c == '/':
      return a / b   
    elif c == '*':
      return a * b


a = int(m[0])
c = m[1]
b = int(m[2])


result = int(m[0])

for i in range(1, len(m) - 1, 2):
    if m[i] == '*' or m[i] == '/':
     result = calc(result, int(m[i + 1]), m[i])
     m2.append(result)
    else:
      m2.append(m[i]) 
      m2.append(int(m[i + 1])) 


for i in range(1, len(m) - 1, 2):
    if m[i] == '+' or m[i] == '-':
     result = calc(result, int(m[i + 1]), m[i])
     m2.append(result)
    else:
      m2.append(m[i]) 
      m2.append(int(m[i + 1])) 


print(m[i], m[i + 1])
print(m2)
print(result)


#print(a,b,c)

#print(calc(a, b, c))