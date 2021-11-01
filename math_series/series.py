###################
def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1 or i == 2:
        return 1
    elif i > 2:
        return fibonacci( i - 1 ) + fibonacci( i - 2 )

def lucas(i):
    if i == 0:
        return 2
    elif i == 1:
        return 1
    elif i > 1:
        return lucas( i - 1 ) + lucas( n - 2 )

def sum_series(i, x = 0, j = 1):
    if x == 0 and i == 1:
        return fibonacci( i )
    elif  x == 2 and j == 1:
        return lucas( i )
    else:
        return i - 1 + i - 2