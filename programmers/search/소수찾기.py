import itertools

def prime(number):
    if number != 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return False


def solution(numbers):
    arr = [i for i in numbers]
    primes = []
    for i in range(1, len(arr)+1):
        p = itertools.permutations(arr, i) # 튜플로 반환
        for pp in p:
            result = int(''.join(pp))
            if result != 0:
                if prime(result):
                    primes.append(result)

    return len(list(set(primes)))



print(solution("17"))
print(solution("011"))
