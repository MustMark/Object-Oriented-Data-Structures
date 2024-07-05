h,w = input("Enter your High and Weight : ").split(" ")
bmi = float(w) / float(h)**2

if bmi < 18.50:
    print("Less Weight")
elif 18.50 <= bmi < 23:
    print("Normal Weight")
elif 23 <= bmi < 25:
    print("More than Normal Weight")
elif 25 <= bmi < 30:
    print("Getting Fat")
elif bmi >= 30:
    print("Fat")