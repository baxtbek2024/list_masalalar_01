#1-masala
roy1 = [2, 3, 4, 5, 6]
roy2 = [4, 3, 2, 5, 8]
new = []

for i in roy1 + roy2:
    if i not in new:
        new.append(i)


new.sort()
print(new)
#2-masala
roy = [13, 20, 33, 40, 5, 69]
juft = []
toq = []

for i in range(len(roy)):
    if i % 2 == 0:
        juft.append(roy[i])
    else:
        toq.append(roy[i])

print(juft)
print(toq)

#3-masala
lst = [1, 1, 2, 2, 2, 3, 1]
natija = []

son = lst[0]
count = 1

for i in range(1, len(lst)):
    if lst[i] == son:
        count += 1
    else:
        natija.append((son, count))
        son = lst[i]
        count = 1

natija.append((son, count))
print(natija)

#4-masala

roy = [22, 3, 443, 32]
eng_katta = max(roy)
eng_kichik = min(roy)

roy.remove(eng_kichik)
roy.remove(eng_katta)

farq = max(roy) - min(roy)
print(farq)
