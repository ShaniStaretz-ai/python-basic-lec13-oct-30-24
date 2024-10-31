# ex a:
students: int = int(input("enter total number of students:"))
students_per_class = 30
print(
    f"there are full {students // students_per_class} classes and 1 class with {students % students_per_class} students ")

# ex b
number: int = 0
while True:
    try:
        number = int(input("enter number in range (10,99):"))
        if not 10 <= number <= 99:
            raise ValueError("not in range")
        break
    except ValueError as e:
        print(f"ERROR- invalid number:{e},try again")
print("reverse number:", number % 10 * 10 + number // 10)

# ex c
print("prime numbers in range (1,200):")
for x in range(1, 200):
    if x < 2:
        continue;
    elif x == 2:
        print(x, end=" ")
        continue;
    elif x % 2 == 0:
        continue
    is_prime: bool = True
    divider = 3
    while divider <= (x ** 0.5 + 1):
        # for divider in range(2,x**0.5+1):

        if x % divider == 0:
            is_prime = False
            break
        divider += 2
    if is_prime:
        print(x, end=" ")

# ex d:
from hw.my_func import get_answer_char_by_index, get_answer_index_by_char

SENTINEL: str = 'x'
results: list[int] = [0] * 4  # [a,b,c,d]
while True:
    answer = input("enter your answer (a,b,c,d), if you want to stop enter x:")
    if answer == SENTINEL:
        print("goodbye")
        break
    if answer not in ['a', 'b', 'c', 'd']:
        print("not an option")
        continue
    results[get_answer_index_by_char(answer)] += 1

for i in range(len(results)):
    print(f"{results[i]} students selected answer {get_answer_char_by_index(i)} ")

print(f"most students answer {get_answer_char_by_index(results.index(max(results)))}")
print(f"least students answer {get_answer_char_by_index(results.index(min(results)))}")
