from pulp import LpMaximize, LpProblem, LpVariable

# Створюємо модель лінійного програмування
model = LpProblem(name="drink-production", sense=LpMaximize)

# Змінні рішення
lemonade = LpVariable(name="Lemonade", lowBound=0, cat="Integer")
fruit_juice = LpVariable(name="Fruit_Juice", lowBound=0, cat="Integer")

# Цільова функція: максимізувати загальну кількість вироблених напоїв
model += lemonade + fruit_juice, "Total_Production"

# Обмеження ресурсів
model += (2 * lemonade + fruit_juice <= 100), "Water_Constraint"
model += (1 * lemonade <= 50), "Sugar_Constraint"
model += (1 * lemonade <= 30), "Lemon_Juice_Constraint"
model += (2 * fruit_juice <= 40), "Fruit_Puree_Constraint"

# Розв'язуємо задачу
model.solve()

# Виводимо результати
print(f"Кількість виробленого лимонаду: {lemonade.varValue}")
print(f"Кількість виробленого фруктового соку: {fruit_juice.varValue}")
print(f"Загальна кількість виробленої продукції: {lemonade.varValue + fruit_juice.varValue}")
