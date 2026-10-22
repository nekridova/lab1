import math

user_input = ""
current_index = 0

def skip_spaces():
    global current_index
    while current_index < len(user_input) and user_input[current_index] == " ":
        current_index += 1

def parse_expression():
    global current_index
    result = parse_multiply_divide()
    
    while current_index < len(user_input):
        skip_spaces()
        if current_index >= len(user_input):
            break
            
        if user_input[current_index:current_index+2] == '!=':
            current_index += 2
            right_side = parse_multiply_divide()
            if result != right_side:
                result = 1
            else:
                result = 0
                
        elif user_input[current_index] == '+':
            current_index += 1
            result = result + parse_multiply_divide()
            
        elif user_input[current_index] == '-':
            current_index += 1
            result = result - parse_multiply_divide()
            
        else:
            break
            
    return result

def parse_multiply_divide():
    global current_index
    result = parse_primary()
    
    while current_index < len(user_input):
        skip_spaces()
        if current_index >= len(user_input):
            break
            
        if user_input[current_index] == '*':
            current_index += 1
            result = result * parse_primary()
            
        elif user_input[current_index] == '/':
            current_index += 1
            divisor = parse_primary()
            if divisor == 0:
                print("Ошибка: На 0 делить нельзя")
                exit()
            result = result / divisor
            
        else:
            break
            
    return result

def parse_primary():
    global current_index
    skip_spaces()
    
    if current_index >= len(user_input):
        print("Ошибка: Выражение пустое или оборвалось")
        exit()
        
    char = user_input[current_index]
    
    if char == '-':
        current_index += 1
        return -parse_primary()
        
    if char == '+':
        current_index += 1
        return parse_primary()
        
    if char == '(':
        current_index += 1
        result = parse_expression()
        if current_index >= len(user_input) or user_input[current_index] != ')':
            print("Ошибка: Не хватает закрывающей скобки")
            exit()
        current_index += 1
        return result
        
    if user_input[current_index:current_index+4] == 'fact':
        current_index += 4
        skip_spaces()
        if current_index >= len(user_input) or user_input[current_index] != '(':
            print("Ошибка: После fact нужна скобка")
            exit()
        current_index += 1
        
        num = parse_expression()
        
        if current_index >= len(user_input) or user_input[current_index] != ')':
            print("Ошибка: Не хватает скобки в fact")
            exit()
        current_index += 1
        
        if num < 0 or num != int(num):
            print("Ошибка: Факториал только для целых неотрицательных чисел")
            exit()
        if num > 20:
            print("Ошибка: Слишком большое число")
            exit()
            
        return math.factorial(int(num))
        
    start_pos = current_index
    while current_index < len(user_input) and (user_input[current_index].isdigit() or user_input[current_index] == '.'):
        current_index += 1
        
    if start_pos == current_index:
        print("Ошибка: Неизвестный символ")
        exit()
        
    return float(user_input[start_pos:current_index])

user_input = input("Введите пример: ")
current_index = 0

answer = parse_expression()

skip_spaces()
if current_index < len(user_input):
    print("Введены лишние знаки")
else:
    if answer == int(answer):
        answer = int(answer)
    print(f"Ответ: {answer}")
