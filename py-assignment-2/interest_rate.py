savings = int(input("Enter your savings: "))
months = 12
initialSavings = 1000000

parseSavings = int(savings)


for result in range(months):
    interest = 2 / 100
    parseSavings = parseSavings + (parseSavings * interest)
    print("Nilai untuk bulan ke ",result + 1)

print("nilai Tabungan awal : ", int(initialSavings))
print("nilai tabungan setelah 1 tahun", int(parseSavings))