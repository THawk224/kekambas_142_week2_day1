# Exercise 1 codes copy and pasted from Jupyter Notebooks

for i in range(1, 1000):
    cube = i ** 3
    if cube > 1000:
        break
    print(cube)

# Exercise 2 codes copy and pasted from Jupyter Notebooks

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)

# Exercise 3 codes copy and pasted from Jupyter Notebooks

age = int(input("Enter your age: "))

if age < 18:
    print("Kids")
elif age >= 18 and age <= 65:
    print("Adults")
else:
    print("Seniors")