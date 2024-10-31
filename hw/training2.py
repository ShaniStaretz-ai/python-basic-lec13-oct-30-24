# ex a:
students: int = int(input("enter total number of students:"))
students_per_class: int = 30
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
    divider: int = 3
    while divider <= (x ** 0.5 + 1):
        if x % divider == 0:
            is_prime = False
            break
        divider += 2
    if is_prime:
        print(x, end=" ")

# ex d:

SENTINEL: str = 'x'
results: list[int] = [0] * 4  # [a,b,c,d]
options = ['a', 'b', 'c', 'd']
while True:
    answer = input("enter your answer (a,b,c,d), if you want to stop enter x:").lower()
    if answer == SENTINEL:
        print("goodbye")
        break
    if answer not in ['a', 'b', 'c', 'd']:
        print("not an option")
        continue
    results[options.index(answer)] += 1

for i in range(len(results)):
    print(f"{results[i]} students selected answer {options[i]} ")

print(f"most students answer {options[results.index(max(results))]}")
print(f"least students answer {options[results.index(min(results))]}")
