#
namber= 305678149569923
namber_0 = 0
namber_1 = 0
namber_2 = 0
namber_3 = 0
namber_4 = 0
namber_5 = 0
namber_6 = 0
namber_7 = 0
namber_8 = 0
namber_9 = 0
for i in str(namber):
    if i =='0':
        namber_0 += 1
    elif i == '1':
        namber_1 += 1
    elif i == '2':
        namber_2 += 1
    elif i == '3':
        namber_3 += 1
    elif i == '4':
        namber_4 += 1
    elif i == '5':
        namber_5 += 1
    elif i == '6':
        namber_6 += 1
    elif i == '7':
        namber_7 += 1
    elif i == '8':
        namber_8 += 1
    elif i == '9':
        namber_9 += 1
if namber_9 > 0:
    print('Цифра - 9 максимальная в числе', namber)
elif namber_8 > 0:
    print('Цифра - 8 максимальная в числе', namber)
elif namber_7 > 0:
    print('Цифра - 7 максимальная в числе', namber)
elif namber_6 > 0:
    print('Цифра - 6 максимальная в числе', namber)
elif namber_5 > 0:
    print('Цифра - 5 максимальная в числе', namber)
elif namber_4 > 0:
    print('Цифра - 4 максимальная в числе', namber)
elif namber_3 > 0:
    print('Цифра - 3 максимальная в числе', namber)
elif namber_2 > 0:
    print('Цифра - 2 максимальная в числе', namber)
elif namber_1 > 0:
    print('Цифра - 1 максимальная в числе', namber)
elif namber_0 > 0:
    print('Цифра - 0 максимальная в числе', namber)




