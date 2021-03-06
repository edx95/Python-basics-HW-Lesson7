"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data: list):
        ld = len(data[0])
        for row in data:
            if len(row) != ld:
                raise ValueError(f"непрямоугольные матрицы не поддерживаются {data}")
        self.data = data

    def __str__(self):
        return ' \n'.join(' '.join((str(num) for num in row)) for row in self.data)

    def __add__(self, other):
        self.__check_other_same(other)
        return Matrix([[el_s + el_o for el_s, el_o in zip(row_s, row_o)]
                       for row_s, row_o in zip(self.data, other.data)])

    def __iadd__(self, other):
        self.__check_other_same(other)
        for i, row_o in enumerate(other.data):
            for j, el in enumerate(row_o):
                self.data[i][j] += el
        return self

    def __check_other_same(self, other):
        """
        Проверить тип и размеры кандидата в матрицу
         : param other: кандидат
         : return: None, если то же самое
        """
        if type(other) != Matrix:
            raise ValueError(f'Введите объект матричного типа')

        ds = self.dimensions()
        do = other.dimensions()
        if ds != do:
            raise ValueError

    def dimensions(self):
        """
        Размер формы матрицы
        :return: tuple
        """
        return len(self.data), len(self.data[0])


if __name__ == '__main__':
    m1 = Matrix([[31, 22], [37, 43], [51, 86]])
    m2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])
    m3 = Matrix([[3, 5, 8, 3], [8, 3, 7, 1]])
    print(m1)
    print('-'*25)
    print(m2)
    print('-'*25)
    print(m3)
    print('-'*25)
    m3 += Matrix([[-3, -5, -8, -3], [-7, -1, -4, 3]])
    print(m3)
    print('-'*25)

    ms1 = m1 + Matrix([[1, 2], [3, 4], [5, 6]])
    print('ms1\n', ms1, sep='')
    print('-' * 25)
    ms2 = ms1 + Matrix([[-1, -2], [-3, -4], [-5, -6]])
    print('ms2\n', ms2, sep='')
    ms3 = ms1 + Matrix([[1, 2], [3, 4], [5, 6]]) + Matrix([[-10, -20], [-30, -40], [-50, -60]])
    print('ms3\n', ms3, sep='')