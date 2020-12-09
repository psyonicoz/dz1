firstRes = int(input('Введите количество километров пройденное в первый день '))
desiredRes = int(input('Ведите желаемый результат в километрах '))
daysCount = 1

while desiredRes > firstRes:
    firstRes = (firstRes + firstRes * 0.1)
    daysCount += 1
    if firstRes > desiredRes:
        print(f'На {daysCount} день спортсмен достигнет результата — не менее {firstRes:.0f} км')
