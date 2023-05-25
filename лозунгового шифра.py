# Лозунговый шифр
alphabet = "Арсамаков"


def Losung(main_string):
    lst = []
    res1 = ""
    res2 = []

    for i in range(len(main_string)):
        lst.append(main_string[i])
    for i in lst:
        if res1.find(i) == -1:
            res1 += i
    res1 += alphabet
    for i in range(len(res1)):
        res2.append(res1[i])
    res1 = ""
    for i in res2:
        if res1.find(i) == -1:
            res1 += i
    return res1


def Encrypt(res_string):
    res = ""
    losung = Losung(s)
    for i in range(len(res_string)):
        for j in range(len(alphabet)):
            if alphabet[j] == res_string[i]:
                res += losung[j]
    return res


s = input()
string = input()
s = s.lower()
s = ''.join(s.split())
string = string.lower()
string = ''.join(string.split())

print(Losung(s))
print(Encrypt(string))