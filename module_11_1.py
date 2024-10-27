import requests
import numpy as np


# пример реквеста
def test_requests():
    url = 'https://jsonplaceholder.typicode.com/posts/1'

    try:
        response = requests.get(url)

        if response.status_code == 200:
            print("Запрос успешен!")
            data = response.json()
            print("Данные получены:")
            print(f"Заголовок: {data['title']}")
            print(f"Содержимое: {data['body']}")
        else:
            print(f"Ошибка. Статус-код: {response.status_code}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == '__main__':
    test_requests()


# пример нумпай
def test_numpy():
    arr_1d = np.array([1, 2, 3, 4, 5])
    print("Одномерный массив:")
    print(arr_1d)

    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
    print("\nДвумерный массив (матрица):")
    print(arr_2d)

    print("\nСумма элементов массива 1D:", np.sum(arr_1d))
    print("Среднее значение элементов массива 1D:", np.mean(arr_1d))
    print("Максимальное значение массива 1D:", np.max(arr_1d))

    arr_squared = arr_1d ** 2
    print("\nКвадраты элементов массива 1D:")
    print(arr_squared)

    zeros = np.zeros((2, 3))
    ones = np.ones((3, 2))
    print("\nМассив из нулей:")
    print(zeros)
    print("Массив из единиц:")
    print(ones)

    product = np.dot(arr_2d, ones)
    print("\nРезультат умножения матрицы на массив из единиц:")
    print(product)


if __name__ == '__main__':
    test_numpy()

# https://github.com/numpy/numpy и https://github.com/psf/requests не понял где тут им комментарии писать, поставил по звёздочке)
# Смысл библиотеки `requests` заключается в упрощении и улучшении работы разработчиков с HTTP-запросами и веб-API.
# Она предоставляет интуитивно понятные инструменты для отправки запросов, обработки ответов и управления сессиями,
# что делает взаимодействие с интернет-ресурсами более доступным и эффективным.

# А библиотека `NumPy` в Python предназначена для работы с многомерными массивами и матрицами,
# а также предоставляет широкий спектр математических функций для их обработки.
# Она значительно упрощает выполнение научных вычислений, анализ данных и работу с векторизированными операциями,
# что делает её основным инструментом для научных и численных расчётов в Python.
