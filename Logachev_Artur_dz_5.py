src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
b = []

for i in src:
    if i not in b:
        b.append(i)

print(b) 
# никак не могу понять, как получить результат в методичке

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print([x for x in src if src.count(x) == 1])
