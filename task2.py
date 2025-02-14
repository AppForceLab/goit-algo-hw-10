import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a = 0  
b = 2  

# Метод Монте-Карло для обчислення інтегралу
N = 100000  # Кількість випадкових точок
x_rand = np.random.uniform(a, b, N)
y_rand = np.random.uniform(0, b**2, N)

# Обчислення кількості точок під кривою
under_curve = y_rand < f(x_rand)
monte_carlo_integral = (b * (b**2)) * np.sum(under_curve) / N

# Аналітичне обчислення інтегралу
analytical_integral, error = spi.quad(f, a, b)

# Візуалізація
x = np.linspace(a, b, 400)
y = f(x)

fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2, label=r'$f(x) = x^2$')

# Точки, використані для методу Монте-Карло
ax.scatter(x_rand[:1000], y_rand[:1000], c=under_curve[:1000], cmap='coolwarm', s=1, alpha=0.5)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([a - 0.5, b + 0.5])
ax.set_ylim([0, b**2 + 0.5])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Метод Монте-Карло для інтеграції')

# Відображення результатів
plt.legend()
plt.grid()
plt.show()

# Вивід результатів
print("Метод Монте-Карло:", monte_carlo_integral)
print("Аналітичний інтеграл:", analytical_integral)
print("Різниця між методами:", abs(monte_carlo_integral - analytical_integral))