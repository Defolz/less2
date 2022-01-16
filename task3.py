f = open('travels.txt', 'r')
l = list()
maxx = int()
number = list()
number1 = list()
number2 = list()
number3 = list()
s = list()
for i in f:
    l = i.split()
    if l[0] == "1":
        l[6] = int(l[6])
        number.append(l[6])
    if l[0] == "2":
        l[6] = int(l[6])
        number1.append(l[6])
    if l[0] == "3":
        l[6] = int(l[6])
        number2.append(l[6])
    if l[2] == "Липки":
        l[6] = int(l[6])
        number3.append(l[6])
    if l[0] == "1":
        l[4] = int(l[4])
        s.append(l[4])
        
                                          
print("Первое октября: ", sum(number))
print("Второе октября: ", sum(number1))
print("Третье октября: ", sum(number2))
print("Перевезено в липки: ", sum(number3))
print("Суммарное расстояне за 1 октября: ", sum(s))

