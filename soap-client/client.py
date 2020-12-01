from soap import soap_request
from params import Params
import yaml


def load_wsdl_url():
    with open("config.yaml", 'r') as stream:
        try:
            data = yaml.safe_load(stream)
            print('Загружен файл конфигурации.')
            print(f"Ссылка на сервис: {data['soap.wsdl.url']}.")
            return data['soap.wsdl.url']
        except yaml.YAMLError:
            print('Произошла ошибка при попытке загрузки wsdl url из файла конфигурации!')
            print('Будет использовано стандартной значение - http://localhost:8080/psu-trrp-lab3/calculate?wsdl.')
            return 'http://localhost:8080/psu-trrp-lab3/calculate?wsdl'


def menu():
    url = load_wsdl_url()
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
        print(f"Результат: {soap_request(url, params)}")
        print('---------------------------------')


menu()
