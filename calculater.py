# calculate 2 numbers by function
# halfway

def plus(str1,str2,num2calc = {}):
    num2calc[str1,str2] = str1+str2
    return num2calc

def minus(str1,str2,num2calc = {}):
    num2calc[str1,str2] = str1-str2
    return num2calc


def multiple(str1,str2,num2calc = {}):
    num2calc[str1,str2] = str1*str2
    return num2calc


def divide(str1,str2,num2calc = {}):
    num2calc[str1,str2] = str1/str2
    return num2calc


def main():
    first_number = input('-->')
    second_number = input('-->')
    first_number = float(first_number)
    second_number = float(second_number)
    
    
    print(plus(first_number,second_number))
    print(minus(first_number,second_number))
    print(multiple(first_number,second_number))
    print(divide(first_number,second_number))


if __name__ == '__main__':
    main()

