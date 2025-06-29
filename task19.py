letters = ["h", "e", "l", "l", "o", "w", "O", "r", "l", "d"]
unlilar = {'a', 'e', 'i', 'o', 'u'}
sana = 0

for harf in letters:
    if harf.lower() in unlilar:
        sana += 1

print(sana)