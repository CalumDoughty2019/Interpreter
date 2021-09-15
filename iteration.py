# while loop

#1
n = 10
while n > 0:
    print(n)
    n = n - 1
print("Blast off!")
print()

#2
num = int(input("Enter a whole number: "))
while num > 1:
    print("%d" % num, end=" ")
    num = int(num / 2)
print("\n")
print()

#3
for number in range(10):
    print("12 x", number, "= ", 12 * number)
print("That was the last one... Phew! \n")
print()

#4
for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, '\t', end="")
    print()
print("Finished")
print()

#5
total = 0
for count in range(1, 6):
    new_number = int(input("Enter a number: "))
    total = total + new_number
average = total / count
print("The average is: ", average, "\n")

#6
for number in range(2, 12, 2):
    print("12 x", number, "= ", 12 * number)
print("That was the last one... Phew! \n")