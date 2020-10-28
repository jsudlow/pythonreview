def c_to_f(degree):
    return 32+ (degree*9.0)/5.0


if __name__ == "__main__":
    print('This program converts the temperature in Celsius to Fahrenheit.')
    start=int(input('Enter start: \n'))
    end=int(input('Enter end: \n'))
    end += 1
    increment=int(input('Enter the degree increments: '))
    print('Celsius | Fahrenheit')
    print('--------------------')

    for degree in range(start,end,increment):
        f_temp=round(c_to_f(degree),1)
        print('{:<8d}{:>s} {:>3.1f}'.format(degree,'|',f_temp))
    print('--------------------')