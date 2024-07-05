print("*** Fun with permute ***")
original = [int(i) for i in input("input : ").split(",")]
print(f"Original Cofllection: {original}" )
print("Collection of distinct numbers: ")

all = []
rv = original[::-1]
all.append(original[::-1])

for i in range(len(rv)-1):
    rv[i], rv[i+1] = rv[i+1], rv[i]
    all.append(rv)
    print(all)