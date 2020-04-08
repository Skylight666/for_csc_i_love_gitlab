import numpy as np
import matplotlib.pyplot as plt
import torch # подключаем основной пакет PyTorch
import torchviz

# стандартная команда настройки девайса на GPU
# device = 'cuda' if torch.cuda.is_available() else 'cpu'
device = 'cpu'
print(device)

# Наши исходные данные хранятся в формате массивов NumPy,
# требуется преобразовать их в формат тензоров PyTorch,
# привести к типу float и выгрузить на девайс
np.random.seed(42)

# создаём np-массив из 100 случайных чисел в диапазоне 0..1
sz = 100
x = np.random.rand(sz, 1)

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

x_train_tensor = torch.from_numpy(x_train).float().to(device)
y_train_tensor = torch.from_numpy(y_train).float().to(device)
print(x_train_tensor.type())

# инициализация повторяемой посл-ти случайных чисел
torch.manual_seed(42)

# задаём начальные случайные значения коэффициентам линейной регрессии
a = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
b = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
print(a, b)

# скорость обучения
lr = 0.1

# количество эпох
n_epochs = 1000

for epoch in range(n_epochs):

    # как и в примере с numpy, записываем нашу линейную зависимость,
    # только теперь в качестве обучающей выборки -- тензор
    yhat = a + b * x_train_tensor

    # 1. считаем лосс как и раньше
    error = y_train_tensor - yhat
    loss = (error ** 2).mean()

    # 2. вычисляем градиенты автоматически!
    loss.backward()


    # ПЕРВАЯ ПОПЫТКА (неверно)
    # TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
    # a = a - lr * a.grad
    # b = b - lr * b.grad

    # ВТОРАЯ ПОПЫТКА (неверно)
    # RuntimeError: a leaf Variable that requires grad has been used in an in-place operation.
    # a -= lr * a.grad
    # b -= lr * b.grad

    # ТРЕТЬЯ ПОПЫТКА (верно)
    with torch.no_grad():
        a -= lr * a.grad
        b -= lr * b.grad

    # Обнуляем градиенты вручную
    a.grad.zero_()
    b.grad.zero_()

print(a, b)


torch.manual_seed(42)
a = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)
b = torch.randn(1, requires_grad=True, dtype=torch.float, device=device)

yhat = a + b * x_train_tensor
error = y_train_tensor - yhat
loss = (error ** 2).mean()

torchviz.make_dot(loss).view() # визуализируем граф вычислений
