def is_6k_1(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

n = int(input("Enter "))
print("Prime till", n, "are:")
for i in range(2, n + 1):
    if is_6k_1(i):
        print(i)
