"""
This is code for q1b
"""
def cal(val_n):
    """
    Docstring for the function
    """
    L_0 = -3
    L_1 = -1
    if val_n == 0:
        return L_0
    elif val_n == 1:
        return L_1
    Ln_minus_2 = L_0
    Ln_minus_1 = L_1
    for i in range(2, val_n + 1):
        Ln = Ln_minus_1 + Ln_minus_2
        Ln_minus_2 = Ln_minus_1
        Ln_minus_1 = Ln
    return Ln
val_n_2 = int(input())
if val_n_2 <= 1 or val_n_2 >= 1000001:
    print("Error: n out of range. Input value between 1 and 1000001 ")
else:
    result = cal(val_n_2)
    print(f"L{val_n_2} = {result}")
