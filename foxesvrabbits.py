import math
def bunnies(rabbit, fox, years):
    prev_R = rabbit
    prev_F = fox
    R=rabbit
    F=fox
    i=0
    result = [0,0]
    A = 0.04
    B = 0.0005
    G = 0.2
    S = 0.00005
    
    while (i<years):
        R = prev_R + math.floor(prev_R *(A-B*prev_F))
        F = prev_F - math.floor(prev_F*(G-S*prev_R))
        prev_R = R
        prev_F = F
        i=i+1
        
    result[0] = R
    result[1] = F
    #print("OK:" + str(result[0]) + "F:" + str(result[1]))
    return(result)
           
#You do not need to make changes below this line.
if __name__=="__main__":
    print ("Welcome to Predator-Prey Model.")
    rabbit=int(input("Enter Initial Rabbit Population:\n"))
    fox=int(input("Enter Initial Fox Population:\n"))
    years=int(input("Enter Number of Years to Simulate:\n"))

    res = [0,0]
    res = bunnies(rabbit,fox,years)

    if (years >=0):
        print ("After " + str(years) + " years there will be " + str(res[0]) + " rabbits.")
        print ("After " + str(years) + " years there will be " + str(res[1]) + " foxes.")
    else :
        print ("Invalid years entered")
