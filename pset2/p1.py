balance = 5000
minpay = 0.02
intrate = 0.18/12

for n in range(13):
    print(f"month {n}: ${balance:.2f}")
    minamt = balance * minpay
    unpaybal = balance - minamt
    intamt = intrate * unpaybal
    balance = unpaybal + intamt