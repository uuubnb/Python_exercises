### Weasel script

Вы когда-нибудь слышали про теорему о бесконечных обезьянах? В ней утверждается, что если обезьяна будет беспорядочно нажимать на клавиши клавиатуры бесконечное количество времени, то рано или поздно напечатает заданный текст (например, полное собрание сочинений Вильяма Шекспира). Что ж, предположим, что мы заменяем обезьяну функцией на Python. Как вы думаете, сколько она потратит времени на генерирование хотя бы одного предложения из Шекспира? Выберем для проверки фразу “methinks it is like a weasel”.

Вам наверняка не захочется запускать эту программу в браузере, так что запускайте вашу любимую Python IDE. Симуляция будет выполняться с помощью функции, генерирующей строку из двадцати семи символов путём случайного выбора из двадцати шести букв алфавита + пробел. Мы напишем ещё одну функцию, которая будет оценивать каждую сгенерированную строку, сравнивая её с целью.

Третья функция будет циклично вызывать генератор и оценщик до тех пор, пока не совпадёт 100% букв. В случае несовпадения будет генерироваться новая строка целиком. Чтобы было проще следить за прогрессом программы, эта третья функция должна печатать лучшую из уже сгенерированных строк и её оценку каждые тысячу попыток.

##### Усложнённое задание для самопроверки

Посмотрите, сможете ли вы улучшить программу из самопроверки, сохраняя правильно стоящие буквы и изменяя всего лишь одну из оставшихся, чтобы приблизиться к результату. Алгоритм такого типа относится к классу “поиска с восхождением к вершине”, в котором результат сохраняется только в том случае, если он лучше предыдущего.
