def flippingBits(n):
    # convert decimal to binary. // 4 -> 100
    count = 0
    binary = ""
    while n >= 1:
        rem = n % 2
        binary += str(rem)
        count += 1
        n //= 2
    # reverse the binary by math
    binary = binary[::-1]
    # count the num of digits in binary, add 0s to make it 32 digits
    count = 32 - count
    extra = "0" * count
    binary = extra + binary
    new = ""
    # change 0s to 1s and 1s to 0s
    for char in binary:
        if char == "0":
            new += "1"
        elif char == "1":
            new += "0"
    # print(new)
    new = new[::-1]
    calc = 0
    # convert new binary to decimal
    for i in range(len(new)):
        calc += (2 ** i) * int(new[i])
    return int(calc)
