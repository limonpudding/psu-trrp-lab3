from soap import soap_request
from params import Params


def menu():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("0. Выход")
        option = int(input())

        if option not in range(5):
            print("Неверный ввод!")
            continue
        if option == 0:
            break

        operation = ''
        if option == 1:
            operation = 'add'
        if option == 2:
            operation = 'sub'
        if option == 3:
            operation = 'mul'
        if option == 4:
            operation = 'div'
        print("Введите 1 операнд:")
        arg1 = input()
        print("Введите 2 операнд:")
        arg2 = input()
        params = Params(arg1, arg2, operation)
        print(f"Результат: {soap_request(params)}")
        print('---------------------------------')


menu()
