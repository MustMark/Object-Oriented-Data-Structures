def asteroid_collision(asts, i=0):
    if i > len(asts) - 2:
        return asts
    else:
        if asts[i] > 0 and asts[i+1] < 0:
            if asts[i] > abs(asts[i+1]):
                asts.pop(i+1)
            elif asts[i] < abs(asts[i+1]):
                asts.pop(i)
            else:
                asts.pop(i)
                asts.pop(i)
            return asteroid_collision(asts,0)
        else:
            return asteroid_collision(asts,i+1)

x = [int(i) for i in input("Enter Input : ").split(",")]
print(asteroid_collision(x))