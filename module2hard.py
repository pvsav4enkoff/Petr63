def get_result(num):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = []
    for i in range(num):
        for j in range(num):
            if numbers[i] < numbers[j]:
                if (num % (numbers[i]+numbers[j]) == 0 and (num / (numbers[i]+numbers[j])) != 1) or (numbers[i]+numbers[j]) % num == 0:
                    result.append(str(numbers[i]))
                    result.append(str(numbers[j]))
    return result

num = 3
while num >= 3 and num <= 20:
    num = int(input("Введите число от 3 до 20: "))
    print(f'Для: {num} password: {"".join(get_result(num))}')

print('Число должно быть от 3 до 20')