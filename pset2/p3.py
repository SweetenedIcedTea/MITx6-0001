intrate = 0.2/12
balance = 320000
upb = (balance * (1+intrate)**12) / 12.0
lowb = balance / 12

while round(balance, 2) != 0:
    balance = 320000
    fixpay = (upb + lowb) / 2
    for n in range(12):
        unpaybal = balance - fixpay
        intamt = intrate * unpaybal
        balance = unpaybal + intamt
    if balance > 0:
        lowb = fixpay
    elif balance < 0:
        upb = fixpay

print(f"amount to pay to clear loan after a year: ${fixpay:.2f}")