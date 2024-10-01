def check_fill_box(product_list, box_number, max_weight):
    sum = 0
    count = 1
    for product_weight in product_list:
        if product_weight > max_weight:
            return False
        if (sum + product_weight) > max_weight:
            sum = product_weight
            count += 1
        else:
            sum += product_weight
    return count <= box_number

inp = input("Enter Input : ").split("/")
product_list, box_number = list(map(int, inp[0].split())), int(inp[1])

low_weight = max(product_list)
high_weight = sum(product_list)
while low_weight < high_weight:
    mid_weight = (low_weight + high_weight) // 2
    if check_fill_box(product_list, box_number, mid_weight):
        high_weight = mid_weight
    else:
        low_weight = mid_weight + 1

print(f"Minimum weigth for {box_number} box(es) = {low_weight}")