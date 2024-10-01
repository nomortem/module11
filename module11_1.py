# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

# Пример с Pandas
def analyze_data_with_pandas(file_path):

    df = pd.read_csv(file_path)


    print("Первые 5 строк данных:")
    print(df.head())


    print("\nОписание данных (основные статистические параметры):")
    print(df.describe())


    missing_values = df.isnull().sum()
    print("\nКоличество пропущенных значений по каждому столбцу:")
    print(missing_values)


if __name__ == "__main__":
    file_path = 'data.csv'
    analyze_data_with_pandas(file_path)


#  Пример с numpy
def numpy_array_operations():

    arr = np.arange(1, 11)

    print("Оригинальный массив:", arr)
    print("Квадрат каждого элемента массива:", np.square(arr))
    print("Среднее значение элементов массива:", np.mean(arr))
    print("Сумма элементов массива:", np.sum(arr))

if __name__ == "__main__":
    numpy_array_operations()
