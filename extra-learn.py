def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket

print(add_item("apple"))
print(add_item("banana"))

def add_all(*args):
    return sum(args)

print(add_all(1,2))
print(add_all(1,2,3,4,5))




def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="John", age=35, city="Accra")



day=input("Enter day(Mon/Tues/Wed/Thur/Fri/Sat/Sun)")

match day:
    case "Mon":
        print("Start of the week")
    case "Fri":
        print("Almost weekend")