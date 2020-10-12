import statistics

def median(a,b,c):
    numlist = [a,b,c]
    median = statistics.median(numlist)
    print('The median is', median)
    return median
    
def main():
    print('This Program finds the median value of three numbers entered by the user.')
    num1 = int(input('Input first number:\n'))
    num2 = int(input('Input second number:\n'))
    num3 = int(input('Input third number:\n'))
    median(num1,num2,num3)




if __name__ == "__main__": 

    main()
    