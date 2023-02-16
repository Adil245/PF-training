def prime():
    p = int(input('Enter a number: '))
    for i in range(2,p):
        if p%i==0:
            return -1
    else:
        tot =0
        for i in range(p + 1):
            tot = tot+i
        return 'Number is Prime \nIts sum is ' + str(tot)

print(prime())