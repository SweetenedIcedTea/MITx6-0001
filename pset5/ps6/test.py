import string

dic = {}
lowerletters = list(string.ascii_lowercase)
upperletters = list(string.ascii_uppercase)

for i in range(len(lowerletters)):
    if i + shift >= len(lowerletters):
        dic[lowerletters[i]] = lowerletters[abs(len(lowerletters) - (i + shift))]
        dic[upperletters[i]] = upperletters[abs(len(upperletters) - (i + shift))]
    else:
        dic[lowerletters[i]] = lowerletters[i + shift]
        dic[upperletters[i]] = upperletters[i + shift]

print(dic)