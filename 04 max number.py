number = int(input('Ведите число для которого хотите узнать самую большую цифру '))
# print(max(list(str(number))))
maxNum = 0

while number > 10:
    check = number % 10
    number //=10
    if check > maxNum:
        maxNum = check

print(maxNum)
