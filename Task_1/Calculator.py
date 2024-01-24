def identification_input(input_str):
    operators = {'+', '-', '*', '/'}
    operators_count = sum(input_str.count(o) for o in operators)

    if operators_count != 1:
        raise ValueError('Формат математической операции не удовлетворяет заданию - два операнда и один оператор')

    for operator in operators:
        if operator in input_str:
            a,b = map(int, input_str.split(operator))
            if not (1 <= a <= 10) or not (1 <= b <= 10):
                raise ValueError('Число должно быть от 1 до 10')
            return a, operator, b

    raise ValueError('Недопустимая арифметическая операция')


def calculator(input_str):
    a, operator, b = identification_input(input_str)
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            return ValueError('Деление на ноль')
        return a // b


if __name__ == '__main__':
    user_input = input('Введите пример: ')

    try:
        result = calculator(user_input)
        print(result)
    except Exception as e:
        print(f'Ошибка: {e}')
