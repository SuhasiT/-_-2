import random
import string
def main():
    len = int(input("enter length of password: "))
    lowc = string.ascii_lowercase
    #print(lowc) for checking
    uppc = string.ascii_uppercase
#print(uppc) for verify
    digitd = string.digits
    symb=string.punctuation
    #print(symb)
    combine = lowc + uppc + digitd + symb
    r = random.sample(combine,len)
#print(r)
    paswd ="".join(r)
    print(paswd)
    main()
main()






