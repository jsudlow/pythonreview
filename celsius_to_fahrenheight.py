def c_to_f(celsius):
    fahrenheit = (celsius * 1.8)+32

    print('The temperature entered in Celsius is ' + str(celsius))
    print('The temperature in Fahrenheit is ' + str(fahrenheit) + '\n')
    return fahrenheit



celsius = float(input('Enter the temperature in Celsius:\n'))
c_to_f(celsius)
