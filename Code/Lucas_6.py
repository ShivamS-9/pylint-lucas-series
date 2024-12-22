"""
This is code for q1b
"""
def cal(val_n):
    """
    Docstring for the function
    """
    l_0 = -3
    l_1 = -1
    if val_n == 0:
        return l_0
    elif val_n == 1:
        return l_1
    ln_minus_2 = l_0
    ln_minus_1 = l_1
    for i in range(2, val_n + 1):
        l_n = ln_minus_1 + ln_minus_2
        ln_minus_2 = ln_minus_1
        ln_minus_1 = l_n
    return l_n
val_n_2 = int(input())
if val_n_2 <= 1 or val_n_2 >= 1000001:
    print("Error: n out of range. Input value between 1 and 1000001 ")
else:
    RESULT = cal(val_n_2)
    print(f"L{val_n_2} = {RESULT}")
    