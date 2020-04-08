import numpy as np
import matplotlib.pyplot as plt

# инициализация повторяемой последовательности случайных чисел
np.random.seed(42)

# создаём np-массив из 100 случайных чисел в диапазоне 0..1
sz = 200
x = np.random.rand(sz, 1) - 0.5

# строим функцию y = f(x) и добавляем немного гауссова шума
y = 1 + 2 * x + 0.1 * np.random.randn(sz, 1)

# формируем индексы от 0 до 99
idx = np.arange(sz)
# случайно их тасуем
np.random.shuffle(idx)


# первые 80 случайных индексов (значений x) используем для обучения
sz80 = (int)(sz*0.8)
train_idx = idx[: sz80]

# оставшиеся 20 -- для валидации
val_idx = idx[sz80:]

# формируем наборы обучающих данных
x_train, y_train = x[train_idx], y[train_idx]
# и наборы для валидации
x_val, y_val = x[val_idx], y[val_idx]

# выводим на экран
plt.scatter(x_train, y_train)
plt.title('Обучающая выборка')
# plt.ylim(0, 10)
# plt.xlim(-10, 10)
plt.show()
plt.scatter(x_val, y_val, color= "red")
plt.title('Проверочная выборка')
plt.show()

np.random.seed(42)

# задаём начальные случайные значения коэффициентам линейной регрессии
a = np.random.randn(1)
b = np.random.randn(1)
print(a,b)

# скорость обучения
lr = 0.1
# количество эпох
n_epochs = 1000

# основной цикл
for epoch in range(n_epochs):

    # рассчитываем результирующий массив с текущими коэффициентами a и b
    # на основе обучающей выборки
    yhat = a + b * x_train

    # 1. определяем лосс
    # сперва считаем отклонение нового результата от обучающего:
    error = (y_train - yhat)
    # и затем считаем среднеквадратическую ошибку:
    loss = (error ** 2).mean()

    # 2. считаем градиенты (вспоминая формулу производной)
    # для коэффициента a
    a_grad = -2 * error.mean()
    # для коэффициента b
    b_grad = -2 * (x_train * error).mean()

    # 3. обновляем параметры, используя коэффициент скорости обучения,
    # градиенты берём с обратным знаком
    a = a - lr * a_grad
    b = b - lr * b_grad
print(a,b)
