a = []
for i in range(25):
    while True:
        try:
            grade = int(input(f"Оценка ученика {i+1}: "))
            if grade in [2, 3, 4, 5]:
                a.append(grade)
                break
            else:
                print("Ошибка! Оценка должна быть 2, 3, 4 или 5.")
        except ValueError:
            print("Ошибка! Введите число.")

count_2 = a.count(2)
count_3 = a.count(3)
count_4 = a.count(4)
count_5 = a.count(5)

print('5:',count_5,'4:',count_4,'3:',count_3,'2:',count_2)
