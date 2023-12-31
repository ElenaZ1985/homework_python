1. Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

def is_triangle(a, b, c):

    if a + b < c or b + c < a or c + a < b:

        return False

    else:

        return True

a = 3

b = 4

c = 5

if is_triangle(a, b, c) == True:

    print("Треугольник существует")    

else:

    print("Треугольник не существует")



if is_triangle(a, b, c) == True:

    if a==b==c:

        print("Треугольник является равносторонним")

    elif a==b or a==c or b==c:

        print("Треугольник является равнобедренным")

    else:

        print("Треугольник является разносторонним")


2.  Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = int(input('Введите число: '))



res = [i for i in range(1, num + 1) if num % i == 0]

if num < 0 or num > 99999:

    print('Число должно быть положительным и не более 99999')

elif res[0] == 1 and res[1] == num:

    print(f'Число {num} является простым')

else:

    print(f'Число {num} является составным')
