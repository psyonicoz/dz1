proceeds = int(input('Ведите значение выручки '))
costs = int(input('Ведите значение издержек '))
rentability = (((proceeds - costs) / proceeds) * 100)

if proceeds > costs:
    print(f'Фирма в прибыли, рентабельнось {rentability:.0f}%')
    employees = int(input('Введите колличество сотрудников '))
    personal = ((proceeds - costs) / employees)
    print(f'Прибыль фирмы в расчете на одного сотрудника:  {personal:.0f} условных единиц.')
else:
    print('Фирма в убытке')
