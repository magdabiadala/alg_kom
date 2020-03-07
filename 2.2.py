#generuje podzbiory długości n w porządku minimalnych zmian (kod Gray'a)

n = int(input("Enter n:"))

#pierwszy podzbiór
bin = []
for i in range(n):
    bin.append(0)
print(bin)

if n != 0:
    for i in range(2**(n-1)-1):
        if bin[n-1] == 1:
            bin[n-1] = 0
        else:
            bin[n-1] = 1
        print(bin)

        bin.reverse()
        ind = bin.index(1)
        if bin[ind+1] == 1:
            bin[ind+1] = 0
        else:
            bin[ind+1] = 1
        bin.reverse()
        print(bin)
        
    #ostatni podzbiór
    if bin[n-1] == 1:
        bin[n-1] = 0
    else:
        bin[n-1] = 1
    print(bin)
