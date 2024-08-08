numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
primes = []
not_primes = []
is_prime = True
for i in range(2, 21):
    k = 0
    for j in range(1, len(numbers)):
        if i % numbers[j] == 0:
            k += 1
        if j > i:
            break

    if k == is_prime:
        primes.append(numbers[i - 1])
    else:
        not_primes.append(numbers[i - 1])

print(primes)
print(not_primes)
