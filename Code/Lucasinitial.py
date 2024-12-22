def cal(n):
    L_0 = -3
    L_1 = -1

    if n == 0:
        return L_0
    elif n == 1:
        return L_1
    
    Ln_minus_2 = L_0
    Ln_minus_1 = L_1
    for i in range(2, n + 1):
        Ln = Ln_minus_1 + Ln_minus_2
        Ln_minus_2 = Ln_minus_1
        Ln_minus_1 = Ln
    return Ln

n = int(input())

if n <= 1 or n >= 1000001:
    print("Error: n out of range. Input value between 1 and 1000001 ")
else:
    result = cal(n)
    print(f"L{n} = {result}")
