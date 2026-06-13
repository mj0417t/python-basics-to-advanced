x=int(input("Enter a number: "))
def printIncreasingPower(x):
    #code here
    # Loop to jump in powers of 2
    i=1
    while(True):
        #code here
        num=i*i;
        if(num>x):
            break
        print (num, end = " ")
        i=i+1
printIncreasingPower(x)