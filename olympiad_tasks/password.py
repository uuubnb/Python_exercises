'''
Британские ученые выяснили, что чаще всего взламывают пароли, содержащие группы одинаковых, идущих подряд символов, пробелы и звездочки. И гораздо реже взламывают пароли, содержащие многоточия.
Узнав про эту новость, Никита крепко задумался: почти все его пароли попадают в группу риска! Для того, чтобы исправить ситуацию, он решил конвертировать все свои пароли по следующему правилу: от группы одинаковых символов оставить один; два и более пробелов заменить на знак подчеркивания, а две и более звездочки — на многоточие.
Напиши программу, которая будет быстро и правильно производить конвертацию пароля.

Входные данные
На выход подается один аргумент: пароль — непустая строка длиной до 1000 символов, которая может состоять из строчных букв латинского алфавита, пробелов и символов '*'.

Выходные данные
Верни пароль, полученный после конвертации.
'''

def main(text):
    text = text.lower()
    new_text = []
    repeats = 0
    for i in range(len(text)):
        if i < (len(text)-1):
            if text[i] != text[i+1]:
                if repeats > 0 and text[i] == '*':
                    new_text.append('...')
                    repeats = 0
                elif repeats > 0 and text[i] == ' ':
                    new_text.append('_')
                    repeats = 0
                elif repeats > 0:
                    new_text.append(text[i])
                    repeats = 0
                else:
                    new_text.append(text[i])
                    repeats = 0
            else:
                repeats += 1
        elif i == (len(text)-1):
            if repeats > 0 and text[len(text)-1] == '*':
                new_text.append('...')
                repeats = 0
            elif repeats > 0 and text[len(text)-1] == ' ':
                new_text.append('_')
                repeats = 0
            elif repeats > 0:
                new_text.append(text[len(text)-1])
                repeats = 0
            else:
                new_text.append(text[i])
                repeats = 0

    return ''.join(new_text)


data = '*anton*'
print(main(data))

