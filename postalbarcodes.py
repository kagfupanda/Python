list = ["||:::",
        ":::||",
        "::|:|",
        "::||:",
        ":|::|",
        ":|:|:",
        ":||::",
        "|:::|",
        "|::|:",
        "|:|::"
        ]   
def checksum(zip):
    num=0
    for c in zip:
        if c.isdigit():
            num = num + int(c)
    myMod = num%10
    if myMod==0:
        return(str(myMod))
    else:
        return(str(10-myMod))

def barcode(zip):
    res=''
    for c in zip:
        if c.isdigit():
            res=res+str(list[int(c)])
    num = int(checksum(zip))
    if num >=0 and num <=9:
        res = res + str(list[int(num)])
    res="|"+res+"|"
    return(res)
    
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
    
if __name__=="__main__":
    print ("Welcome to Bar Code Generator")
    while True:
        text = input("Enter Zip Code (exit to quit):\n")
        if text=='exit':
            break
        if is_number(text):
            print("Bar Code:\n" + barcode(text))
        else:
            continue

    print("Thanks for using me.") 
