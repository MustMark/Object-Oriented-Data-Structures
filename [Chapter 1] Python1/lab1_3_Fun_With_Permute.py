def permute(original, index = 0, part = []):
    all_answer = []
    if index == len(original)-1:
        temp_answer = []
        part.insert(0, original[-1])
        temp_answer.append(part.copy())
        for count in range(len(original)-1):
            part[count], part[count+1] = part[count+1], part[count]
            temp_answer.append(part.copy())
        part.pop(len(part)-1)
        return temp_answer
    else:
        for count in range(len(part)+1):
            part.insert(count, original[index])
            all_answer.extend(permute(original, index + 1, part))
            part.pop(count)
        return all_answer

print("*** Fun with permute ***")
original = [int(i) for i in input("input : ").split(",")]
print(f"Original Cofllection:  {original}" )
print("Collection of distinct numbers: ")
print(f" {permute(original)}")