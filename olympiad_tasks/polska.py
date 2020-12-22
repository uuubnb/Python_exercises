import operator


def main(string):
    operations = {'+': operator.add, 
                '-': operator.sub, 
                '*': operator.mul, 
                '/': operator.truediv}
    formula = string.split(' ')
    output_stack = []
    for i in formula:
        if i.isnumeric():
            output_stack.insert(0, i)
        elif i in '+-*/':
            if len(output_stack) < 2:
                print('Something is wrong in your formula')
                break
            else:   
                x1 = int(output_stack.pop(1))
                x2 = int(output_stack.pop(0))
                operation = operations[i](x1,x2)
                output_stack.insert(0,str(operation))
        else: 
            raise ValueError
    
    result = int(''.join(output_stack))
    return result
  

string1 = '4 2 10 * +'
string2 = '2 3 + 8 *'

x = main(string1)
print(x)


