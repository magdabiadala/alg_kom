### program tworzący wektor charakterystyczny dla podanego podzbioru oraz zwracający dla niego wartość funkcji pozycyjnej ###

input_string = input("Enter a subset of numbers separated by space:")
subset = input_string.split()
subset_len = int(len(subset))
for i in range(subset_len):
    subset[i] = int(subset[i])
bridge = []
# print(subset)

# przypadek otrzymania zbioru pustego
if subset_len == 0:
    rank = 0
else:
    subset_max = int(max(subset))

    # tworzenie pomostu o długości równej największemu elementowi pozbioru
    i = 0
    while i < subset_max:
        bridge.append(0)
        i+=1
    # print(bridge)

    # kodowanie kolejnych elementów podzbioru w pomoście
    i = 0
    while i < subset_len:
        el = subset[i]
        i+=1
        bridge[subset_max - el] = 1
    # print(bridge)

    #liczę rangę (przeliczam binarny pomost na liczbę dziesiętną)
    i = subset_max-1
    power = 0
    rank = 0
    while power < subset_max:
        bin = bridge[i]
        if bin ==1:
            rank += 2**power
        power+=1
        i -= 1

print(rank)
