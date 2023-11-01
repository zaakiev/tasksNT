import sys

def massive_function(n, m):
    result = [] # Пустой список
    i = 1
    while True:
        result.append(i) # Нынешняя позиция в массив
        i = 1 + (i + m - 2) % n # Получаем следующуую позицию в массиве
        if i == 1:
            break
    return result

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Использование: python3 task1.py m n")
        sys.exit(1)
    n = int(sys.argv[1])
    m = int(sys.argv[2])
  
    result = circular_array_path(n, m)
    
    result_str = ''.join(map(str, result)) # Список в строку
    print(result_str)

