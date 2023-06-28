def ans(num : list) -> int:
    if len(num) < 2:
        return 0
    p = 0
    m = num[0]
    for price in num[1:]:
        m = min(m, price)
        profit = price - m
        p = max(p, profit)
    return p


y = ans([7,1,5,3,6,84])
print(y)