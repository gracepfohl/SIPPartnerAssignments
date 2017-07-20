random_numbers = [29, 68, 69, 30, 20, 91, 62, 28, 36, 67, 40, 71, 71, 82, 71, 84, 96, 34, 40, 92, 57, 56, 86, 63, 88, 79, 48, 22, 12, 74,
86, 54, 94, 19, 73, 25, 23, 72, 74, 56,53, 52, 55, 10, 37, 48, 82, 84, 57, 45, 85, 48, 58, 56, 95, 21, 47, 98, 71, 38, 24, 51, 28, 71,
52, 33, 78, 78, 77, 24,17, 31, 85, 87, 86, 63, 23, 73, 40, 64, 35, 29, 10, 43, 99, 38, 63, 61, 76, 91, 64, 48, 23, 26, 19, 21, 17, 49, 15, 62]


def DivisibleByFive():
    for number in random_numbers:
        if number%5 == 0:
            print (number)
def DivisibleByThree ():
    for number in random_numbers:
        if number%3 ==0:
            print (number)

def DivisibleBy3and5(random_numbers):
    for number in random_numbers:
        if (number%3 == 0 and number%5 == 0):
            x = x + number
            print (x)

# global x
# DivisibleBy3and5(random_numbers)


total = 0
multiples = []
for number in random_numbers:
    if (number % 5 == 0 and number % 3 == 0):
        multiples.append(number)
        total = total + number
print(total)

# print ("These numbers are divisible by 5.")
# DivisibleByFive()
# print ("These numbers are divisible by 3 and 5.")
