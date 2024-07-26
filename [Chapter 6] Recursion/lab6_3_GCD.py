def find_gcd(n1, n2):
    if n2 == 0:
        return n1
    else:
        n1, n2 = n2, n1%n2
        return find_gcd(n1, n2)  

n1, n2 = [int(i) for i in input("Enter Input : ").split(" ")]

if n1 == 0 and n2 == 0:
    print("Error! must be not all zero.")
elif n1 >= n2:
    print(f"The gcd of {n1} and {n2} is : {find_gcd(abs(n1), abs(n2))}")
else:
    print(f"The gcd of {n2} and {n1} is : {find_gcd(abs(n2), abs(n1))}")
