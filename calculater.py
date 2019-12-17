# calculate 2 numbers by function
# halfway

def plus(str1,str2,num2calc = {}):
    str1 = float(str1)
    str2 = float(str2)
    num2calc[str1,str2] = str1+str2
    return num2calc

def minus(str1,str2,num2calc = {}):
    str1 = float(str1)
    str2 = float(str2)
    num2calc[str1,str2] = str1-str2
    return num2calc


def multiple(str1,str2,num2calc = {}):
    str1 = float(str1)
    str2 = float(str2)
    num2calc[str1,str2] = str1*str2
    return num2calc


def cut(str1,str2,num2calc = {}):
    str1 = float(str1)
    str2 = float(str2)
    num2calc[str1,str2] = str1/str2
    return num2calc


def main():
    first_number = input('-->')
    second_number = input('-->')
    #first_number and second_number is str


    #list->dictionary
    addition = plus(first_number,second_number)
    subtraction = minus(first_number,second_number)
    multiplication = multiple(first_number,second_number)
    division = cut(first_number,second_number)
    print(division)


if __name__ == '__main__':
    main()

