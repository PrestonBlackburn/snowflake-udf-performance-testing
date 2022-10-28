
def calc_factorials_simple(A, B):

    a = 1
    b = 1
    
    for i in range(1, int(A) + 1):
        a *= i
    
    for j in range(1, int(B) + 1):
        b *= j

    fact_sum = a + b
    
    return fact_sum
    
