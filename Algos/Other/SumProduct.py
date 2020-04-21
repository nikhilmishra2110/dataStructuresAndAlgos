def sumProdut(n):
    sum = 0
    product = 1
    while n>0:
        digit = n % 10
        sum += digit
        product *= digit
        n //= 10
    return product - sum

print(sumProdut(983))
