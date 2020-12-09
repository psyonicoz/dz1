time = int(input('Ведите время в секундах '))
hours = time // 3600
minutes = time % 3600 // 60
seconds = time % 3600 % 60

if hours >= 1:
    print(f'{hours:02}:{minutes:02}:{seconds:02}')
elif minutes >= 1:
    print(f'{minutes:02}:{seconds:02}')
else:
    print(f'{seconds:02}')
