number = int(input('Ведите любое число '))
scale = (10**(len(str(number))))
#print(number + (number*scale + number) + (number*scale**2 + number*scale + number))
print(3*number + 2*number*scale + number*scale**2)
