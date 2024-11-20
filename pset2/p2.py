intrate = 0.2/12
fixpay = 50
balance = 4773

while balance > 0:
    balance = 4773
    for n in range(12):
        unpaybal = balance - fixpay
        intamt = intrate * unpaybal
        balance = unpaybal + intamt
    fixpay += 10

print(f"amount to pay to clear loan after a year: {fixpay}")
    