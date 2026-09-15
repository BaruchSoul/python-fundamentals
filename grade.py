try:
    mark = float(input("Enter a mark: "))

    if 85 <= mark <= 100:
        print("A+")
    elif 80 <= mark < 85:
        print("A")
    elif 75 <= mark < 80:
        print("B+")
    elif 70 <= mark < 75:
        print("B")
    elif 65 <= mark < 70:
        print("C+")
    elif 60 <= mark < 65:
        print("C")
    elif 55 <= mark < 60:
        print("D+")
    elif 50 <= mark < 55:
        print("D")
    elif 0 <= mark < 50:
        print("F")
    else:
        print("Invalid! Enter a mark between 0 and 100.")
except ValueError:
    print("Invalid! Enter a number.")


