code, hint = input("Enter code,hint : ").split(",")

secret_code = []
diff = ord(hint) - ord(code[0])

for i in code:
    secret_code.append(chr(ord(i) + diff))
    print(secret_code)