print("Числа от 1 до 50:")
for i in range(1, 51):
    print(i, end=' ')
print("\n")

print("Чётные числа от 2 до 50:")
for i in range(2, 51, 2):
    print(i, end=' ')
print("\n")

total_sum = 0
for i in range(1, 101):
    total_sum += i
print(f"Сумма чисел от 1 до 100: {total_sum}\n")
    
print("числа от 100 до 1:")
for i in range(100, 0, -1):
    print(i, end=' ')
print("\n")

count_div3 = 0
print("Числа делящиеся на 3:")
for number in range (1,31):
    if number % 3 == 0:
        print(number, end=' ')
        count_div3 += 1
print(f"\nКоличество чисел от 1 до 30, делящихся на 3: {count_div3}")

squares = []
for i in range(1, 11):
    squares.append(i*i)
print(f"Список квадратов: {squares}")