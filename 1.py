import random
from timeit import timeit
import matplotlib.pyplot as plt

def randomized_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

def deterministic_quick_sort(arr):
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо опорний елемент (перший елемент)
    pivot = arr[0]

    # Розділяємо масив на частини
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def run_with_timer(arr):
    randomized_time = timeit(lambda: deterministic_quick_sort(arr), number=10)
    deterministic_time = timeit(lambda: deterministic_quick_sort(arr), number=10)

    print(f'Розмір масиву: {len(arr)}')
    print(f'    Рандомізований QuickSort: {randomized_time:.4f} секунд')
    print(f'    Детермінований QuickSort: {deterministic_time:.4f} секунд')

    return randomized_time, deterministic_time

def show_results(results):
    sizes, randomized_times, deterministic_times = zip(*results)

    plt.figure(figsize=(10, 5))
    plt.plot(sizes, randomized_times, label='Рандомізований QuickSort', marker='o')
    plt.plot(sizes, deterministic_times, label='Детермінований QuickSort', marker='x')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час (секунди)')
    plt.title('Порівняння часу виконання QuickSort')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == '__main__':
    # Тестування з різними розмірами масиву
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = []

    for size in sizes:
        arr = [random.randint(0, 100000) for _ in range(size)]
        randomized_time, deterministic_time =run_with_timer(arr)
        results.append((size, randomized_time, deterministic_time))

    show_results(results)