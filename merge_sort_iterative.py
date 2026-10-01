def merge_sort_iterative(a):
    n = len(a)
    comparisons = 0
    assignments = 0
    i = 1 # Початковий розмір підмасивів (починаємо з 1 елемента)
    
    # Зовнішній цикл: збільшуємо розмір підмасивів вдвічі на кожному кроці
    while i < n:
        j = 0
        # Внутрішній цикл: проходимо по масиву та зливаємо сусідні підмасиви
        while j < n - i:
            left = j
            mid = j + i
            # min() гарантує, що ми не вийдемо за межі масиву наприкінці
            right = min(j + 2 * i, n) 
            
            # Виклик допоміжної функції для злиття
            c, a_count = merge(a, left, mid, right)
            comparisons += c
            assignments += a_count
            j += 2 * i # Перехід до наступної пари підмасивів
        i *= 2 # Подвоєння розміру підмасиву для наступної ітерації
    return a, comparisons, assignments

def merge(a, left, mid, right):
    comparisons = 0
    assignments = 0
    n1 = mid - left
    n2 = right - mid
    
    # Створюємо тимчасові підмасиви для лівої та правої частини
    L = a[left:mid]
    R = a[mid:right]
    assignments += n1 + n2
    
    it1 = 0 # Індекс для лівого підмасиву
    it2 = 0 # Індекс для правого підмасиву
    k = left # Індекс для основного масиву
    assignments += 2 
    assignments += 1 
    
    # Основний цикл злиття: порівнюємо елементи і записуємо менший в основний масив
    while it1 < n1 and it2 < n2:
        comparisons += 1
        if L[it1] < R[it2]:
            a[k] = L[it1]
            it1 += 1
            assignments += 1
        else:
            a[k] = R[it2]
            it2 += 1
            assignments += 1
        k += 1
        assignments += 1
        
    # Додаємо елементи, що залишилися в лівому підмасиві (якщо такі є)
    while it1 < n1:
        a[k] = L[it1]
        it1 += 1
        k += 1
        assignments += 1
        
    # Додаємо елементи, що залишилися в правому підмасиві (якщо такі є)
    while it2 < n2:
        a[k] = R[it2]
        it2 += 1
        k += 1
        assignments += 1
        
    return comparisons, assignments

# Приклад використання для Варіанту 15
my_list = [50, 80, 19, 86, 35, 7, 60, 48, 51]
print("Оригінальний список:", my_list)
sorted_list, comps, assigs = merge_sort_iterative(my_list.copy())
print("Відсортований список:", sorted_list)
print(f"Кількість порівнянь: {comps}")
print(f"Кількість присвоювань: {assigs}")

