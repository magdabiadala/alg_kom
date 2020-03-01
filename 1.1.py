print("Podaj n > 0: ")
n = int(input())
print("Podaj k > 0: ")
k = int(input())
list = []
#tworzenie pierwszego ciągu
i = k
while i > 0:
    list.append(1)
    i -= 1
print(list)
# tworzenie reszty
eol = k-1
k = k-1

while k >= 0:
    # znajdź element który możesz zwiększyć
    if list[k] == n:
        k -= 1
    else:
        # zwiększ go
        list[k] += 1
        # wyjedynkuj pozostałe
        i = k+1
        while i <= eol:
            list[i] = 1
            i +=1
        # wróć k na koniec listy
        k = eol
        print(list)
