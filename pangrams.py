def pangrams(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    sL = s.lower()
    alp = {}
    for char in sL:
        if char == " ":
            continue
        if char in alphabet:
            alp[char] = 1
        else:
            return "not pangram"
    count = 0
    for key in alp:
        count += 1
    if count == 26:
        return "pangram"
    else:
        return "not pangram"
