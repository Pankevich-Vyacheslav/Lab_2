def merge_sort_recursive(arr):
    comparisons = 0
    assignments = 0
    recursive_calls = 1 # Рахуємо поточний виклик функції
    
    # Базовий випадок рекурсії: масив з 0 або 1 елемента вже відсортований
    if len(arr) <= 1:
        return arr, comparisons, assignments, recursive_calls
        
    mid = len(arr) // 2 # Знаходимо середину масиву
    assignments += 1
    
    # Рекурсивно ділимо ліву та праву половини
    left_half, c1, a1, r1 = merge_sort_recursive(arr[:mid])
    right_half, c2, a2, r2 = merge_sort_recursive(arr[mid:])
    
    comparisons += c1 + c2
    assignments += a1 + a2
    recursive_calls += r1 + r2
    
    # Зливаємо дві відсортовані половини
    merged_arr, c_merge, a_merge = merge(left_half, right_half)
    comparisons += c_merge
    assignments += a_merge
    
    return merged_arr, comparisons, assignments, recursive_calls

def merge(left, right):
    merged_arr = [] # Новий масив для результату злиття
    comparisons = 0
    assignments = 0
    i = 0 # Індекс лівого масиву
    j = 0 # Індекс правого масиву
    
    # Порівнюємо елементи з обох масивів та додаємо менший до результату
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] <= right[j]:
            merged_arr.append(left[i])
            i += 1
        else:
            merged_arr.append(right[j])
            j += 1
        assignments += 1
        
    # Додаємо всі елементи, що залишилися в лівому масиві
    while i < len(left):
        merged_arr.append(left[i])
        i += 1
        assignments += 1
        
    # Додаємо всі елементи, що залишилися в правому масиві
    while j < len(right):
        merged_arr.append(right[j])
        j += 1
        assignments += 1
        
    return merged_arr, comparisons, assignments

# Приклад використання для Варіанту 15
my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
print("Оригінальний список:", my_list)
sorted_list, total_comparisons, total_assignments, total_recursive_calls = merge_sort_recursive(my_list)
print("Відсортований список:", sorted_list)
print(f"Загальна кількість порівнянь: {total_comparisons}")
print(f"Загальна кількість присвоювань: {total_assignments}")
print(f"Загальна кількість рекурсивних викликів: {total_recursive_calls}")

