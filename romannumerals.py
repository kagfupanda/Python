def roman(num, one, five, ten):
    four = one+five
    nine=one+ten
    romanNumeralMap = (('M',1000),
                       ('CM',900),
                       ('D',500),
                       ('CD',400),
                       ('C',100),
                       ('XC',90),
                       ('L',50),
                       ('XL',40),
                       (ten,10),
                       (nine,9),
                       (five, 5),
                       (four, 4),
                       (one, 1))
    result=''
    
    if num < 1 or num > 9:
        return ''
    else:
        for numeral, integer in romanNumeralMap:
            while num >= integer:
                result += numeral
                num -= integer
        return result

def roman_num(num):
    romanNumeralMap = (('M',1000),
                       ('CM',900),
                       ('D',500),
                       ('CD',400),
                       ('C',100),
                       ('XC',90),
                       ('L',50),
                       ('XL',40),
                       ('X',10),
                       ('IX', 9),
                       ('V',  5),
                       ('IV', 4),
                       ('I',  1))
    result=''
    
    if num < 1 or num > 9999:
        return ''
    elif num >=1 and num <= 9:
        return(roman(num, 'I','V','X'))
    else:
        for numeral, integer in romanNumeralMap:
            while num >= integer:
                result += numeral
                num -= integer
        return result

if __name__=="__main__":
    print ("Roman Number Generator. Enter 0 to quit.")
    while True:
        num = int(input("Enter a number between 1 and 9,999:\n"))
        if (num == 0):
            break
        print("Roman Numerals: " + roman_num(num))

    print("Roman Numerals: ")  
    print ("Bye.")
