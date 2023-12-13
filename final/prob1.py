def frequency_analytic(s):
    dic = {}
    for i in s:
        if i in dic:
            dic[i] += 1
        else :
            dic[i]= 1
    print(dic)

if __name__ == "__main__":
    s = input('input your message : ')
    frequency_analytic(s)
