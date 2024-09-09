def generate_combinations(digits, current, index, result):
    if current:
        result.append(int(current))
        
    if index == len(digits):
        return

    generate_combinations(digits[:index] + digits[index + 1:], current + digits[index], 0, result)
    generate_combinations(digits, current, index + 1, result)

def combinations(digits):
    result = []
    generate_combinations(digits, '', 0, result)
    return sorted(set(result))

digits = input("Enter digits : ").split(" ")
print(combinations(digits))