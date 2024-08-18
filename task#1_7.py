class TreeNode:
    def __init__(self, value):
        # Ініціалізація вузла дерева
        self.value = value
        self.left = None
        self.right = None
        self.height = 1  # Висота вузла для балансування

def get_height(node):
    # Функція для отримання висоти вузла
    if not node:
        return 0
    return node.height

def update_height(node):
    # Функція для оновлення висоти вузла після вставки або видалення
    if not node:
        return
    node.height = 1 + max(get_height(node.left), get_height(node.right))

def get_balance(node):
    # Функція для обчислення балансу вузла (різниця висоти лівого і правого піддерева)
    if not node:
        return 0
    return get_height(node.left) - get_height(node.right)

def rotate_right(y):
    # Праве обертання дерева
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x

def rotate_left(x):
    # Ліве обертання дерева
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y

def insert(node, key):
    # Вставка нового ключа у дерево з автоматичним балансуванням
    if not node:
        return TreeNode(key)
    if key < node.value:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    update_height(node)

    balance = get_balance(node)

    # Left Left Case
    if balance > 1 and key < node.left.value:
        return rotate_right(node)

    # Right Right Case
    if balance < -1 and key > node.right.value:
        return rotate_left(node)

    # Left Right Case
    if balance > 1 and key > node.left.value:
        node.left = rotate_left(node.left)
        return rotate_right(node)

    # Right Left Case
    if balance < -1 and key < node.right.value:
        node.right = rotate_right(node.right)
        return rotate_left(node)

    return node

def print_tree(node, level=0, prefix="Root: "):
    # Виведення дерева у зручному для читання форматі
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.value))
        if node.left is not None or node.right is not None:
            if node.left:
                print_tree(node.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if node.right:
                print_tree(node.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")

# Завдання 1: Знаходження найбільшого значення у дереві
def find_max_value(node):
    # Якщо дерево порожнє, повертаємо мінімальне можливе значення
    if node is None:
        return float('-inf')
    # Проходимо до крайнього правого вузла
    while node.right is not None:
        node = node.right
    return node.value

# Завдання 2: Знаходження найменшого значення у дереві
def find_min_value(node):
    # Якщо дерево порожнє, повертаємо максимальне можливе значення
    if node is None:
        return float('inf')
    # Проходимо до крайнього лівого вузла
    while node.left is not None:
        node = node.left
    return node.value

# Завдання 3: Обчислення суми всіх значень у дереві
def sum_of_values(node):
    # Якщо дерево порожнє, сума дорівнює 0
    if node is None:
        return 0
    # Рекурсивно обчислюємо суму значень усіх вузлів у дереві
    return node.value + sum_of_values(node.left) + sum_of_values(node.right)

# Приклад використання
root = None
values = [50, 25, 75, 10, 30, 60, 85, 5, 15, 27, 35, 55, 65, 80, 90, 3, 8, 12, 20, 33]

# Вставка значень у дерево
for value in values:
    root = insert(root, value)

# Виведення дерева у зручному форматі
print("Дерево:")
print_tree(root)

# Виконання Завдання 1: Знаходимо максимальне значення у дереві
max_value = find_max_value(root)
print("Максимальне значення у дереві:", max_value)

# Виконання Завдання 2: Знаходимо мінімальне значення у дереві
min_value = find_min_value(root)
print("Мінімальне значення у дереві:", min_value)

# Виконання Завдання 3: Знаходимо суму всіх значень у дереві
total_sum = sum_of_values(root)
print("Сума всіх значень у дереві:", total_sum)
