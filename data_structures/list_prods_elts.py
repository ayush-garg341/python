def find_product(lst):
    fwd_prod = [None] * len(lst)
    fwd_prod[0] = 1
    for i in range(1, len(lst)):
        fwd_prod[i] = lst[i-1] * fwd_prod[i-1]
    
    # print(fwd_prod)

    bwd_prod = [None] * len(lst)
    bwd_prod[-1] = 1
    for i in range(len(lst)-2, -1, -1):
        bwd_prod[i] = lst[i+1] * bwd_prod[i+1]
    
    # print(bwd_prod)

    return [fwd_prod[i]*bwd_prod[i] for i in range(len(lst))]

print(find_product([1, 2, 3, 4]))


def find_product_optimised(lst):
    fwd_prod = []
    prod = 1
    for num in lst:
        fwd_prod.append(prod)
        prod *= num

    prod = 1
    for i in range(len(lst)-1, -1, -1):
        fwd_prod[i] *= prod 
        prod *= lst[i]

    # print(fwd_prod)

    return fwd_prod

print(find_product_optimised([1, 2, 3, 4]))
