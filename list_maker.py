import random

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_random_prime_list(size):
    prime_list = []
    while len(prime_list) < size:
        num = random.randint(1, 100000)  # 범위를 조정하여 원하는 수의 소수 리스트를 생성할 수 있습니다.
        if is_prime(num):
            prime_list.append(num)
    return prime_list

# 예제 사용
random_prime_list = generate_random_prime_list(10000)
print(random_prime_list)
