def dig_pow(n, p):
    digits = list(map(int, str(n)))
    total = 0
    for digit in digits:
        total += pow(digit, p)
        p += 1
    return total // n if total % n == 0 else -1
