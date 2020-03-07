#znajduje podzbiór dla danej rangi i zbioru bazowego

rank = int(input("Enter rank:"))
input_string = input("Enter a set of numbers separated by space:")
set = input_string.split()
l = len(set)

#przypadek gdy podana ranga jest za duża
if rank > (2**l)-1:
    print("Subset with given rank does not exist")
else:
    subset = []
    el = 1
    while rank > 0:
        if rank % 2 == 1:
            subset.append(el)
        rank = rank // 2
        el +=1
    print(subset)
