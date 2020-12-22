'''
Условие
Как-то раз хипстер Дима решил посчитать, сколько у него носков. Оказалось, что у Димы есть a красных носков и b синих носков. Согласно последним веяниям моды, хипстеры должны носить носки разных цветов: на левой ноге красный, а на правой — синий.
Каждый день Дима надевает новые носки, а перед сном выкидывает их, поскольку покупать новые носки ему больше по нраву, чем брать кредит на стиральную машину.
Диме стало интересно, какое максимальное количество дней он сможет носить разноцветные носки по моде, и сколько затем дней он сможет ходить в одноцветных носках, пока носки либо не закончатся, либо из оставшихся носков нельзя будет составить ни одной пары.
Поможешь ему?

Входные данные
На вход подается два аргумента:

количество носков красного цвета
количество носков синего цвета

Выходные данные
Верни массив из двух чисел — максимальное количество дней, в которые Дима сможет носить разноцветные носки, и количество дней, когда он сможет носить одноцветные носки до тех пор, пока они либо не кончатся, либо из оставшихся носков нельзя будет составить ни одной пары.
Напомним, что в конце дня Дима выкидывает носки, которые он носил в этот день.
'''

def main(arg1, arg2):
    red = arg1
    blue = arg2
    if red > blue:
        style = blue
    else:
        style = red
    socks_left = (red+blue) - style*2 
    days_left = socks_left // 2
    return [style, days_left]



xyz = print(main(7,3))