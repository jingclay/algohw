def homework_easy_way(n):
    return sum(range(1, n + 1))


def homework_hard_way(n):
    answer = 0
    while n:
        answer += n
        n -= 1
    return answer


def max_easy(numbers):
    return max(numbers)


def max_hard(numbers):
    answer = 0
    for n in numbers:
        if n > answer:
            answer = n
    return answer


def count_digits(number):
    odd_count = 0
    even_count = 0

    for num in str(number):
        if int(num) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f'{odd_count=} {even_count=}')


my_answer = homework_easy_way(8)
print(my_answer)

my_answer = homework_hard_way(8)
print(my_answer)

print(max_easy([1, 7, 9, 3]))
print(max_hard([1, 7, 9, 3]))

count_digits(423740)
