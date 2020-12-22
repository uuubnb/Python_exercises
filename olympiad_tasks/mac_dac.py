'''
Условие
Банковский счет Скруджа Макдака подвергся взлому, после чего злоумышленники получили доступ к его счету и узнали, сколько на нем средств. Они решили проучить Скруджа и учинить такую пакость: самую большую цифру заменить на «0».
Тебе потребуется написать программу, которая по заданному числу (сумма на счете Скруджа) определит, сколько денег непутевый Скрудж потерял в результате пакости злоумышленников.

Входные данные
На вход подается одно четырехзначное число — сумма на счете Скруджа.

Выходные данные
Требуется вернуть число - сколько потерял Скрудж.
'''


def main(was: int):
    arr = [int(i) for i in str(was)]
    max_int = max(arr)
    x = [i for i, j in enumerate(arr) if j == max_int]
    for i in x:
        arr[i] = 0
    now = int(''.join(str(e) for e in arr))

    return was - now

result = main(1234)
print(result)