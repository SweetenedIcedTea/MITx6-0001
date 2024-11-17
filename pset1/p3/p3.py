def main(s: str)->None:
    print("Longest substring in alphabetical order for ", s, " is: ", sub(s))

def sub(s: str)->str:
    res = ""
    if s == res:
        return res
    temp = [s[0]]
    for i in range(1, len(s)):
        if ord(temp[-1]) > ord(s[i]): # prev char is bigger than curr char
            if len(res) < len(temp): # if res is smaller than temp (replace)
                res = ''.join(temp)
            temp = []
        temp.append(s[i])
    
    if len(res) < len(temp):
        res = ''.join(temp)
        
    return res

if __name__ == "__main__":
    main("azcbobobegghakl")
    main("abcbcd")
    main("abcbcd")
    main("abcde")
    main("zyxwvutsrqponmlkjihgfedcba")