def rev(text1):
    return(text1[::-1])

def reverse_number(text):
    str=''
    res=''
    flag=False
    for s in text:
        if s.isdigit():
            str = str + s
            flag = True
        else:
            flag=False
            if (len(str)>0):
                res=res+rev(str) + s
                str = ''
            else:
                res = res + s
    
    if (flag==True and len(str)>0):
        res=res+rev(str)
    
    return(res)
    
if __name__=="__main__":
    print ("Welcome to Digit Flipper")
    text = input("Enter Some Text:\n")
    text1 = reverse_number(text)
    print ("Revised String:")
    print (text1)
