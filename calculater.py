# calculate 2 numbers by function

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
    target_number = float(input('-->'))
    cal_symbol = float(input('what kind of calculation do you want?')
    calculation_number = float(input('-->'))
    
    
    if(cal_symbol=='+'):
        print(plus(target_number,calculation_number))
    elif(cal_symbol=='-'):
        print(minus(target_number,calculation_number))
    elif(cal_symbol=='-'):
        print(multiple(target_number,calculation_number))
    elif(cal_symbol=='-'):
        print(divide(target_number,calculation_number))
    else:
        print('error!')
                       


if __name__ == '__main__':
    main()

