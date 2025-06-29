yosh = int(input("Yoshingizni kiriting: "))
narx = 100_000

if yosh <= 7:
    chegirma = 50
elif yosh >= 60:
    chegirma = 30
else:
    chegirma = 0

yakuniy_narx = narx - (narx * chegirma / 100)
print(f"Yakuniy narx: {int(yakuniy_narx)} so'm ({chegirma}% chegirma qo'llanildi)")